"""
diceengine implements functionality for Fate dice and their arithmetic.
"""
import enum
import random


class Face(enum.IntEnum):
    """Face represents the faces of a Fate die."""

    BLANK = 0
    MINUS = -1
    PLUS = 1

    def __repr__(self):
        return self.name.lower()


class Die:
    sides = list(Face)

    def roll(self):
        return random.choice(self.sides)
