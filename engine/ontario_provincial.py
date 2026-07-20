"""
Ontario provincial aerial imagery provider (OIWMS).

Province-wide fallback for aerial_imagery.py — covers every Ontario
municipality in one adapter. Register BELOW city-specific high-res
adapters (Toronto 8cm, Brampton) and ABOVE the Mapbox fallback.

Source:  Ontario Imagery Web Map Service (Geospatial Ontario / LIO)
         Cached ArcGIS tile service, Web Mercator, levels 0-23.
Licence: Open data, free, commercial use permitted with attribution.
Caption: "Aerial imagery: Ontario Imagery Web Map Service,
          © King's Printer for Ontario"

Verified 2026-07-20 against: Mississauga, Vaughan, Markham,
Richmond Hill, Oakville, Burlington, Oshawa, Cambridge.
"""

import io
import math
import time
import urllib.request

from PIL import Image

OIWMS_TILE = (
    "https://ws.lioservices.lrc.gov.on.ca/arcgis1071a/rest/services/"
    "LIO_Imagery/Ontario_Imagery_Web_Map_Service/MapServer/tile"
)
SOURCE_LABEL = "Ontario Imagery Web Map Service, © King's Printer for Ontario"

DEFAULT_ZOOM = 19
MAX_ZOOM = 21
TIMEOUT = 20
RETRIES = 2


def _tile_xy(lat: float, lon: float, z: int):
    n = 2 ** z
    x = int((lon + 180.0) / 360.0 * n)
    y = int(
        (1.0 - math.log(math.tan(math.radians(lat)) + 1.0 / math.cos(math.radians(lat))) / math.pi)
        / 2.0 * n
    )
    return x, y


def _fetch_tile(z: int, y: int, x: int) -> bytes | None:
    url = f"{OIWMS_TILE}/{z}/{y}/{x}"
    for attempt in range(RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "houselyft-report-engine"})
            return urllib.request.urlopen(req, timeout=TIMEOUT).read()
        except Exception:
            if attempt == RETRIES:
                return None
            time.sleep(1.5 * (attempt + 1))
    return None


def _looks_blank(img: Image.Image) -> bool:
    extrema = img.convert("RGB").getextrema()
    spread = sum(hi - lo for lo, hi in extrema)
    return spread < 60


def fetch_ontario_provincial(
    lat: float,
    lon: float,
    zoom: int = DEFAULT_ZOOM,
    grid: int = 3,
) -> tuple[bytes, str] | None:
    """
    Fetch a stitched (grid x grid) aerial patch centred on the property.
    Returns (jpeg_bytes, source_label) or None so the registry can fall
    through to the next provider (Mapbox).
    """
    zoom = min(zoom, MAX_ZOOM)
    cx, cy = _tile_xy(lat, lon, zoom)
    half = grid // 2

    canvas = Image.new("RGB", (256 * grid, 256 * grid))
    blanks = 0
    for dy in range(-half, half + 1):
        for dx in range(-half, half + 1):
            raw = _fetch_tile(zoom, cy + dy, cx + dx)
            if raw is None:
                return None
            tile = Image.open(io.BytesIO(raw)).convert("RGB")
            if _looks_blank(tile):
                blanks += 1
            canvas.paste(tile, ((dx + half) * 256, (dy + half) * 256))

    if blanks > (grid * grid) // 2:
        return None

    out = io.BytesIO()
    canvas.save(out, format="JPEG", quality=88)
    return out.getvalue(), SOURCE_LABEL
