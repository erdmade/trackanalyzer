from xml.etree import ElementTree as ET
from trackanalyzer.core.data_models import Track, TrackPoint
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def load_kml(file_path: str) -> Track:

    logger.info("Loading KML file: %s", file_path)
    tree = ET.parse(file_path)
    root = tree.getroot()

    ns = {"kml": root.tag.split("}")[0].strip("{")}
    logger.info("Namespace: %s", str(ns))

    name_elem = root.find(".//kml:Placemark/kml:name", ns)
    name = name_elem.text if name_elem is not None else "Unnamed Track"

    # detect file format Track or LineString
    if root.find(".//kml:Track", ns) is not None:
        points = _parse_track(root, ns)

    elif root.find(".//kml:LineString", ns) is not None:
        points = _parse_linestring(root, ns)

    else:
        raise ValueError("Unsupported KML track format")
    
    return Track(name=name, points=points)


def _parse_track(root, ns):

    whens = root.findall(".//kml:Track/kml:when", ns)
    coords = root.findall(".//kml:Track/kml:coord", ns)

    points = []

    for when, coord in zip(whens, coords):

        if coord.text is None or coord.text.strip == "":
            continue

        lon, lat, *rest = coord.text.split()

        ele = float(rest[0]) if rest else None

        time = datetime.fromisoformat(when.text) if when.text else None

        points.append(TrackPoint(latitude=float(lat),
                                 longitude=float(lon),
                                 elevation=ele,
                                 time=time))
        
    return points

def _parse_linestring(root, ns):
    print("LineString format support not yet implemented")