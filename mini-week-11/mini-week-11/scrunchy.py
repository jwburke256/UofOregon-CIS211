"""
CIS 211 Spring 2021 Week 11 Mini Exam 5 scrunchy

Author: Jacob Burke

Credits: N/A

Scrunchy grids: Each row can be reduced to a single element,
in different ways.
"""

from typing import List

class Scrunchy:
    """Abstract base class.  Represents a kind of
    grid that can be scrunched so that each row is
    transformed to a single value, e.g., by summing
    or taking the product.
    """
    def __init__(self, values: List[List[int]]):
        self.values = values
        self.check_valid()

    def check_valid(self):
        """Must be a rectangular grid
        with at least one row and at least one column
        """
        assert len(self.values) > 0, "Must have at least one row"
        assert len(self.values[0]) > 0, "Must have at least one column"
        row_len = len(self.values[0])
        for row in self.values:
            assert len(row) == row_len, "Must be rectangular: All rows the same length"

    def __eq__(self, other: "Scrunchy") -> bool:
        # Same shape?
        if len(self.values) != len(other.values):
            return False
        if len(self.values[0]) != len(other.values[0]):
            return False
        # Same values in all elements?
        for row_i in range(len(self.values)):
            for col_i in range(len(self.values[0])):
                if self.values[row_i][col_i] != other.values[row_i][col_i]:
                    return False
        return True

    def scrunch_row(self, row: List[int]) -> int:
        """Use this abstract function to refactor scrunch"""
        raise NotImplementedError("Class {self.__class__.__name__} must implement row_scrunch")

    def scrunch(self):
        """Reduce each row to a single column"""
        for row_i in range(len(self.values)):
            self.values[row_i] = [ self.scrunch_row(row_i)]
        self.check_valid()


class ScrunchableBySum(Scrunchy):
    """We can scrunch rows down to their sum"""

    def scrunch_row(self, row: List[int]) -> int:
        return sum(self.values[row])


class ScrunchableByProduct(Scrunchy):
    """We can multiply the elements in a row"""
    def scrunch_row(self, row: List[int]) -> int:
        product = 1
        for el in self.values[row]:
            product *= el
        return product


class ScrunchableByMin(Scrunchy):
    """We can take minimum of each row"""
    def scrunch_row(self, row: List[int]) -> int:
        return min(self.values[row])


def main():
    """Smoke test"""
    g = ScrunchableBySum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    g.scrunch()
    assert g == ScrunchableBySum([[6], [15], [24]])
    # It's as scrunched as it gets
    g.scrunch()
    assert g == ScrunchableBySum([[6], [15], [24]])

    g = ScrunchableByMin([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    g.scrunch()
    assert g == ScrunchableBySum([[1], [4], [7]])
    # It's as scrunched as it gets
    g.scrunch()
    assert g == ScrunchableBySum([[1], [4], [7]])

    g = ScrunchableByProduct([[2, 3], [5, 2], [3, 8]])
    g.scrunch()
    assert g == ScrunchableBySum([[6], [10], [24]])

if __name__ == "__main__":
    main()







