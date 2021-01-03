"""
test_diceengine implements tests for everything related to the diceengine
module.
"""
import pytest

from fate.diceengine import Face


@pytest.fixture
def test_cases():
    cases = (("BLANK", 0), ("MINUS", -1), ("PLUS", 1))

    return cases


def test_face_values(subtests, test_cases):
    for face, value in test_cases:
        with subtests.test(msg=f"Test {face}"):
            assert getattr(Face, face) == value
