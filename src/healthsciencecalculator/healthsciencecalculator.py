from dataclasses import dataclass


@dataclass
class BMIResult:
    bmi: float
    category: str
    risk_level: str


def get_bmi(
    weight: float,
    height: float,
) -> BMIResult:
    """Calculate Body Mass Index (BMI) and return detailed classification information.

    BMI is calculated as weight (kg) divided by height (m) squared.

    Parameters
    ----------
    weight : float
        Weight in kilograms
    height : float
        Height in meters

    Returns
    -------
    BMIResult
        A dataclass containing:
        - bmi (float): The calculated BMI value
        - category (str): BMI category, one of:
            - 'underweight' (BMI < 18.5)
            - 'healthy' (BMI 18.5-24.9)
            - 'overweight' (BMI 25-29.9)
            - 'class 1 obesity' (BMI 30-34.9)
            - 'class 2 obesity' (BMI 35-39.9)
            - 'class 3 obesity' (BMI >= 40)
        - risk_level (str): Associated health risk level
    """
    return

def unit_convert(value: float, input_unit: str, ouput_unit: str):
    """Converts values from one unit to another.

    Supported measurement units:
    - Weight: kg, g, lb, stone
    - Length: m, cm, feet, inch
    - Temperature: C, F, K
    - Concentration: mg/dL, mmol/L
    - Volume: L, mL

    Parameters
    ----------
    value : float
        The numeric value to be converted.

    input_unit : str
        The unit of input value.

    output_unit : str
        The desired unit of output value.
    

    Returns
    -------
    float
        The output value in desired unit.

    Examples
    --------
    >>> unit_convert(1, "m", "cm")
    100
    """
    
