"""
property_lookup_v2.py — Multi-city lookup layer (GTA rollout, city #2)
House Lyft / SpeedX — owned build

Pattern: ONE engine, one ADAPTER per municipality.
An adapter = (a) a zoning data source, (b) that city's verified rules.

  Toronto adapter     : ingested Open Data GeoJSON (50MB, indexed) + ward endpoint
                        rules: 4 as-of-right citywide; 6 in the 9 sixplex wards; ADU stacking OK
  Mississauga adapter : LIVE ArcGIS FeatureServer point query (no download)
                        rules: 4 as-of-right citywide (Dec 2023) in R1-R11, R15, R16, RM1/2/7;
                               NO ADU on a fourplex lot; DC/parkland grant for 4th unit
                               (25-yr rental condition) instead of Toronto's waiver

Both adapter styles are valid; production uses whichever a city offers.
"""

import json, sys, time, urllib.parse, urllib.request

# Reuse Toronto internals from v1 (geocode, ward endpoint, geojson index)
from property_lookup import geocode, get_ward, get_zoning as toronto_zoning, SIXPLEX_WARDS

UA = "speedx-property-lookup/2.0"

# ---------------- Mississauga adapter ----------------

MISS_ZONING = ("https://services6.arcgis.com/hM5ymMLbxIyWTjn2/ArcGIS/rest/services/"
               "Mississauga_Zoning_Bylaw/FeatureServer/0/query")
MISS_FOURPLEX_BASE_ZONES = {"R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11",
                            "R15","R16","RM1","RM2","RM7"}

def _miss_query(lat, lon, distance=None):
    p = {"geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
         "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
         "outFields": "ZONE_CODE,ZONE_DESCRIPTION,ZONE_CATEGORY,BASE_ZONE_DESIGNATION,"
                      "EXCEPTION_ZONE_NUMBER,GREENLANDS_OVERLAY,BYLAW,HOLDING_PROVISION",
         "returnGeometry": "false", "f": "json"}
    if distance:
        p["distance"] = distance
        p["units"] = "esriSRUnit_Meter"
    req = urllib.request.Request(f"{MISS_ZONING}?{urllib.parse.urlencode(p)}",
                                 headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r).get("features", [])

def mississauga_zoning(lat, lon):
    # Exact-point query first. Geocoded coordinates sometimes land in a road
    # allowance or a sliver gap between zoning polygons and return nothing; in
    # that case escalate a small search buffer and take the majority zone found
    # (the parcel that surrounds the point), so a good address is not lost to a
    # few metres of geocode drift.
    f = _miss_query(lat, lon)
    if not f:
        for d in (20, 40):
            f = _miss_query(lat, lon, distance=d)
            if f:
                codes = [x["attributes"].get("ZONE_CODE") for x in f]
                top = max(set(codes), key=codes.count)
                f = [x for x in f if x["attributes"].get("ZONE_CODE") == top]
                break
    if not f:
        return None
    a = f[0]["attributes"]
    return {"zone": a.get("ZONE_CODE"), "base_zone": a.get("BASE_ZONE_DESIGNATION"),
            "category": a.get("ZONE_CATEGORY"), "description": a.get("ZONE_DESCRIPTION"),
            "exception": a.get("EXCEPTION_ZONE_NUMBER"),
            "greenlands_overlay": a.get("GREENLANDS_OVERLAY") == "Y",
            "holding": a.get("HOLDING_PROVISION") == "Y",
            "bylaw_ref": f"Mississauga ZBL {a.get('BYLAW')}"}

def mississauga_rules(z):
    gate = (z or {}).get("category") == "Residential"
    fourplex = gate and (z.get("base_zone") in MISS_FOURPLEX_BASE_ZONES)
    flags = []
    if z and z.get("greenlands_overlay"): flags.append("Greenlands overlay — environmental review likely; confirm in Phase 2")
    if z and z.get("holding"): flags.append("Holding provision on zone — confirm in Phase 2")
    return {
        "gate_pass": gate,
        "main_units_max": 4 if fourplex else (3 if gate else 0),   # Bill 23 floor = 3
        "sixplex_as_of_right": False,
        "adu_stacking_on_multiplex": False,   # Mississauga: no ARU on a fourplex lot
        "incentive_note": "DC + cash-in-lieu-of-parkland GRANT for 4th unit "
                          "(rental 25 yrs, no condo conversion) + permit-fee refund — "
                          "NOT a blanket waiver like Toronto. Confirm in Phase 2.",
        "flags": flags,
    }

