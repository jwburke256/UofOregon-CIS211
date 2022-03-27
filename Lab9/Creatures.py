"""
CIS 211 Spring 2021 Week 9 Lab 9

Author: Jacob Burke

Credits: N/A

Created an abstract class and 3 concrete classes in order to demonstrate
use of recursion.
"""


class Creature(object):

    def __init__(self):
        raise NotImplementedError("Abstract classes should not be instanciated")

    def __str__(self) -> str:
        raise NotImplementedError("Abstract class methods should not be called")

    def search(self, name: str) -> bool:
        raise NotImplementedError("Abstract class methods should not be called")


class Orthrus(Creature):

    def __init__(self, left: Creature, right: Creature):
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.left} {self.right}"

    def search(self, name: str) -> bool:
        return self.left.search(name) or self.right.search(name)


class Cerberus(Creature):

    def __init__(self, left: Creature, middle: Creature, right: Creature):
        self.left = left
        self.middle = middle
        self.right = right

    def __str__(self) -> str:
        return f"{self.left} {self.middle} {self.right}"

    def search(self, name: str) -> bool:
        return self.left.search(name) or self.middle.search(name) or self.right.search(name)


class Head(Creature):

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def search(self, name: str) -> bool:
        if name == self.__str__():
            return True
        else:
            return False


def main():
    doggy1 = Head("Kane")
    doggy2 = Head("Wolfie")
    doggy3 = Head("Rugal")
    doggy4 = Head("Taker")
    ort1 = Orthrus(doggy1, doggy2)
    ort2 = Orthrus(doggy3, Head("Jeff"))
    cer = Cerberus(ort1, doggy4, ort2)
    print(cer)
    print(cer.search("Drogon"))
    print(cer.search("Rugal"))


if __name__ == "__main__":
    main()