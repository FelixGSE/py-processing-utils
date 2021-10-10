from typing import List, Any
from point import Point
from triangle import Triangle
from utils import Utils
from random import choice



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
