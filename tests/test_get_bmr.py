import pytest # type: ignore
from healthsciencecalculator.healthsciencecalculator import get_bmr


# Test cases
def test_bmr_male_calculation():
    """ Test case to test the BMR calculation of a male"""
    # Normal values
    expected = 1724.052
    actual = get_bmr(70, 175, 25, "male")
    assert actual == pytest.approx(expected, 0.0001)

    # Decimal values
    expected = 1728.9149
    actual = get_bmr(70.32, 175.12, 25, "male")
    assert actual == pytest.approx(expected, 0.0001)

    # Edge case: High weight and height
    expected = 2485.492
    actual = get_bmr(120, 200, 30, "male")
    assert actual == pytest.approx(expected, 0.0001)

    # Edge case: Very young age
    expected = 1837.592
    actual = get_bmr(70, 175, 5, "male")
    assert actual == pytest.approx(expected, 0.0001)


def test_bmr_female_calculation():
    """ Test case to test the BMR calculation of a female"""
    # Normal values
    expected = 1383.683
    actual = get_bmr(60, 165, 30, "female")
    assert actual == pytest.approx(expected, 0.0001)

    # Decimal values
    expected = 1385.8422
    actual = get_bmr(60.2, 165.1, 30, "female")
    assert actual == pytest.approx(expected, 0.0001)

    # Edge case: Low weight and height
    expected = 1164.593
    actual = get_bmr(40, 140, 20, "female")
    assert actual == pytest.approx(expected, 0.0001)

    # Edge case: Very old age
    expected = 1015.923
    actual = get_bmr(50, 160, 90, "female")
    assert actual == pytest.approx(expected, 0.0001)


def test_bmr_case_insensitivity():
    """ Test case to test the input for sex case sensitivity"""
    # Case insensitivity for "male"
    expected = 1724.052
    actual = get_bmr(70, 175, 25, "Male")
    assert actual == pytest.approx(expected, 0.0001)

    actual = get_bmr(70, 175, 25, "MALE")
    assert actual == pytest.approx(expected, 0.0001)

    # Case insensitivity for "female"
    expected = 1383.683
    actual = get_bmr(60, 165, 30, "Female")
    assert actual == pytest.approx(expected, 0.0001)

    actual = get_bmr(60, 165, 30, "FEMALE")
    assert actual == pytest.approx(expected, 0.0001)


def test_bmr_invalid_inputs():
    """ Test case to test the invalid inputs"""
    # Negative weight
    with pytest.raises(ValueError):
        get_bmr(-70, 175, 25, "male")

    # Decimal age
    with pytest.raises(ValueError):
        get_bmr(70, 175, 25.2, "male")

    # Negative height
    with pytest.raises(ValueError):
        get_bmr(70, -175, 25, "male")

    # Negative age
    with pytest.raises(ValueError):
        get_bmr(70, 175, -25, "male")

    # Invalid sex
    with pytest.raises(ValueError):
        get_bmr(70, 175, 25, "other")

    with pytest.raises(ValueError, match="Weight must be positive"):
        get_bmr(0, 175, 25, "male")

def test_bmr_edge_cases():
    """Test case for edge cases in the BMR calculation"""
    # Extremely low values
    expected = 100.881  # Male: Near-zero inputs
    actual = get_bmr(1, 1, 1, "male")
    assert actual == pytest.approx(expected, 0.0001)

    expected = 455.608  # Female: Near-zero inputs
    actual = get_bmr(1, 1, 1, "female")
    assert actual == pytest.approx(expected, 0.0001)

    # Extremely high values
    expected = 4739.512 # Male: Large values
    actual = get_bmr(300, 250, 100, "male")
    assert actual == pytest.approx(expected, 0.0001)

    expected = 3563.193  # Female: Large values
    actual = get_bmr(300, 250, 100, "female")
    assert actual == pytest.approx(expected, 0.0001)

