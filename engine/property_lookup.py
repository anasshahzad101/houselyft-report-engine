"""
property_lookup.py — Toronto data-lookup layer (v1)
House Lyft / SpeedX — owned build. Rebuilt 2026-07-10 from recovered v1
constants + live re-verified endpoints. Consumed by property_lookup_v2.

Pipeline:
    address
      -> geocode       (OSM Nominatim)                  -> lat/lon
      -> ward lookup   (Toronto ArcGIS, live)           -> ward_no + ward_name
      -> zoning lookup (Open Data "Zoning Area" 4326,   -> zone string, density,
                        point-in-polygon via STRtree)      exceptions, holding

SELF-PROVISIONING:
    The 50MB zoning GeoJSON is NOT committed to the repo. On first call,
    if zoning_area.geojson is absent, it is downloaded from Toronto Open
    Data (CKAN, Open Government Licence - Toronto) and cached beside this
    file. Refreshing = delete the file.
"""
import json, os, urllib.parse, urllib.request

from shapely.geometry import shape, Point
from shapely.strtree import STRtree

USER_AGENT = "speedx-property-lookup/2.0"
WARD_ENDPOINT = ("https://gis.toronto.ca/arcgis/rest/services/"
                 "cot_geospatial2/FeatureServer/0/query")
CKAN_PACKAGE = ("https://ckan0.cf.opendata.inter.prod-toronto.ca/"
                "api/3/action/package_show?id=zoning-by-law")
ZONING_RESOURCE = "Zoning Area - 4326.geojson"
ZONING_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "zoning_area.geojson")

# Rule R1 — the 9 sixplex wards (recovered verbatim from v1)
SIXPLEX_WARDS = {"4", "9", "10", "11", "12", "13", "14", "19", "23"}
# Rule R0 — residential zone families that pass the eligibility gate
RESIDENTIAL_ZONES = {"R", "RD", "RS", "RT", "RM", "RA"}


def _http_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    return json.load(urllib.request.urlopen(req, timeout=45))


# ---- step 1: geocode --------------------------------------------------------

def geocode(address):
    q = urllib.parse.urlencode({"q": address, "format": "json", "limit": 1})
    data = _http_json("https://nominatim.openstreetmap.org/search?" + q)
    if not data:
        raise LookupError("Could not geocode: " + address)
    return {"matched": data[0]["display_name"],
            "lat": float(data[0]["lat"]), "lon": float(data[0]["lon"])}


# ---- step 2: ward (live ArcGIS, field names probed 2026-07-10) --------------

def get_ward(lat, lon):
    p = urllib.parse.urlencode({
        "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
        "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
        "outFields": "AREA_SHORT_CODE,AREA_NAME", "returnGeometry": "false",
        "f": "json"})
    d = _http_json(WARD_ENDPOINT + "?" + p)
    feats = d.get("features", [])
    if not feats:
        return {"ward_no": None, "ward_name": None}
    a = feats[0]["attributes"]
    return {"ward_no": str(a.get("AREA_SHORT_CODE")),
            "ward_name": a.get("AREA_NAME")}


# ---- step 3: zoning (ingested Open Data, indexed once per process) ----------

def _ensure_data():
    if os.path.exists(ZONING_PATH):
        return
    pkg = _http_json(CKAN_PACKAGE)
    url = next(r["url"] for r in pkg["result"]["resources"]
               if r.get("name") == ZONING_RESOURCE)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=300) as r, \
         open(ZONING_PATH, "wb") as f:
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            f.write(chunk)


_TREE = None
_PROPS = None

def _index():
    global _TREE, _PROPS
    if _TREE is None:
        _ensure_data()
        gj = json.load(open(ZONING_PATH))
        geoms, props = [], []
        for feat in gj["features"]:
            try:
                geoms.append(shape(feat["geometry"]))
                props.append(feat["properties"])
            except Exception:
                continue
        _TREE, _PROPS = STRtree(geoms), props
    return _TREE, _PROPS



def get_zoning(lat, lon):
    tree, props = _index()
    pt = Point(lon, lat)
    hits = tree.query(pt, predicate="intersects")
    if len(hits) == 0:
        return {"zone": None, "zn_string": None,
                "note": "No zoning polygon at this point (Zoning Area layer)."}
    p = props[int(hits[0])]
    def clean(v):
        return None if v in (-1, -1.0, "", "N") else v
    return {
        "zone": p.get("ZN_STRING") or p.get("ZN_ZONE"),
        "zn_string": p.get("ZN_STRING"),
        "zn_zone": p.get("ZN_ZONE"),
        "density": clean(p.get("DENSITY")),
        "fsi_total": clean(p.get("FSI_TOTAL")),
        "frontage_min_m": clean(p.get("FRONTAGE")),
        "holding": p.get("ZN_HOLDING") == "Y",
        "exception": clean(p.get("ZBL_EXCPTN")) or clean(p.get("EXCPTN_NO")),
        "bylaw_chapter": p.get("ZBL_CHAPT"),
        "bylaw_section": p.get("ZBL_SECTN"),
        "bylaw_ref": "Toronto ZBL 569-2013 (as amended)",
    }


if __name__ == "__main__":
    import sys
    addr = " ".join(sys.argv[1:]) or "303 Coxwell Avenue, Toronto, Ontario"
    g = geocode(addr)
    print(json.dumps({"geo": g, "ward": get_ward(g["lat"], g["lon"]),
                      "zoning": get_zoning(g["lat"], g["lon"])}, indent=1))
