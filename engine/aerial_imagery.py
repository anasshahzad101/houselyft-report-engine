"""
aerial_imagery.py — House Lyft property report imagery resolver.

Returns a licensed aerial image of a property for the
Development Feasibility & Home Evaluation Report(TM).

HOW IT WORKS
    SOURCES maps a city -> ordered list of candidate endpoints.
    Each candidate is fetched, then VALIDATED at runtime. A source that
    returns a flat/blank tile is discarded and the resolver falls through
    to the next one. Nothing is trusted just because it returned HTTP 200.

    Adding or swapping a city's imagery = one entry in SOURCES.

WHY THE VALIDATION EXISTS
    Municipal ArcGIS services return HTTP 200 with a blank white tile when
    a layer is scale-gated or out of coverage. Without the blank check,
    reports would silently ship with an empty grey square.

LICENSING  (verified 2026-07-09)
    Open Government Licence - Toronto / Ontario / Brampton / Vancouver:
        commercial use AND modification permitted; attribution required.
    Google Maps Platform:
        PROHIBITED in generated documents, print or electronic.
        Do not add a Google source. Ever.
    Esri World_Imagery:
        Publicly exportable but governed by Esri ToU, not an open licence.
        Deliberately excluded pending legal review.
"""

from __future__ import annotations

import io
import math
import json
import os
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from typing import Optional

from PIL import Image, ImageFilter, ImageStat

USER_AGENT = "HouseLyft-PropertyReport/1.0"
TIMEOUT = 45

# Tuned against known-good (Toronto 8cm: ~98k colours) vs known-blank (1 colour).
MIN_UNIQUE_COLOURS = 2_000
MIN_EDGE_STDDEV = 5.0   # was 8.0 - rejected valid low-contrast rural imagery; blankness is already caught by MIN_UNIQUE_COLOURS

OGL = "Contains information licensed under the Open Government Licence \u2013 {}."


# ---------------------------------------------------------------- model

@dataclass
class Source:
    name: str
    url: str
    kind: str                            # "mapserver" | "imageserver" | "mapbox"
    attribution: str
    year: Optional[int] = None
    layers: Optional[str] = None
    target_scale: Optional[int] = None   # spoof dpi to clear a maxScale gate
    min_half_m: float = 0.0              # refuse if caller wants a tighter crop
    notes: str = ""
    extra: dict = field(default_factory=dict)


# ---- verified lot-scale sources -------------------------------------------

TORONTO_2025 = Source(
    name="City of Toronto Orthophoto 2025 (8cm)",
    url="https://gis.toronto.ca/arcgis/rest/services/basemap/cot_ortho_2025_color_8cm/MapServer",
    kind="mapserver", attribution=OGL.format("Toronto"), year=2025,
)

BRAMPTON_2023 = Source(
    name="City of Brampton Orthophoto 2023 (Spring)",
    url="https://maps1.brampton.ca/image/rest/services/Imagery/BRAM2023S_SID_MOSAIC/ImageServer",
    kind="imageserver", attribution=OGL.format("City of Brampton"), year=2023,
)

CRD_ORTHO = Source(
    name="Capital Regional District Orthophoto",
    url="https://mapservices.crd.bc.ca/arcgis/rest/services/Ortho/MapServer",
    kind="mapserver",
    attribution="Contains information licensed under the CRD Open Data Licence.",
)

VANCOUVER_2018 = Source(
    name="City of Vancouver Aerial Basemap",
    url="https://maps.vancouver.ca/server/rest/services/Basemap/april_2018/MapServer",
    kind="mapserver", attribution=OGL.format("Vancouver"), year=2018,
)

# ---- context-scale only ----------------------------------------------------
# Province-wide, but blank below ~150m half-extent and mushy even then.
# Never selected for a lot-scale crop. Kept for wide context insets.
LIO_ONTARIO_CONTEXT = Source(
    name="Ontario Imagery Web Map Service (LIO)",
    url="https://ws.lioservices.lrc.gov.on.ca/arcgis2/rest/services/"
        "LIO_Imagery/Ontario_Imagery_Web_Map_Service_Source/MapServer",
    kind="mapserver", attribution=OGL.format("Ontario"),
    target_scale=1600, min_half_m=150.0,
    notes="Context inset only. Toronto is carved out of this service.",
)

# ---- optional universal fallback ------------------------------------------
# Mapbox ToU permits static images in print/PDF with attribution.
# Inert unless MAPBOX_TOKEN is set.
MAPBOX = Source(
    name="Mapbox Satellite",
    url="https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static",
    kind="mapbox",
    attribution="\u00a9 Mapbox \u00a9 OpenStreetMap \u00a9 Maxar",
    notes="Requires MAPBOX_TOKEN env var. Paid. Commercial print use permitted.",
)


def _chain(*sources: Source) -> list[Source]:
    """Append Mapbox as last resort only when a token is configured."""
    chain = list(sources)
    if os.environ.get("MAPBOX_TOKEN"):
        chain.append(MAPBOX)
    return chain


