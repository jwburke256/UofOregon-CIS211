"""
CIS 211 Spring 2021 Week 7 Lab 7

Author: Jacob Burke

Credits: N/A

Created multiple functions to demonstrate passing functions as arguments
and using Lambda. Then created a dictionary to hold the aliases for the
function locations, and then a class to call necessary functions when
needed
"""

from typing import Callable, List
from math import sqrt


def total_sum(args: list[int]) -> int:
    total = 0
    for item in args:
        total += item
    return total


def apply(f: Callable, args: list[int]) -> list:
    new_list = []
    for item in args:
        new_list.append(f(item))
    return new_list


def square(args: list[int]) -> list:
    return apply(lambda x: x**2, args)


def magnitude(vector: List[int]) -> float:
    return sqrt(total_sum(square(vector)))


dispatch_table = {1: total_sum, 2: square, 3: magnitude}


class FunctionDispatcher:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def process_command(self, key: int, args: list[int]):
        f = self.dictionary[key]
        return f(args)


def main():
    fd = FunctionDispatcher(dispatch_table)
    print(fd.process_command(1, [3,4]))
    # 7
    print(fd.process_command(2, [3,4]))
    # [9, 16]
    print(fd.process_command(3, [3,4]))
    # 5.0


if __name__ == "__main__":
    main()
