from point import Point
from utils import Utils
from triangle import Triangle
from math import pi
from typing import List


class Arc(object):
    def __init__(self, center: Point, radius: float, start_angle: float, stop_angle: float):
        self.center = center
        self.radius = radius
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.inner_triangle = Triangle(vertex_a=self.center, vertex_b=self.right_vertex, vertex_c=self.left_vertex)

    @property
    def right_vertex(self) -> Point:
        return Utils.point_on_circle(center=self.center, radius=self.radius, angle=self.start_angle)

    @property
    def left_vertex(self) -> Point:
        return Utils.point_on_circle(center=self.center, radius=self.radius, angle=self.stop_angle)

    @property
    def chord(self) -> float:
        return self.inner_triangle.a

    @property
    def chord_segment(self) -> List[Point]:
        return self.inner_triangle.segment_a

    @property
    def alpha_radiants(self) -> float:
        return self.stop_angle - self.start_angle

    @property
    def alpha_degrees(self) -> float:
        return Utils.radians_to_degrees(self.stop_angle - self.start_angle)

    @property
    def area(self) -> float:
        return pi * self.radius ** 2 * (self.alpha_degrees / 360)

    @property
    def arc_length(self) -> float:
        return pi * self.radius * self.alpha_radiants / 360

    def get_point_on_arc(self, angle: float) -> Point:
        if not self.start_angle <= angle <= self.stop_angle:
            raise ValueError(f"Angle must be va value between {self.start_angle} and {self.stop_angle}. Got {angle}")
        return Utils.point_on_circle(center=self.center, radius=self.radius, angle=angle)
