"""
test_diceengine implements tests for everything related to the diceengine
module.
"""
import pytest

from fate.diceengine import Die, Face


@pytest.fixture
def face_test_cases():
    cases = (("BLANK", 0), ("MINUS", -1), ("PLUS", 1))

    return cases


def test_face_repr(subtests, face_test_cases):
    for face, _ in face_test_cases:
        with subtests.test(msg=f"Test {face}"):
            f = getattr(Face, face)
            assert repr(f) == face.lower()


def test_face_values(subtests, face_test_cases):
    for face, value in face_test_cases:
        with subtests.test(msg=f"Test {face}"):
            assert getattr(Face, face) == value


def test_die_roll_returns_face():
    die = Die()
    assert type(die.roll()) == Face