SOURCES: dict[str, list[Source]] = {
    # verified lot-scale
    "toronto":       _chain(TORONTO_2025),
    "brampton":      _chain(BRAMPTON_2023, LIO_ONTARIO_CONTEXT),
    "vancouver":     _chain(VANCOUVER_2018),
    "saanich":       _chain(CRD_ORTHO),
    "victoria":      _chain(CRD_ORTHO),

    # GAPS — no verified lot-scale municipal source yet.
    # Resolve to context-only (or Mapbox, if enabled). A lot-scale request
    # fails loudly rather than shipping a blank square.
    "mississauga":   _chain(LIO_ONTARIO_CONTEXT),
    "vaughan":       _chain(LIO_ONTARIO_CONTEXT),
    "markham":       _chain(LIO_ONTARIO_CONTEXT),
    "richmond hill": _chain(LIO_ONTARIO_CONTEXT),
    "oakville":      _chain(LIO_ONTARIO_CONTEXT),
    "burlington":    _chain(LIO_ONTARIO_CONTEXT),
    "oshawa":        _chain(LIO_ONTARIO_CONTEXT),
    "cambridge":     _chain(LIO_ONTARIO_CONTEXT),

    # Edmonton: the city publicly serves Pictometry (EagleView) imagery -
    # third-party licence, excluded per the licensing doctrine above. No
    # verified open lot-scale source yet; resolves to nothing (or Mapbox
    # when a token is configured) and fails loudly rather than shipping
    # unlicensed imagery.
    "edmonton":      _chain(),
}


def sources_for(city: str) -> list[Source]:
    return SOURCES.get(city.strip().lower(), _chain(LIO_ONTARIO_CONTEXT))


# ---------------------------------------------------------------- geometry

def to_web_mercator(lat: float, lon: float) -> tuple[float, float]:
    x = lon * 20037508.34 / 180.0
    y = math.log(math.tan((90.0 + lat) * math.pi / 360.0)) / (math.pi / 180.0)
    return x, y * 20037508.34 / 180.0


def geocode(address: str) -> tuple[float, float]:
    q = urllib.parse.urlencode({"q": address, "format": "json", "limit": 1})
    req = urllib.request.Request(
        f"https://nominatim.openstreetmap.org/search?{q}",
        headers={"User-Agent": USER_AGENT},
    )
    data = json.load(urllib.request.urlopen(req, timeout=TIMEOUT))
    if not data:
        raise LookupError(f"Could not geocode: {address}")
    return float(data[0]["lat"]), float(data[0]["lon"])


# ---------------------------------------------------------------- adapters

def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    return urllib.request.urlopen(req, timeout=TIMEOUT).read()


# --- hard monthly cap for the paid Mapbox fallback -------------------------
# The free tier is 50,000 images/month. We stop far below that so a charge is
# impossible. The counter lives in the Apps Script dropbox (persists across
# cloud runs). FAIL-CLOSED: any error checking or bumping the counter means we
# skip Mapbox entirely rather than risk an uncounted paid call.
MAPBOX_MONTHLY_CAP = int(os.environ.get("MAPBOX_MONTHLY_CAP", "10000"))
_DROPBOX_URL = os.environ.get("HL_DROPBOX_URL", "")
_DROPBOX_KEY = os.environ.get("HL_DROPBOX_KEY", "")


def _mapbox_budget_ok(n: int = 1) -> bool:
    """Reserve n Mapbox images this month. True only if under the cap AND the
    counter was successfully incremented. Any failure returns False."""
    if not (_DROPBOX_URL and _DROPBOX_KEY):
        return False
    try:
        import json as _json
        from datetime import datetime, timezone
        month = datetime.now(timezone.utc).strftime("%Y%m")
        q = urllib.parse.urlencode({"action": "mapcount", "key": _DROPBOX_KEY,
                                    "month": month, "n": n, "cap": MAPBOX_MONTHLY_CAP})
        with urllib.request.urlopen(f"{_DROPBOX_URL}?{q}", timeout=15) as r:
            out = _json.loads(r.read().decode())
        return bool(out.get("ok") and out.get("allowed"))
    except Exception:
        return False


def _fetch(src: Source, x: float, y: float, half_m: float, px: int,
           lat: float = 0.0, lon: float = 0.0) -> bytes:
    if src.kind == "mapbox":
        if not _mapbox_budget_ok(1):
            raise RuntimeError("Mapbox monthly cap reached or counter "
                               "unavailable - skipping paid fallback (fail-closed)")
        token = os.environ["MAPBOX_TOKEN"]
        # Mapbox static API renders px*2 device pixels with @2x. To make the
        # image span exactly 2*half_m metres on the ground:
        #   device_px * (156543.03392*cos(lat) / 2^zoom) = 2*half_m
        # Solve for zoom. (The previous formula mis-derived this and produced
        # zoom ~11 -> a 46 km regional view instead of a lot-scale crop.)
        device_px = px * 2
        zoom = math.log2(device_px * 156543.03392 * math.cos(math.radians(lat))
                         / (2.0 * half_m))
        zoom = max(1.0, min(20.0, zoom))
        return _get(f"{src.url}/{lon},{lat},{zoom:.2f}/{px}x{px}@2x"
                    f"?access_token={token}")

    bbox = f"{x - half_m},{y - half_m},{x + half_m},{y + half_m}"

    if src.kind == "mapserver":
        params = {"bbox": bbox, "bboxSR": 3857, "imageSR": 3857,
                  "size": f"{px},{px}", "format": "jpg",
                  "transparent": "false", "f": "image"}
        if src.layers:
            params["layers"] = src.layers
        if src.target_scale:
            # ArcGIS: scale = (metres_across / px) * (dpi / 0.0254)
            # Solve for the dpi that lands on target_scale for ANY px.
            params["dpi"] = max(1, round(src.target_scale * 0.0254 * px
                                         / (half_m * 2.0)))
        endpoint = "/export?"

    elif src.kind == "imageserver":
        params = {"bbox": bbox, "bboxSR": 3857, "imageSR": 3857,
                  "size": f"{px},{px}", "format": "jpgpng", "f": "image"}
        endpoint = "/exportImage?"

    else:
        raise ValueError(f"Unknown adapter kind: {src.kind}")

    return _get(src.url + endpoint + urllib.parse.urlencode(params))


