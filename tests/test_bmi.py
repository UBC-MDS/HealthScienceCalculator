import pytest
from healthsciencecalculator.healthsciencecalculator import get_bmi
import math


class TestBMICalculator:
    """Tests for the BMI calculator functionality."""
    
    def test_bmi_categories(self):
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

    def test_bmi_edge_cases(self):
        """Test boundary values between BMI categories."""
        test_cases = [
            (56.6, 1.75, 18.5, "healthy"),      # BMI = 18.5
            (76.6, 1.75, 25.0, "overweight"),   # BMI = 25
        ]
        
        for weight, height, expected_bmi, expected_category in test_cases:
            result = get_bmi(weight=weight, height=height)
            assert math.isclose(result.bmi, expected_bmi, rel_tol=0.01)
            assert result.category == expected_category

    def test_input_validation(self):
        """Test error handling for invalid inputs."""
        with pytest.raises(ZeroDivisionError):
            get_bmi(weight=70, height=0)
        
        with pytest.raises(TypeError):
            get_bmi(weight="70", height=1.75)
        
        with pytest.raises(TypeError):
            get_bmi(weight=70, height="1.75")
