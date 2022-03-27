"""Snail graphics are slower and simpler than turtle graphics, but
they have one nice feature:  A sequence of snail graphics commands
can be encoded as hexadecimal numbers, a format we call
"snail language you might enjoy", or "slyme".
"""

import slate
from slate import Slate
from typing import List
from slate import Dir

# slime format 8-bit encoding:
# bit 7:  0 = move, 1 = draw
# bits 4..6: index of direction vector
# bits 0..3: distance, 0..15 steps


def inked(cmd: int) -> bool:
    """Extract the inked/uninked bit from integer command"""
    bit = 0
    mask = 128
    inked_bit = cmd & mask
    if inked_bit == 128:
        bit = 1
    return bool(bit)


def direction(cmd: int) -> slate.Dir:
    """Extract the direction indicator from integer command"""
    dir_bits = 0
    mask = 112
    dir_bits = cmd & mask
    dir_bits = dir_bits >> 4
    return slate.Dir(dir_bits)


def dist(cmd: int) -> int:
    """Extract the distance (number of steps) from integer command"""
    dist_bits = 0
    mask = 15
    dist_bits = cmd & mask
    return dist_bits


class Snail:
    """Snails can interpret Slyme code to draw character graphic on a slate"""
    def __init__(self):
        self.slate = Slate()

    def interpret(self, commands: List[str]):
        """Each string in 'commands' is two hexadecimal digits"""
        for command in commands:
            cmd_int = int(command, base=16)
            vec = direction(cmd_int)
            steps = dist(cmd_int)
            self.slate.stroke(vec, steps, inked(cmd_int))


def example():
    # Ring
    snail = Snail()
    commands = slate.ox_example()
    print(commands)
    snail.interpret(commands)
    print(snail.slate)
    print()
    # Z
    snail = Snail()
    commands = slate.z_example()
    print(commands)
    snail.interpret(commands)
    print(snail.slate)
    print()
    # S
    snail = Snail()
    commands = slate.s_example()
    print(commands)
    snail.interpret(commands)
    print(snail.slate)
    print()
    # concentric
    snail = Snail()
    commands = slate.concentric_example()
    print(commands)
    snail.interpret(commands)
    print(snail.slate)
    print()


def main():
    example()


if __name__ == "__main__":
    main()