# ---------------------------------------------------------------- validation

def validate(raw: bytes) -> tuple[bool, dict]:
    """Blank-tile and low-detail rejection. This is what makes fallthrough work."""
    try:
        im = Image.open(io.BytesIO(raw)).convert("RGB")
    except Exception as exc:
        return False, {"error": f"undecodable: {exc}"}

    colours = im.getcolors(maxcolors=2_000_000)
    n_unique = len(colours) if colours else 2_000_000

    grey = im.convert("L")
    if grey.size[0] > 800:
        grey = grey.resize((800, 800))
    edges = grey.filter(ImageFilter.FIND_EDGES)
    # FIND_EDGES lights up the image frame; crop it or a flat tile scores ~18.
    w, h = edges.size
    edges = edges.crop((4, 4, w - 4, h - 4))
    edge_sd = ImageStat.Stat(edges).stddev[0]

    ok = n_unique >= MIN_UNIQUE_COLOURS and edge_sd >= MIN_EDGE_STDDEV
    return ok, {"unique_colours": n_unique, "edge_stddev": round(edge_sd, 2)}


# ---------------------------------------------------------------- resolver

@dataclass
class AerialResult:
    image: bytes
    source: Source
    metrics: dict
    lat: float
    lon: float
    caption: str


def get_aerial(address: str, city: str, half_m: float = 45.0, px: int = 1200,
               lat: Optional[float] = None, lon: Optional[float] = None,
               verbose: bool = True) -> Optional[AerialResult]:
    """Best validated aerial for `address`, or None. Caller must handle None."""
    if lat is None or lon is None:
        lat, lon = geocode(address)
    x, y = to_web_mercator(lat, lon)

    for src in sources_for(city):
        if half_m < src.min_half_m:
            if verbose:
                print(f"  [skip] {src.name}: context-only "
                      f"(needs >= {src.min_half_m:.0f}m half-extent)")
            continue
        try:
            raw = _fetch(src, x, y, half_m, px, lat, lon)
        except Exception as exc:
            if verbose:
                print(f"  [skip] {src.name}: fetch failed ({type(exc).__name__})")
            continue

        ok, metrics = validate(raw)
        if not ok:
            if verbose:
                print(f"  [skip] {src.name}: failed validation {metrics}")
            continue

        year = f" ({src.year})" if src.year else ""
        caption = (f"Aerial view of {address}. Approx. {int(half_m * 2)}m across. "
                   f"Source: {src.name}{year}. {src.attribution}")
        if verbose:
            print(f"  [ok]   {src.name} {metrics}")
        return AerialResult(raw, src, metrics, lat, lon, caption)

    if verbose:
        print(f"  [FAIL] no validated lot-scale imagery for '{city}'")
    return None


def coverage_report() -> None:
    print(f"{'city':16s} {'lot-scale source':46s} status")
    print("-" * 78)
    for city, chain in sorted(SOURCES.items()):
        lot = [s for s in chain if s.min_half_m <= 45.0]
        if lot:
            print(f"{city:16s} {lot[0].name[:45]:46s} VERIFIED")
        else:
            print(f"{city:16s} {'(context inset only)':46s} GAP")


if __name__ == "__main__":
    coverage_report()
    print()
    for addr, city in [
        ("303 Coxwell Avenue, Toronto, Ontario", "toronto"),
        ("8850 McLaughlin Road, Brampton, Ontario", "brampton"),
        ("1361 Hastings Street, Saanich, British Columbia", "saanich"),
        ("638 East Broadway, Vancouver, British Columbia", "vancouver"),
        ("258 Victoria Avenue, Cambridge, Ontario", "cambridge"),
        ("300 City Centre Drive, Mississauga, Ontario", "mississauga"),
    ]:
        print(f"\n=== {addr} [{city}] ===")
        try:
            res = get_aerial(addr, city)
        except Exception as exc:
            print(f"  [ERR] {exc}")
            continue
        if res:
            fn = f"out_{city.replace(' ', '_')}.jpg"
            open(fn, "wb").write(res.image)
            print(f"  saved -> {fn}")
