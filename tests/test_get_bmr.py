import pytest # type: ignore
from healthsciencecalculator.healthsciencecalculator import get_bmr


# Test cases
def test_bmr_male_calculation():
    # Normal values
    expected = 1668.8720
    actual = get_bmr(70, 175, 25, "male")
    assert actual == pytest.approx(expected, 0.0001)

    # Decimal values
    expected = 1674.6482
    actual = get_bmr(70.32, 175.12, 25, "male")
    assert actual == pytest.approx(expected, 0.0001)

    # Edge case: High weight and height
    expected = 2525.4218
    actual = get_bmr(120, 200, 30, "male")
    assert actual == pytest.approx(expected, 0.0001)

    # Edge case: Very young age
    expected = 1853.122
    actual = get_bmr(70, 175, 5, "male")
    assert actual == pytest.approx(expected, 0.0001)


def test_bmr_female_calculation():
    # Normal values
    expected = 1392.2470
    actual = get_bmr(60, 165, 30, "female")
    assert actual == pytest.approx(expected, 0.0001)

    # Decimal values
    expected = 1398.2124
    actual = get_bmr(60.2, 165.1, 30, "female")
    assert actual == pytest.approx(expected, 0.0001)

    # Edge case: Low weight and height
    expected = 1056.3530
    actual = get_bmr(40, 140, 20, "female")
    assert actual == pytest.approx(expected, 0.0001)

    # Edge case: Very old age
    expected = 1226.4020
    actual = get_bmr(50, 160, 90, "female")
    assert actual == pytest.approx(expected, 0.0001)


def test_bmr_case_insensitivity():
    # Case insensitivity for "male"
    expected = 1668.8720
    actual = get_bmr(70, 175, 25, "Male")
    assert actual == pytest.approx(expected, 0.0001)

    actual = get_bmr(70, 175, 25, "MALE")
    assert actual == pytest.approx(expected, 0.0001)

    # Case insensitivity for "female"
    expected = 1392.2470
    actual = get_bmr(60, 165, 30, "Female")
    assert actual == pytest.approx(expected, 0.0001)

    actual = get_bmr(60, 165, 30, "FEMALE")
    assert actual == pytest.approx(expected, 0.0001)


def test_bmr_invalid_inputs():
    # Negative weight
    with pytest.raises(ValueError):
        get_bmr(-70, 175, 25, "male")

    # Negative height
    with pytest.raises(ValueError):
        get_bmr(70, -175, 25, "male")

    # Negative age
    with pytest.raises(ValueError):
        get_bmr(70, 175, -25, "male")

    # Invalid sex
    with pytest.raises(ValueError):
        get_bmr(70, 175, 25, "other")


def test_bmr_zero_inputs():
    # Zero weight
    expected = 88.362
    actual = get_bmr(0, 175, 25, "male")
    assert actual == pytest.approx(expected, 0.0001)

    # Zero height
    expected = 285.387
    actual = get_bmr(70, 0, 25, "male")
    assert actual == pytest.approx(expected, 0.0001)

    # Zero age
    expected = 2008.237
    actual = get_bmr(70, 175, 0, "male")
    assert actual == pytest.approx(expected, 0.0001)
