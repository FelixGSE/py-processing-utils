from dataclasses import dataclass
from math import sqrt, acos, pi
from random import random, choice, seed
from typing import List, Any


@dataclass
class Point:
    x: float
    y: float

    def __repr__(self) -> str:
        return f"Point({self.x},{self.y})"


class Utils(object):
    @staticmethod
    def random_point_on_line(a: Point, b: Point) -> Point:
        random_split = random()
        x = round((1 - random_split) * a.x + random_split * b.x, 2)
        y = round((1 - random_split) * a.y + random_split * b.y, 2)

        return Point(x, y)

    @staticmethod
    def euclidean_distance(a: Point, b: Point) -> float:
        distance = sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

        return distance

    @staticmethod
    def degree_to_radians(degrees: float) -> float:
        if not 0 <= degrees <= 360:
            raise ValueError("Degree must be number between 0 and 360")

        radians = degrees * pi / 180

        return radians

    @staticmethod
    def radians_to_degrees(radians: float) -> float:
        degrees = radians * 180 / pi

        return degrees


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


class Node(object):
    def __init__(self, value: Any):
        self.left = None
        self.data = value
        self.right = None

    def __repr__(self):
        return f"{self.data}"


class TriangleTree(object):
    def __init__(self, root: Node, max_depth: int = 3) -> None:
        self.root = root
        self.max_depth = max_depth

    def split_triangle(self) -> None:
        self._split_triangle(self.root, 1)

    def _split_triangle(self, node: Node, depth: int) -> None:

        depth = depth + 1
        if depth == self.max_depth + 1:
            return

        triangle = node.data
        edge_choice = choice(["a", "b", "c"])
        line_segment = TriangleTree._get_segment_from_edge_choice(triangle, edge_choice)
        split_point = self._point_on_edge(line_segment)

        if edge_choice == "a":
            left = Triangle(triangle.A, split_point, triangle.C)
            right = Triangle(triangle.A, triangle.B, split_point)
        elif edge_choice == "b":
            left = Triangle(triangle.A, triangle.B, split_point)
            right = Triangle(split_point, triangle.B, triangle.C)
        elif edge_choice == "c":
            left = Triangle(split_point, triangle.B, triangle.C)
            right = Triangle(triangle.A, split_point, triangle.C)

        print("Insert: left", "depth", depth)
        node.left = Node(left)
        self._split_triangle(node.left, depth)

        print("Insert: right", "depth", depth)
        node.right = Node(right)
        self._split_triangle(node.right, depth)

    @staticmethod
    def _get_segment_from_edge_choice(triangle: Triangle, edge: str):
        if edge == "a":
            return triangle.segment_a
        elif edge == "b":
            return triangle.segment_b
        elif edge == "c":
            return triangle.segment_b
        else:
            raise ValueError(f"Edge choice must be a,b or c. Got {edge}")

    @staticmethod
    def _point_on_edge(segment: List[Point]) -> Point:
        return Utils.random_point_on_line(*segment)


if __name__ == "__main__":
    A = Point(10, 10)
    B = Point(100, 10)
    C = Point(50, 50)

    initial_triangle = Triangle(A, B, C)
    tree = TriangleTree(root=Node(initial_triangle), max_depth=3)
    tree.split_triangle()
