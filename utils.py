from math import sqrt, pi, sin, cos
from random import random, shuffle
from typing import Iterable, List, Union, Any
from point import Point


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

    @staticmethod
    def random_point_in_circle(center: Union[Iterable,Point], radius: float) -> Point:

        r = radius * sqrt(random())
        theta = random() * 2 * pi
        x = center[0] + r * cos(theta)
        y = center[1] + r * sin(theta)

        return Point(x, y)

    @staticmethod
    def point_on_circle(center: Union[Point, Iterable], radius: float, angle: float) -> Point:
        """

        :param center:
        :param radius:
        :param angle: The angle in radians
        :return:
        """

        x = round(center[0] + radius * cos(angle), 2)
        y = round(center[1] + radius * sin(angle), 2)
        return Point(x, y)

    @staticmethod
    def partition_list(input_list: List[Union[float, int]], n: int):
        """

        :param input_list:
        :param n:
        :return:
        """
        shuffle(input_list)
        return [input_list[i::n] for i in range(n)]

    @staticmethod
    def random_list_partitioning(input_list: List[Any]) -> List[Any]:
        pass

    @staticmethod
    def rotate_point_on_circle(a: Union[Point, Iterable], b: Union[Point, Iterable], angle) -> Point:
        pass

    @staticmethod
    def point_is_in_convex_polygon():
        pass

    @staticmethod
    def random_agent():
        pass
