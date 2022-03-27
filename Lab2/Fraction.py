"""
CIS 211 Spring 2021 Week 2 Lab 2

Author: Jacob Burke

Credits: N/A

Created a class fraction, and associated methods with that class in order
to demonstrate understanding of classes and methods.
"""


class Fraction:
    """An object that has both a numerator and a denominator, with each
    being integers"""

    def __init__(self, num: int, den: int) -> "Fraction":
        assert num >= 0 and den >= 0
        self.num = num
        self.den = den
        self.simplify()

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraction({repr(self.num)} / {repr(self.den)})"

    def __mul__(self, other) -> "Fraction":
        new_num = self.num * other.num
        new_den = self.den * other.den
        new_fraction = Fraction(new_num, new_den)
        new_fraction.simplify()
        return new_fraction

    def __add__(self, other):
        new_num = self.num * other.den + other.num + self.den
        new_den = self.den * other.den
        new_fraction = Fraction(new_num, new_den)
        new_fraction.simplify()
        return new_fraction

    def simplify(self):
        GCD = gcd(self.num, self.den)
        new_num = self.num // GCD
        new_den = self.den // GCD
        self.num = new_num
        self.den = new_den
        return None

def gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

if __name__ == "__main__":
    f1 = Fraction(4,8)
    print(f1)