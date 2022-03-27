"""Tests for grid.py"""
from grid import *
import unittest


class TestGrid(unittest.TestCase):

    def test_no_row(self):
        """No rows, so there are no positive columns"""
        g = Grid([])
        self.assertFalse(g.some_column_sum_positive())

    def test_no_col(self):
        """No columns, so there are no positive columns"""
        g = Grid([[]])
        self.assertFalse(g.some_column_sum_positive())

    def test_last_col_positive(self):
        """The last column has a positive sum"""
        g = Grid([[3, -2, 4],
                  [-3, 2, -4],
                  [0, -1, 2]])
        self.assertTrue(g.some_column_sum_positive())

    def test_pos_row_but_not_col(self):
        """There is a positive sum row in this example,
        but no positive sum column.
        """
        g = Grid([[3, -2, 4],
                  [-3, 2, -4],
                  [0, -1, -2]])
        self.assertFalse(g.some_column_sum_positive())

    def test_more_rows(self):
        """This grid has more rows than columns
        (don't assume square matrices)
        """
        g = Grid([[3, -2],
                  [-3, 2],
                  [-1, 0]])
        self.assertFalse(g.some_column_sum_positive())

    def test_more_cols(self):
        """This grid has more columns than rows
        (don't assume square matrices)
        """
        g = Grid([[3, -2, 5, 7],
                  [-3, 2, -6, -6]])
        self.assertTrue(g.some_column_sum_positive())


if __name__ == "__main__":
    unittest.main()
