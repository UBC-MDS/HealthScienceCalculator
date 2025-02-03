import pytest
# import sys
# sys.path.append("../src/healthsciencecalculator")
from healthsciencecalculator.get_bmi import get_bmi
import math

@pytest.mark.parametrize(
    "weight, height, expected_bmi, expected_category",
    [
        (50, 1.75, 16.3, "underweight"),
        (70, 1.75, 22.9, "healthy"),
        (85, 1.75, 27.8, "overweight"),
        (100, 1.75, 32.7, "class 1 obesity"),
        (115, 1.75, 37.6, "class 2 obesity"),
        (130, 1.75, 42.4, "class 3 obesity"),
    ]
)
def test_bmi_categories(weight, height, expected_bmi, expected_category):
    """Test all BMI categories with representative values."""
    result = get_bmi(weight=weight, height=height)
    assert math.isclose(result.bmi, expected_bmi, rel_tol=0.01), f"Expected BMI {expected_bmi}, got {result.bmi}"
    assert result.category == expected_category, f"Expected category '{expected_category}', got '{result.category}'"

@pytest.mark.parametrize(
    "weight, height, expected_bmi, expected_category",
    [
        (56.6, 1.75, 18.5, "healthy"),      # BMI = 18.5
        (76.6, 1.75, 25.0, "overweight"),   # BMI = 25
    ]
)
def test_bmi_edge_cases(weight, height, expected_bmi, expected_category):
    """Test boundary values between BMI categories."""
    result = get_bmi(weight=weight, height=height)
    assert math.isclose(result.bmi, expected_bmi, rel_tol=0.01), f"Expected BMI {expected_bmi}, got {result.bmi}"
    assert result.category == expected_category, f"Expected category '{expected_category}', got '{result.category}'"

def test_input_validation():
    """Test error handling for invalid inputs."""
    # Test invalid types
    with pytest.raises(TypeError, match="Weight and height must be numbers"):
        get_bmi(weight="70", height=1.75)
    
    with pytest.raises(TypeError, match="Weight and height must be numbers"):
        get_bmi(weight=70, height="1.75")
    
    with pytest.raises(TypeError, match="Weight and height must be numbers"):
        get_bmi(weight=None, height=1.75)
    
    with pytest.raises(TypeError, match="Weight and height must be numbers"):
        get_bmi(weight=70, height=None)
    
    # Test negative values
    with pytest.raises(ValueError, match="Weight must be positive"):
        get_bmi(weight=-70, height=1.75)
    
    with pytest.raises(ValueError, match="Height must be positive"):
        get_bmi(weight=70, height=-1.75)
    
    # Test zero values
    with pytest.raises(ValueError, match="Weight must be positive"):
        get_bmi(weight=0, height=1.75)
    
    with pytest.raises(ValueError, match="Height must be positive"):
        get_bmi(weight=70, height=0)

def test_valid_edge_inputs():
    """Test edge cases with valid inputs."""
    # Test very small valid values
    result = get_bmi(weight=0.1, height=0.1)
    assert result.bmi > 0, f"Expected BMI to be > 0, got {result.bmi}"
    
    # Test very large valid values
    result = get_bmi(weight=500, height=2.5)
    assert result.bmi > 0, f"Expected BMI to be > 0, got {result.bmi}"
    
    # Test integer inputs
    result = get_bmi(weight=70, height=2)
    assert isinstance(result.bmi, float), f"Expected result.bmi to be float, got {type(result.bmi)}"