"""
CIS 211 Spring 2021 Week 3 Lab 3

Author: Jacob Burke

Credits: N/A

Created shape classes and demonstrated the concept of inheritance.
"""
from math import pi


class Shape3D:

    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated")

    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def area(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def print_info(self):
        return print(f"Area:{self.area()} Volume: {self.volume()}")


class Cylinder(Shape3D):
    def __init__(self, radius: float, height: float) -> "Cylinder":
        self.radius = radius
        self.height = height
        self.vol = pi * (self.radius ** 2) * self.height
        self.sa = 2 * pi * (self.radius ** 2) + 2 * pi * self.radius * self.height

    def volume(self) -> float:
        return self.vol

    def area(self) -> float:
        return self.sa


class Cuboid(Shape3D):
    def __init__(self, width: float, length: float, height: float) -> "Cuboid":
        self.width = width
        self.length = length
        self.height = height
        self.vol = self.width * self.length * self.height
        self.sa = 2 * self.width * self.length + 2 * self.width * self.height + 2 * self.length * self.height

    def volume(self) -> float:
        return self.vol

    def area(self) -> float:
        return self.sa

class Cube(Cuboid):
    def __init__(self, width: float):
        super().__init__(width, width, width)


if __name__ == "__main__":
    cyl = Cylinder(3, 5)
    cuboid = Cuboid(6, 4, 9)
    lst = [Cube(3), cyl, cuboid]
    for shape in lst:
        shape.print_info()

