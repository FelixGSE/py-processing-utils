from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def __repr__(self) -> str:
        return f"Point({self.x},{self.y})"

    def __getitem__(self, key: int) -> float:
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise ValueError("Index out of range")
