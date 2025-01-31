import pytest
# import sys
# sys.path.append("../src/healthsciencecalculator")
from healthsciencecalculator.get_bmi import get_bmi
import math

def test_bmi_categories():
    """Test all BMI categories with representative values."""
    test_cases = [
        (50, 1.75, 16.3, "underweight"),
        (70, 1.75, 22.9, "healthy"),
        (85, 1.75, 27.8, "overweight"),
        (100, 1.75, 32.7, "class 1 obesity"),
        (115, 1.75, 37.6, "class 2 obesity"),
        (130, 1.75, 42.4, "class 3 obesity"),
    ]
    
    for weight, height, expected_bmi, expected_category in test_cases:
        result = get_bmi(weight=weight, height=height)
        print(result)
        assert math.isclose(result.bmi, expected_bmi, rel_tol = 0.01)
        assert result.category == expected_category

def test_bmi_edge_cases():
    """Test boundary values between BMI categories."""
    test_cases = [
        (56.6, 1.75, 18.5, "healthy"),      # BMI = 18.5
        (76.6, 1.75, 25.0, "overweight"),   # BMI = 25
    ]
    
    for weight, height, expected_bmi, expected_category in test_cases:
        result = get_bmi(weight=weight, height=height)
        assert math.isclose(result.bmi, expected_bmi, rel_tol=0.01)
        assert result.category == expected_category

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
    assert result.bmi > 0
    
    # Test very large valid values
    result = get_bmi(weight=500, height=2.5)
    assert result.bmi > 0
    
    # Test integer inputs
    result = get_bmi(weight=70, height=2)
    assert isinstance(result.bmi, float)
