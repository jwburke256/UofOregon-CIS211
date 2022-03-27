"""
CIS 211 Spring 2021 Week 11 Mini Exam 5 grid

Author: Jacob Burke

Credits: N/A
Oh goody, another grid problem!
This one determines whether a grid contains
at least one column whose sum is positive.
"""

from typing import List

class Grid:
    """Represented as a list of lists of integers"""
    def __init__(self, values: List[List[int]]):
        # Assume the values are a rectangular array, i.e.,
        # every row is the same length.
        self.values = values

    def some_column_sum_positive(self) -> bool:
        """Returns True if and only if there is at least
        one column in this grid whose sum is a positive number.
        """
        if len(self.values) == 0:
            return False
        if self.values[0] is None:
            return False

        row_len = len(self.values[0])
        for i in range(row_len):
            sum_ctr = 0  # column sum counter
            for row in self.values:
                sum_ctr += row[i]
            if sum_ctr > 0:
                return True
        return False


def main():
    """Smoke test"""

    print("No columns, so there are no positive columns")
    g = Grid([])
    assert not g.some_column_sum_positive()
    g = Grid([[]])
    assert not g.some_column_sum_positive()

    print("Last column positive sum")
    g = Grid([[3, -2,  4],
              [-3, 2, -4],
              [0, -1,  2]])
    assert g.some_column_sum_positive()

    print("Here a *row* is positive but no column")
    g = Grid([[3, -2,  4],
              [-3, 2, -4],
              [0, -1,  -2]])
    assert not g.some_column_sum_positive()

    print("More rows than columns")
    g = Grid([[3, -2],
             [-3, 2],
             [-1, 0]])
    assert not g.some_column_sum_positive()

    print("More columns than rows")
    g = Grid([[3, -2,  5,  7],
              [-3, 2, -6, -6]])
    assert  g.some_column_sum_positive()

    print("OK")

if __name__ == "__main__":
    main()





