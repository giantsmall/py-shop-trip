from __future__ import annotations
import dataclasses
import math

class Point:
    def __init__(self, location: []):
        self.x = location[0]
        self.y = location[1]

    def calculate_distance(self, point: Point) -> float:
        return round(math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2), 2)