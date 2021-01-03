"""
diceengine implements functionality for Fate dice and their arithmetic.
"""
import enum


class Face(enum.IntEnum):
    """Face represents the faces of a Fate die."""

    BLANK = 0
    MINUS = -1
    PLUS = 1
