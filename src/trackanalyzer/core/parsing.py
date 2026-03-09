from xml.etree import ElementTree as ET
from trackanalyzer.core.data_models import Track, TrackPoint

def load_kml(file_path: str) -> Track:
    tree = ET.parse(file_path)
    root = tree.getroot()

    print(root)

    print("loading complete")