# ---------------- Brampton adapter ----------------

BRAMPTON_ARU = ("https://maps1.brampton.ca/arcgis/rest/services/"
                "ARU_SEARCH/ARU_SEARCH/MapServer/1/query")

def brampton_zoning(lat, lon):
    """Brampton ARU_SEARCH layer: per-parcel zoning + City-computed ADU feasibility."""
    params = urllib.parse.urlencode({
        "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
        "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
        "outFields": "ZONING,PARCELAREA,HOUSEAREA,GARAGEAREA,ADUAREA,ADUMIN,ADUMAX,DECISION,ADDRANGE",
        "returnGeometry": "false", "f": "json"})
    req = urllib.request.Request(f"{BRAMPTON_ARU}?{params}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        out = json.load(r)
    f = out.get("features", [])
    if not f:
        return None
    a = f[0]["attributes"]
    return {"zone": a.get("ZONING"),
            "parcel_area_sqm": a.get("PARCELAREA"),
            "house_area_sqm": a.get("HOUSEAREA"),
            "garage_area_sqm": a.get("GARAGEAREA"),
            "adu_buildable_sqm": a.get("ADUAREA"),
            "adu_min_sqm": a.get("ADUMIN"), "adu_max_sqm": a.get("ADUMAX"),
            "city_adu_decision": a.get("DECISION"),
            "parcel_address": a.get("ADDRANGE"),
            "bylaw_ref": "Brampton ARU framework (ZBL 270-2004 as amended)"}

def brampton_rules(z):
    gate = bool(z) and str(z.get("zone") or "").upper().startswith("R")
    adu_ok = bool(z) and str(z.get("city_adu_decision") or "").lower().startswith("yes")
    return {
        "gate_pass": gate,
        "main_units_max": 3 if gate else 0,   # Bill 23 floor — NO fourplex as-of-right in Brampton
        "unit_combo": "principal + 1 attached second unit + 1 garden suite (max 3 total)",
        "sixplex_as_of_right": False,
        "adu_allowed_city_computed": adu_ok,
        "incentive_note": "ARUs MUST be registered with the City to be legal; citywide "
                          "Residential Rental Licence required for 1-4 unit rentals "
                          "from Jan 1 2026. Confirm in Phase 2.",
        "flags": ["Garden suite approval starts at Planning Division (before building permit)",
                  "CVC/TRCA conservation-authority approval required if on regulated lands — confirm in Phase 2",
                  "Parcel/ADU areas are City-computed screening values — confirm in Phase 2"],
    }

# ---------------- Vaughan adapter ----------------

VAUGHAN_BASE = "https://services2.arcgis.com/9LnN9037wYhPG904/arcgis/rest/services"

def _vaughan_query(layer_url, lat, lon):
    params = urllib.parse.urlencode({
        "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
        "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
        "outFields": "ZONE,ZONE1,EXCEPTION,SCHEDULE,Suffix",
        "returnGeometry": "false", "f": "json"})
    req = urllib.request.Request(f"{layer_url}/query?{params}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        out = json.load(r)
    f = out.get("features", [])
    return f[0]["attributes"] if f else None

def vaughan_zoning(lat, lon):
    """Vaughan runs TWO bylaws in parallel: ZBL 001-2021 (new) with legacy 1-88
    still applicable in some areas. Query 1-21 first, fall back to 1-88."""
    a = _vaughan_query(f"{VAUGHAN_BASE}/Zoning1_21v/FeatureServer/0", lat, lon)
    bylaw = "Vaughan ZBL 001-2021"
    if not a:
        a = _vaughan_query(f"{VAUGHAN_BASE}/Zoning1_88_v/FeatureServer/0", lat, lon)
        bylaw = "Vaughan ZBL 1-88 (legacy — area not yet under 001-2021)"
    if not a:
        return None
    return {"zone": a.get("ZONE"), "zone_name": a.get("ZONE1"),
            "exception": a.get("EXCEPTION"), "schedule": a.get("SCHEDULE"),
            "suffix": a.get("Suffix"), "bylaw_ref": bylaw}

def vaughan_rules(z):
    gate = bool(z) and str(z.get("zone") or "").upper().startswith("R")
    flags = []
    if z and z.get("suffix") and "EN" in str(z.get("suffix")):
        flags.append("(EN) Established Neighbourhood suffix — infill/character rules may apply; confirm in Phase 2")
    if z and "1-88" in (z.get("bylaw_ref") or ""):
        flags.append("Legacy By-law 1-88 area — dual-bylaw regime; confirm governing bylaw in Phase 2")
    flags.append("Greenbelt / Oak Ridges Moraine / TRCA overlays possible — City publishes a Greenbelt-ORM layer (auto-check to wire); confirm in Phase 2")
    return {
        "gate_pass": gate,
        "main_units_max": 3 if gate else 0,   # By-law 082-2025: principal + max 2 ARUs
        "unit_combo": "principal + 2 additional residential units, max 1 in a detached accessory building (By-law 082-2025, Mar 2025)",
        "sixplex_as_of_right": False,
        "incentive_note": "ARU permissions per By-law 082-2025; no fourplex as-of-right found. Confirm in Phase 2.",
        "flags": flags,
    }

# ---------------- Markham adapter ----------------

MARKHAM_BASE = ("https://services3.arcgis.com/OWiFbQmr7Eu5DHn1/arcgis/rest/services/"
                "MarkhamZoning/FeatureServer")

def _markham_query(layer, lat, lon, fields="*"):
    params = urllib.parse.urlencode({
        "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
        "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
        "outFields": fields, "returnGeometry": "false", "f": "json"})
    req = urllib.request.Request(f"{MARKHAM_BASE}/{layer}/query?{params}",
                                 headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        out = json.load(r)
    return out.get("features", [])

def markham_zoning(lat, lon):
    """Markham consolidated zoning (layer 10) + heritage district check (layer 1).
    Service also exposes ORM, floodplain, exceptions, parcels — wireable later."""
    z = _markham_query(10, lat, lon, "ZONE_CODE,ZONE_DESC")
    if not z:
        return None
    a = z[0]["attributes"]
    heritage = len(_markham_query(1, lat, lon, "OBJECTID")) > 0
    return {"zone": a.get("ZONE_CODE"), "zone_name": a.get("ZONE_DESC"),
            "heritage_district": heritage,
            "bylaw_ref": "Markham consolidated zoning (City GIS)"}

def markham_rules(z):
    gate = bool(z) and str(z.get("zone") or "").upper().startswith("RES")
    flags = []
    if z and z.get("heritage_district"):
        flags.append("Heritage Conservation District — heritage review applies to any build; confirm in Phase 2")
    flags.append("Two-unit houses must be REGISTERED with the City (fire inspection + registration fees)")
    flags.append("ARUs excluded in environmentally sensitive areas — ORM/floodplain layers available to auto-check; confirm in Phase 2")
    return {
        "gate_pass": gate,
        "main_units_max": 3 if gate else 0,   # Bill 23 floor — City-confirmed (3 units per urban residential lot)
        "unit_combo": "principal + 2 additional residential units (Bill 23)",
        "pending_change": "Council endorsed HAF amendments (Dec 2023) to allow up to 4 units total "
                          "(3 ARUs) — in progress, NOT in force; confirm status per report",
        "sixplex_as_of_right": False,
        "incentive_note": "ARU garden suites currently DC-exempt under provincial legislation. Confirm in Phase 2.",
        "flags": flags,
    }

# ---------------- Oakville adapter ----------------

OAKVILLE_1414 = ("https://maps.oakville.ca/oakgis/rest/services/SBS/"
                 "Zoning_By_law_2014_014/FeatureServer/10")
OAKVILLE_2009 = ("https://maps.oakville.ca/oakgis/rest/services/SBS/"
                 "Zoning_By_law_2009_189/FeatureServer/4")

def _oakville_query(url, lat, lon):
    params = urllib.parse.urlencode({
        "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
        "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
        "outFields": "ZONE,CLASS,SP_NA,HOLD_NA,ZONE_URL,GROWTH_AREA",
        "returnGeometry": "false", "f": "json"})
    req = urllib.request.Request(f"{url}/query?{params}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        out = json.load(r)
    f = out.get("features", [])
    return f[0]["attributes"] if f else None

def oakville_zoning(lat, lon):
    """Oakville dual-bylaw: ZBL 2014-014 (south of Dundas), legacy 2009-189 (North Oakville)."""
    a = _oakville_query(OAKVILLE_1414, lat, lon)
    bylaw = "Oakville ZBL 2014-014 (as amended by 2024-053/054/111)"
    if not a:
        a = _oakville_query(OAKVILLE_2009, lat, lon)
        bylaw = "Oakville ZBL 2009-189 (North Oakville)"
    if not a:
        return None
    return {"zone": a.get("ZONE"), "zone_name": a.get("CLASS"),
            "special_provision": (a.get("SP_NA") not in (None, "Not Applicable")),
            "holding": (a.get("HOLD_NA") not in (None, "Not Applicable")),
            "growth_area": a.get("GROWTH_AREA"),
            "bylaw_pdf": a.get("ZONE_URL"), "bylaw_ref": bylaw}

def oakville_rules(z):
    zone = str((z or {}).get("zone") or "").upper()
    gate = zone.startswith("R")
    flags = []
    if zone.endswith("-0"):
        flags.append("'-0' suffix zone — established-neighbourhood character regulations apply; confirm in Phase 2")
    if z and z.get("special_provision"):
        flags.append("Special Provision on this zone — site-specific rules; confirm in Phase 2")
    if z and z.get("holding"):
        flags.append("Holding provision — confirm in Phase 2")
    if z and "2009-189" in (z.get("bylaw_ref") or ""):
        flags.append("North Oakville legacy by-law area — dual-bylaw regime; confirm governing text in Phase 2")
    flags.append("Conservation Halton permits may apply near ravines/creeks; heritage districts (Old Oakville, Bronte) add design review; tree protection by-law applies — confirm in Phase 2")
    return {
        "gate_pass": gate,
        "main_units_max": 3 if gate else 0,   # Bill 23 floor — verified
        "unit_combo": "principal + attached ADU(s) + detached ARU per By-laws 2024-053/054/111",
        "conflict_note": "Some 2026 sources report 4 units as-of-right under Livable Oakville updates — "
                         "NOT confirmed in official text found; verify against By-law 2024-053/054 before citing.",
        "sixplex_as_of_right": False,
        "incentive_note": "ADU registration fee reported (~$800); ARU DC exemptions per provincial rules. Confirm in Phase 2.",
        "flags": flags,
    }

# ---------------- Richmond Hill adapter ----------------

RH_BASE = ("https://services5.arcgis.com/cu2HFDk7AqvG7e31/arcgis/rest/services/"
           "CZBL_Schedules/FeatureServer")

def _rh_query(layer, lat, lon, fields="*", count_only=False):
    p = {"geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
         "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
         "returnGeometry": "false", "f": "json"}
    if count_only:
        p["returnCountOnly"] = "true"
    else:
        p["outFields"] = fields
    req = urllib.request.Request(f"{RH_BASE}/{layer}/query?{urllib.parse.urlencode(p)}",
                                 headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        out = json.load(r)
    if count_only:
        return out.get("count", 0)
    f = out.get("features", [])
    return f[0]["attributes"] if f else None

def richmondhill_zoning(lat, lon):
    """Richmond Hill CZBL 93-25 Schedule A (layer 5) + overlay checks.
    STATUS field encodes per-polygon OLT appeal state — the transition flag
    fills itself from the City's own data."""
    a = _rh_query(5, lat, lon, "ZONECODE,ZONENAME,ZONECATEGORY,STATUS,GENERALPROVISIONS,Link")
    if not a:
        return None
    return {"zone": a.get("ZONECODE"), "zone_name": a.get("ZONENAME"),
            "category": a.get("ZONECATEGORY"), "czbl_status": a.get("STATUS"),
            "bylaw_pdf": a.get("Link"),
            "orm": _rh_query(8, lat, lon, count_only=True) > 0,
            "greenbelt": _rh_query(21, lat, lon, count_only=True) > 0,
            "trca": _rh_query(15, lat, lon, count_only=True) > 0,
            "bylaw_ref": "Richmond Hill CZBL 93-25 (Sept 24, 2025)"}

def richmondhill_rules(z):
    gate = bool(z) and (z.get("category") == "Neighbourhood"
                        or str(z.get("zone") or "").upper().startswith("N"))
    flags = []
    if z and str(z.get("czbl_status") or "").lower().startswith("under appeal"):
        flags.append("CZBL 93-25 zone is UNDER OLT APPEAL (OLT-25-000843) — legacy parent "
                     "by-law may currently govern (Section 1.12 transition); confirm governing "
                     "by-law in Phase 2")
    if z and z.get("orm"): flags.append("Oak Ridges Moraine Conservation Plan Area — ARUs excluded in Natural Core/Linkage; confirm in Phase 2")
    if z and z.get("greenbelt"): flags.append("Greenbelt Plan Area — confirm in Phase 2")
    if z and z.get("trca"): flags.append("TRCA Regulation Limit — conservation permit likely; confirm in Phase 2")
    flags.append("4-unit permission is via the ARU pathway; a purpose-built multiplex teardown may still require amendments — confirm in Phase 2")
    return {
        "gate_pass": gate,
        "main_units_max": 4 if gate else 0,   # OPA 58 + By-laws 143-24/144-24 (Dec 11, 2024) — IN FORCE
        "unit_combo": "principal + up to 3 additional residential units, max 1 detached "
                      "(By-laws 143-24/144-24, Dec 2024 — first York Region city at 4)",
        "sixplex_as_of_right": False,
        "accuracy_note": "Many sources still report Richmond Hill at 3 units — 4 has been "
                         "in force since Dec 2024. State 4, cite the by-laws.",
        "incentive_note": "ARU DC exemptions per provincial rules; parking nuances "
                          "(tandem OK, narrow-frontage exemptions). Confirm in Phase 2.",
        "flags": flags,
    }

# ---------------- Burlington adapter ----------------

BURLINGTON_ZBL = ("https://mapping.burlington.ca/arcgisweb/rest/services/COB/"
                  "Zoning_ByLaw/MapServer/6")

def burlington_zoning(lat, lon):
    params = urllib.parse.urlencode({
        "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
        "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
        "outFields": "FULL_ZONING,VIEWER_HTML",
        "returnGeometry": "false", "f": "json"})
    req = urllib.request.Request(f"{BURLINGTON_ZBL}/query?{params}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        out = json.load(r)
    f = out.get("features", [])
    if not f:
        return None
    a = f[0]["attributes"]
    return {"zone": a.get("FULL_ZONING"),
            "bylaw_page": (a.get("VIEWER_HTML") or "").strip(),
            "bylaw_ref": "Burlington Zoning By-law 2020 (as amended; OPA 3 + ZBA Jan 28, 2025)"}

def burlington_rules(z):
    gate = bool(z) and str(z.get("zone") or "").upper().startswith("R")
    return {
        "gate_pass": gate,
        "main_units_max": 4 if gate else 0,   # OPA 3 + Zoning Bylaw amendment, Jan 28 2025
        "unit_combo": "principal + up to 3 additional residential units per urban residential lot "
                      "(OPA 3 + ZBA, Jan 28, 2025 — HAF-driven)",
        "sixplex_as_of_right": False,
        "accuracy_note": "Second Halton/GTA city confirmed at 4 as-of-right. Early-2025 reporting "
                         "noted the implementing ZBA followed OPA 3 — confirm governing text per lot in Phase 2.",
        "incentive_note": "Burlington Affordable Rental Housing CIP (Apr 15, 2025): 10 incentive "
                          "programs incl. a FORGIVABLE LOAN for ARUs (10-yr affordability term, "
                          "affordable-rent cap) + provincial ARU DC exemptions. Confirm in Phase 2.",
        "flags": ["New Zoning Bylaw Project ongoing — ZBL 2020 evolving; confirm current text in Phase 2",
                  "Conservation Halton permits may apply near creeks / Lake Ontario lands — confirm in Phase 2"],
    }

# ---------------- Oshawa adapter ----------------

OSHAWA_ZONING = ("https://services5.arcgis.com/eZ3RGx53Xjn5cGa6/arcgis/rest/services/"
                 "Oshawa_Zoning/FeatureServer/0")

# ZBL 60-94 s.5.12: accessory apartments permitted in these residential/ORM/agri zones
OSHAWA_ARU_ZONE_PREFIXES = ("R1", "R2", "R3", "R5", "OSR-A", "OS-ORM", "AG-A", "AG-B", "AG-ORM")

def oshawa_zoning(lat, lon):
    params = urllib.parse.urlencode({
        "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
        "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
        "outFields": "ZoningCode,ZoningCategory,ZoningType,ZoningURL,Notes",
        "returnGeometry": "false", "f": "json"})
    req = urllib.request.Request(f"{OSHAWA_ZONING}/query?{params}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        out = json.load(r)
    f = out.get("features", [])
    if not f:
        return None
    a = f[0]["attributes"]
    def clean(v): return None if v in (None, "", "Not Available") else v
    return {"zone": a.get("ZoningCode"),
            "category": clean(a.get("ZoningCategory")),
            "type": clean(a.get("ZoningType")),
            "notes": clean(a.get("Notes")),
            "bylaw_page": (a.get("ZoningURL") or "").strip(),
            "bylaw_ref": "Oshawa Zoning By-law 60-94 (as amended)"}

def oshawa_rules(z):
    zone = str((z or {}).get("zone") or "").upper()
    gate = zone.startswith(OSHAWA_ARU_ZONE_PREFIXES)
    return {
        "gate_pass": gate,
        "main_units_max": 3 if gate else 0,   # ZBL 60-94 s.5.12 — max 3 units, max 1 in accessory bldg
        "unit_combo": "principal + accessory apartment(s), max 3 units total, "
                      "max 1 in an accessory building (ZBL 60-94 s.5.12)",
        "sixplex_as_of_right": False,
        "incentive_note": "Accessory apt in accessory building capped ~60 m2 (90 m2 in R1-G/R1-H); "
                          "parking: 4 spaces for a 3-unit property, 3 with direct street access "
                          "(no tandem). Provincial ARU DC exemptions. Confirm in Phase 2.",
        "flags": ["Excluded on CLOCA hazard lands / lands without safe access — confirm in Phase 2",
                  "Not permitted where main dwelling is an interim 'h' holding use — confirm in Phase 2"],
    }

# ---------------- Toronto adapter (wraps v1) ----------------

def toronto_rules(zoning, ward):
    zone_fam = (zoning.get("zone") or "").split()[0].upper() if zoning.get("zone") else ""
    gate = zone_fam in {"R","RD","RS","RT","RM","RA"}
    six = ward.get("ward_no") in SIXPLEX_WARDS
    return {"gate_pass": gate,
            "main_units_max": 6 if (gate and six) else (4 if gate else 0),
            "sixplex_as_of_right": six,
            "adu_stacking_on_multiplex": True,   # garden/laneway suite may stack (per bylaw rules)
            "incentive_note": "Toronto DC waiver up to 6 units (Bill 185) — confirm in Phase 2.",
            "flags": []}

# ---------------- Router ----------------



# ---------------------------------------------------------------- Edmonton
# Zoning Bylaw 20001 (in force Jan 1, 2024; replaced ZBL 12800).
# Rules verified 2026-07-11:
#   - RS (Small Scale Residential) consolidates RF1-RF4; row/multi-unit
#     housing permitted by default (edmonton.ca ZBL 20001 guide).
#   - Mid-block maximum reduced 8 -> 6 dwellings in the one-year-review
#     amendments (mid-2025); developments of MORE than 8 dwellings are
#     limited to corner sites (Residential Land Use Matrix note).
#   - Backyard housing permitted; counts toward total dwellings on site.
#   - Height: 10.5 m now; drops to 9.5 m for applications from Aug 1, 2026
#     (approved Apr 27, 2026) — TIME-SENSITIVE for anything in design now.
#   - Since Jul 8, 2025: max two dwelling entrances facing an interior side
#     lot line; a side-facing entrance triggers a 1.9 m setback on that side.
EDMONTON_FS = ("https://gis.edmonton.ca/site1/rest/services/"
               "ZoningWebApp/Zoning_Map/FeatureServer")
EDMONTON_RES_ZONES = ("RS", "RSF", "RSM", "RM", "RL", "RR")

def _edm_point(layer, lat, lon, fields="*"):
    params = urllib.parse.urlencode({
        "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
        "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
        "outFields": fields, "returnGeometry": "false", "f": "json"})
    req = urllib.request.Request(f"{EDMONTON_FS}/{layer}/query?{params}",
                                 headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        out = json.load(r)
    f = out.get("features", [])
    return f[0]["attributes"] if f else None

def edmonton_zoning(lat, lon):
    z = _edm_point(5, lat, lon, "ZONING,ZONING_STRING,BYLAW_NO,STATUS")
    if not z:
        return None
    ward = _edm_point(34, lat, lon, "DESCRIPTIVE_NAME,COUNCILLOR1") or {}
    hood = _edm_point(35, lat, lon, "DESCRIPTIVE_NAME,DESCRIPTION") or {}
    league = _edm_point(36, lat, lon, "NAME") or {}
    flood = _edm_point(7, lat, lon, "OBJECTID")
    airport = _edm_point(9, lat, lon, "OBJECTID")
    return {
        "zone": z.get("ZONING"),
        "zn_string": z.get("ZONING_STRING") or z.get("ZONING"),
        "bylaw_ref": f"Edmonton Zoning Bylaw {z.get('BYLAW_NO') or '20001'}",
        "ward": ward.get("DESCRIPTIVE_NAME"),
        "councillor": ward.get("COUNCILLOR1"),
        "neighbourhood": hood.get("DESCRIPTIVE_NAME"),
        "neighbourhood_desc": (hood.get("DESCRIPTION") or "")[:600] or None,
        "community_league": league.get("NAME"),
        "flags": [f for f, hit in
                  [("Floodplain Protection Overlay — verify in design", flood),
                   ("Airport Protection Overlay — verify in design", airport)] if hit],
    }

def edmonton_rules(z):
    zone = str((z or {}).get("zone") or "").upper()
    gate = zone.startswith(EDMONTON_RES_ZONES)
    rs = zone == "RS"
    return {
        "gate_pass": gate,
        "main_units_max": 6 if rs else (None if gate else 0),
        "corner_units_max": 8 if rs else None,
        "unit_combo": ("RS: up to 6 dwellings mid-block as-of-right "
                       "(one-year-review amendment, 2025; down from 8); up to 8 on "
                       "corner sites, and developments of more than 8 dwellings are "
                       "limited to corner sites per the Residential Matrix. Backyard "
                       "housing permitted and counts toward the total.") if rs else
                      (f"{zone}: residential zone under ZBL 20001 — detailed unit "
                       "rulebook not yet encoded; treat as needs-review." if gate else
                       "Not a small-scale residential zone."),
        "sixplex_as_of_right": rs,
        "adu_stacking_on_multiplex": rs,
        "incentive_note": ("TIME-SENSITIVE: RS max height drops 10.5 m -> 9.5 m for "
                           "applications from Aug 1, 2026 (approved Apr 27, 2026) — "
                           "file before the cut-off to keep the 10.5 m envelope. "
                           "Since Jul 8, 2025 max two entrances may face an interior "
                           "side lot line; side entrances trigger a 1.9 m setback. "
                           "No DC-waiver equivalent — Edmonton incentives differ from "
                           "Ontario programs; verify per project.") if rs else
                          "Verify zone-specific incentives per project.",
        "source": "gis.edmonton.ca ZoningWebApp (live) + ZBL 20001, verified 2026-07-11",
    }


def detect_city(display_name):
    dn = display_name.lower()
    if "mississauga" in dn: return "Mississauga"
    if "brampton" in dn: return "Brampton"
    if "vaughan" in dn: return "Vaughan"
    if "markham" in dn: return "Markham"
    if "oakville" in dn: return "Oakville"
    if "richmond hill" in dn: return "Richmond Hill"
    if "burlington" in dn: return "Burlington"
    if "oshawa" in dn: return "Oshawa"
    if "toronto" in dn: return "Toronto"
    if "edmonton" in dn: return "Edmonton"
    return None

def lookup(address):
    geo = geocode(address)
    city = detect_city(geo["matched"])
    out = {"address": address, "matched": geo["matched"],
           "coordinates": {"lat": geo["lat"], "lon": geo["lon"]}, "city": city}
    if city == "Mississauga":
        z = mississauga_zoning(geo["lat"], geo["lon"])
        out["zoning"] = z
        out["engine"] = mississauga_rules(z)
        out["source"] = "Zoning: City of Mississauga ArcGIS FeatureServer (live). Geocode: OSM."
    elif city == "Brampton":
        z = brampton_zoning(geo["lat"], geo["lon"])
        out["zoning"] = z
        out["engine"] = brampton_rules(z)
        out["source"] = "Zoning + ADU feasibility: City of Brampton ArcGIS (ARU_SEARCH, live). Geocode: OSM."
    elif city == "Vaughan":
        z = vaughan_zoning(geo["lat"], geo["lon"])
        out["zoning"] = z
        out["engine"] = vaughan_rules(z)
        out["source"] = "Zoning: City of Vaughan ArcGIS (ZBL 001-2021 + 1-88 fallback, live). Geocode: OSM."
    elif city == "Markham":
        z = markham_zoning(geo["lat"], geo["lon"])
        out["zoning"] = z
        out["engine"] = markham_rules(z)
        out["source"] = "Zoning + heritage: City of Markham ArcGIS (live). Geocode: OSM."
    elif city == "Oakville":
        z = oakville_zoning(geo["lat"], geo["lon"])
        out["zoning"] = z
        out["engine"] = oakville_rules(z)
        out["source"] = "Zoning: Town of Oakville GIS (ZBL 2014-014 + 2009-189 fallback, live). Geocode: OSM."
    elif city == "Richmond Hill":
        z = richmondhill_zoning(geo["lat"], geo["lon"])
        out["zoning"] = z
        out["engine"] = richmondhill_rules(z)
        out["source"] = "Zoning + overlays: City of Richmond Hill ArcGIS (CZBL 93-25 Schedule A, live). Geocode: OSM."
    elif city == "Burlington":
        z = burlington_zoning(geo["lat"], geo["lon"])
        out["zoning"] = z
        out["engine"] = burlington_rules(z)
        out["source"] = "Zoning: City of Burlington GIS (ZBL 2020, live). Geocode: OSM."
    elif city == "Oshawa":
        z = oshawa_zoning(geo["lat"], geo["lon"])
        out["zoning"] = z
        out["engine"] = oshawa_rules(z)
        out["source"] = "Zoning: City of Oshawa Open Data ArcGIS (ZBL 60-94, live). Geocode: OSM."
    elif city == "Edmonton":
        z = edmonton_zoning(geo["lat"], geo["lon"])
        out["zoning"] = z
        out["engine"] = edmonton_rules(z)
        out["source"] = "gis.edmonton.ca ZoningWebApp FeatureServer (live)"
    elif city == "Toronto":
        z = toronto_zoning(geo["lat"], geo["lon"])
        w = get_ward(geo["lat"], geo["lon"])
        out["zoning"], out["ward"] = z, w
        out["engine"] = toronto_rules(z, w)
        out["source"] = "Zoning: Toronto Open Data (ingested). Ward: Toronto ArcGIS. Geocode: OSM."
    else:
        out["engine"] = {"gate_pass": False,
                         "note": f"No adapter for this municipality yet — route to manual review."}
    return out

if __name__ == "__main__":
    addr = " ".join(sys.argv[1:]) or "1518 Carmen Drive, Mississauga, Ontario"
    t0 = time.time()
    r = lookup(addr)
    r["_elapsed_sec"] = round(time.time() - t0, 2)
    print(json.dumps(r, indent=2))
