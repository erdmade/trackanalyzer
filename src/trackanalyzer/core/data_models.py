from dataclasses import dataclass
from datetime import datetime

@dataclass
class TrackPoint:
    latitude: float
    longitude: float
    elevation: float
    time: datetime

@dataclass
class Track:
    name: str
    points: list[TrackPoint]

    