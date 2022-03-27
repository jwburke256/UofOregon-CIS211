"""Test cases for snail graphics"""

import unittest
from snail import *


def trim_all(s: str) -> str:
    """Trim all lines in a multi-line string, to
    compare while ignoring indentation.
    """
    parts = s.strip().split("\n")
    trimmed_parts = [s.strip() for s in parts]
    return "\n".join(trimmed_parts)


class TestExample(unittest.TestCase):
    def test_example_ox(self):
        """The O-X combination encoded in hexadecimal"""
        expected = trim_all("""
        #  #  #  #  #  #  #  # 
        #  #  -  -  -  -  #  # 
        #  -  #  -  -  #  -  # 
        #  -  -  #  #  -  -  # 
        #  -  -  #  #  -  -  # 
        #  -  #  -  -  #  -  # 
        #  #  -  -  -  -  #  # 
        #  #  #  #  #  #  #  # 
        """)
        commands = ['B7', 'D7', 'F7', '97', 'C7', 'F7', 'A7', '90']
        snail = Snail()
        snail.interpret(commands)
        produced = trim_all(str(snail.slate))
        self.assertEqual(expected, produced)

    def test_example_s(self):
        expected = trim_all("""
        #  #  #  #  #  #  #  # 
        #  -  -  -  -  -  -  - 
        #  -  -  -  -  -  -  - 
        #  #  #  #  #  #  #  # 
        -  -  -  -  -  -  -  # 
        -  -  -  -  -  -  -  # 
        -  -  -  -  -  -  -  # 
        #  #  #  #  #  #  #  # 
        """)
        commands = ['B7', 'F7', 'D3', 'B7', 'D4', 'F8']
        snail = Snail()
        snail.interpret(commands)
        produced = trim_all(str(snail.slate))
        self.assertEqual(expected, produced)

    def test_example_z(self):
        expected = trim_all("""
        #  #  #  #  #  #  #  # 
        -  -  -  -  -  -  #  - 
        -  -  -  -  -  #  -  - 
        -  -  -  -  #  -  -  - 
        -  -  -  #  -  -  -  - 
        -  -  #  -  -  -  -  - 
        -  #  -  -  -  -  -  - 
        #  #  #  #  #  #  #  # 
        """)
        commands = ['B7', 'E7', 'B8']
        snail = Snail()
        snail.interpret(commands)
        produced = trim_all(str(snail.slate))
        self.assertEqual(expected, produced)

    def test_example_o_o(self):
        expected = trim_all("""
        #  #  #  #  #  #  #  # 
        #  -  -  -  -  -  -  # 
        #  -  #  #  #  #  #  # 
        #  -  #  -  -  -  #  # 
        #  -  #  -  -  -  #  # 
        #  -  #  -  -  -  #  # 
        #  -  #  #  #  #  #  # 
        #  #  #  #  #  #  #  # 
        """)
        commands = ['B7', 'D7', 'F7', '97', '42', 'B4', 'D4', 'F4', '94']
        snail = Snail()
        snail.interpret(commands)
        produced = trim_all(str(snail.slate))
        self.assertEqual(expected, produced)


if __name__ == "__main__":
    unittest.main()
