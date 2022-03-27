"""
CIS 211 Spring 2021 Week 6 Lab 6

Author: Jacob Burke

Credits: N/A
Created a set of classes that create clubs and accompanying times that do
not conflict based on student schedules. Demonstrates looping through
sets and being cognizant of aliasing.
"""


class BinaryNumber:
    def __init__(self, bits: list[int]):
        self.bits = bits

    def __or__(self, other) -> "BinaryNumber":
        """Compares bits between two binary numbers and overwrites
                each bit depending on if the compared bits have the 1
                in either index"""
        assert len(self.bits) == len(other.bits)
        result = []
        for i in range(len(self.bits)):
            if self.bits[i] == 0 and other.bits[i] == 0:
                result.append(0)
            else:
                result.append(1)
        return BinaryNumber(result)

    def __and__(self, other) -> "BinaryNumber":
        """Compares bits between two binary numbers and overwrites
        each bit depending on if the compared bits have the 1
        in each index"""
        assert len(self.bits) == len(other.bits)
        result = []
        for i in range(len(self.bits)):
            if self.bits[i] == 1 and other.bits[i] == 1:
                result.append(1)
            else:
                result.append(0)
        return BinaryNumber(result)

    def left_shift(self):
        """Shifts the bits to the left by 1, with bits leaving
        the index # being discarded"""
        result = []
        for i in range(1, len(self.bits)):
            self.bits[i -1] = self.bits[i]
        self.bits[len(self.bits)-1] = 0

    def right_shift(self):
        """Shifts the bits to the right by 1, with bits leaving
        the index # being discarded"""
        index_size = len(self.bits) - 1
        for i in range(len(self.bits)-1):
            self.bits[index_size - i] = self.bits[index_size - i - 1]
        self.bits[0] = 0

    def extract(self, start: int, end: int) -> "BinaryNumber":
        """Returns a BinaryNumber that only contains the bits found in the given
        one based on the given starting and ending index arguments"""
        num_shift = end - start
        copy_bits = BinaryNumber(self.bits.copy())
        bit_size = len(self.bits)
        mask = []
        for i in range(len(self.bits)):
            mask.append(0)
        for i in range((bit_size - end - 1), (bit_size - start)):
            mask[i] = 1
        mask = BinaryNumber(mask)
        copy_bits = copy_bits.__and__(mask)
        for i in range(num_shift):
            copy_bits.right_shift()
        return copy_bits

    def __str__(self):
        """Returns list of bits"""
        return f"{self.bits}"








