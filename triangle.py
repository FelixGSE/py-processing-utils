from math import acos
from typing import List
from point import Point
from utils import Utils
from circle import Circle


class Triangle(object):
    def __init__(self, vertex_a: Point, vertex_b: Point, vertex_c: Point) -> None:
        self.A = vertex_a
        self.B = vertex_b
        self.C = vertex_c

    def __repr__(self):

        return f"Triangle(A={self.A},B={self.B},C={self.C})"

    @property
    def a(self) -> float:
        return Utils.euclidean_distance(self.C, self.B)

    @property
    def b(self) -> float:
        return Utils.euclidean_distance(self.A, self.C)

    @property
    def c(self) -> float:
        return Utils.euclidean_distance(self.A, self.B)

    @property
    def U(self) -> float:
        return self.a + self.b + self.c

    @property
    def area(self) -> float:
        return self.U / 2

    @property
    def alpha(self) -> float:
        return acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c))

    @property
    def beta(self) -> float:
        return acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))

    @property
    def gamma(self) -> float:
        return acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b))

    @property
    def sum_of_angles(self):
        return self.alpha + self.beta + self.gamma

    @property
    def segment_a(self) -> List[Point]:
        return [self.B, self.C]

    @property
    def segment_b(self) -> List[Point]:
        return [self.A, self.C]

    @property
    def segment_c(self) -> List[Point]:
        return [self.A, self.B]

    @property
    def inner_circle_center(self) -> Point:
        x = (self.a * self.A.x + self.b * self.B.x + self.c * self.C.x) / (self.a + self.b + self.c)
        y = (self.a * self.A.y + self.b * self.B.y + self.c * self.C.y) / (self.a + self.b + self.c)

        return Point(x, y)

    @property
    def inner_circle_radius(self) -> float:
        return 2 * self.area / self.U

    @property
    def inner_circle(self) -> Circle:
        return Circle(center=self.inner_circle_center, radius=self.inner_circle_radius)

    @property
    def outer_circle_center(self) -> Point:

        d = 2 * (self.A.x * (self.B.y - self.C.y) + self.B.x * (self.C.y - self.A.y) + self.C.x * (self.A.y - self.B.y))

        x = (
            (self.A.x ** 2 + self.A.y ** 2) * (self.B.y - self.C.y)
            + (self.B.x ** 2 + self.B.y ** 2) * (self.C.y - self.A.y)
            + (self.C.x ** 2 + self.C.y ** 2) * (self.A.y - self.B.y)
        ) / d

        y = (
            (self.A.x ** 2 + self.A.y ** 2) * (self.C.x - self.B.x)
            + (self.B.x ** 2 + self.B.y ** 2) * (self.A.x - self.C.x)
            + (self.C.x ** 2 + self.C.y ** 2) * (self.B.x - self.A.x)
        ) / d

        return Point(x, y)

    @property
    def outer_circle_radius(self) -> float:
        return (self.a * self.b * self.c) / (4 * self.area)

    @property
    def outer_circle(self) -> Circle:
        return Circle(center=self.outer_circle_center, radius=self.outer_circle_radius)
