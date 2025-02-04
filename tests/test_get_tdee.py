import pytest
from healthsciencecalculator.get_tdee import get_tdee


@pytest.mark.parametrize(
    "test_bmr, activity_level, expected_multiplier",
    [
        (1500.0, 'sedentary', 1.2),
        (1600.0, 'moderately active', 1.55),
    ]
)
def test_get_tdee(test_bmr, activity_level, expected_multiplier):
    """
    Test get_tdee with various activity levels.
    The function should return bmr * expected_multiplier for the given activity level.
    """
    expected_tdee = test_bmr * expected_multiplier
    result = get_tdee(test_bmr, activity_level)
    assert abs(result - expected_tdee) < 1e-6, f"Expected TDEE {expected_tdee}, got {result}"

def test_get_tdee_invalid_bmr():
    """
    Test that get_tdee raises ValueError if bmr <= 0.
    """
    with pytest.raises(ValueError):
        get_tdee(-100, 'sedentary')

def test_get_tdee_invalid_activity_level():
    """
    Test that get_tdee raises ValueError if the activity level is invalid.
    """
    test_bmr = 1500.0
    with pytest.raises(ValueError):
        get_tdee(test_bmr, 'extremely active') # not in the allowed list