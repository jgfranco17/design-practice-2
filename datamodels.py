import math
import numpy as np
from pydantic import BaseModel, validator


class Board(object):
    """
    Store constants for project board.
    """
    HEIGHT = 78
    WIDTH = 117
    r_width = 0
    r_length = 0


class Vector(BaseModel):
    x: float
    y: float

    def __repr__(self):
        return f'<Vector: x={self.x}, y={self.y}>'

    def __str__(self):
        return f'V({self.x:.2f}, {self.y:.2f})'

    def __len__(self):
        return round(self.resultant())

    def resultant(self):
        return math.sqrt(self.x**2 + self.y**2)

    def angle(self):
        return np.rad2deg(math.atan2(self.y, self.x))


class Region(BaseModel):
    """
    Data class representing frame sizes.
    """
    width: tuple
    length: tuple

    def __repr__(self):
        return f'<Region: width={self.width}, length={self.length}>'

    def __len__(self):
        r_x = self.width[1] - self.width[0]
        r_y = self.length[1] - self.length[0]
        return round(math.sqrt(r_x**2 + r_y**2))


class Point(BaseModel):
    """
    Data class representing each recorded data point taken
    from the video capture. Stores coordinate and timestamp.
    """
    x: int
    y: int
    time: float

    def __repr__(self):
        return f'<Point: x={self.x}, y={self.y}, time={self.time:.3f}>'

    def __str__(self):
        return f'[P({self.x}, {self.y}) t={self.time:.3f}]'

    def __len__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.time == other.time

    @validator("x")
    def check_x_value(cls, x):
        if x < 0 or x > 1500:
            raise ValueError("X-coordinate is out of bounds.")

        return x

    @validator("y")
    def check_y_value(cls, y):
        if y < 0 or y > 1500:
            raise ValueError("Y-coordinate is out of bounds.")
        return y

    @validator("time")
    def is_time_valid(cls, t):
        if t < 0:
            raise ValueError("Invalid time given.")
        return t