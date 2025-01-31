import pytest
from healthsciencecalculator.get_tdee import get_tdee

def test_get_tdee_sedentary():
    """
    Test get_tdee with a typical BMR and 'sedentary' activity level.
    Expect the function to return bmr * 1.2 (as an example).
    """
    # Example BMR
    test_bmr = 1500.0
    activity_level = 'sedentary'
    expected_tdee = test_bmr * 1.2
    result = get_tdee(test_bmr, activity_level)
    assert abs(result - expected_tdee) < 1e-6  # Within floating point tolerance

def test_get_tdee_moderately_active():
    """
    Test get_tdee with 'moderately active' activity level.
    Expect the function to return bmr * some known factor.
    """
    test_bmr = 1600.0
    activity_level = 'moderately active'
    # Suppose the multiplier for 'moderately active' is 1.55
    expected_tdee = test_bmr * 1.55
    result = get_tdee(test_bmr, activity_level)
    assert abs(result - expected_tdee) < 1e-6

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
        get_tdee(test_bmr, 'extremely active')  # not in the allowed list
