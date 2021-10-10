from point import Point
from math import pi
from arc import Arc
from typing import List


class Circle(object):
    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle(center={self.center},radius={self.radius})"

    @property
    def area(self):
        return pi * self.radius ** 2

    @property
    def circumference(self):
        return 2 * pi * self.radius


class BasePartitionedCircle(Circle):
    def __init__(self, center: Point, radius: float, partitions: int) -> None:
        super().__init__(center, radius)
        self.number_of_partitions = partitions

    def __repr__(self) -> str:
        return (
            f"BasePartitionedCircle(center={self.center},radius={self.radius},partitions={self.number_of_partitions})"
        )

    def random_partition_circle(self) -> List[Arc]:
        raise NotImplementedError("random_partition_circle is not implemented")


class TrianglePartitionedCircle(BasePartitionedCircle):
    def __init__(self, center: Point, radius: float, partitions: int) -> None:
        super().__init__(center, radius)
        self.number_of_partitions = partitions

    def __repr__(self) -> str:
        return f"TrianglePartitionedCircle(center={self.center},radius={self.radius},partitions={self.number_of_partitions})"

    def random_partition_circle(self) -> List[Arc]:
        pass


class ArcPartitionedCircle(Circle):
    def __init__(self, center: Point, radius: float, partitions: int) -> None:
        super().__init__(center, radius)
        self.number_of_partitions = partitions

    def __repr__(self) -> str:
        return f"ArcPartitionedCircle(center={self.center},radius={self.radius},partitions={self.number_of_partitions})"

    def random_partition_circle(self) -> List[Arc]:
        pass
