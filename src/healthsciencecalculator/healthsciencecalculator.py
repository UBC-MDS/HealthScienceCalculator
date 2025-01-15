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


def unit_convert(value: float, input_unit: str, output_unit: str):
    """Converts values from one unit to another.

    Supported measurement units:
    - Weight: kg, g, lb, stone
    - Length: m, cm, feet, inch
    - Temperature: C, F
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
    
    category = {
        "kg":0,"g":0,"lb":0,"stone":0,
        "m":1,"cm":1,"feet":1,"inch":1,
        "C":2,"F":2,
        "mg/dL":3,"mmol/L":3,
        "L":4,"mL":4
        }
    cal = {
        "kg":1000.0,"g":1.0,"lb":453.59237,"stone":6350.29318,
        "m":100.0,"cm":1.0,"feet":30.48,"inch":2.54,
        "mg/dL":1.0,"mmol/L":18.0,
        "L":1000.0,"mL":1.0
    }

    # validate input
    if (not isinstance(value, float)) & (not isinstance(value, int)):
        raise TypeError("Value must be a number")
    if not isinstance(input_unit, str):
        raise TypeError("Input unit must be string")
    if not isinstance(output_unit, str):
        raise TypeError("output unit must be string")

    # validate category
    if not input_unit in category:
        raise ValueError("Input unit does not exist")
    if not output_unit in category:
        raise ValueError("Output unit does not exist")
    if category[input_unit] != category[output_unit]:
        raise ValueError("Input unit and output unit do not in the same category")

    # convert temperature
    if input_unit == "C":
        return round(value * 1.8 + 32, 2)
    if input_unit == "F":
        return round((value - 32) / 1.8, 2)

    # convert others
    return round(value * cal[input_unit] / cal[output_unit], 2)
        
    

def get_bmr(
        weight: float,
        height:float,
        age:int,
        sex:str
) -> float:
    """
    Computes Basal Metabolic Rate (BMR) using the Harris-Benedict equation.

    The BMR is an estimate of the number of calories your body needs to perform
    basic life-sustaining functions, such as breathing, circulation, and cell production.

    Parameters
    ----------
    weight : float
        Weight of the individual in kilograms.
    height : float
        Height of the individual in centimeters.
    age : int
        Age of the individual in years.
    sex : str
        Biological sex of the individual. Accepted values are "male" or "female".

    Returns
    -------
    float
        The estimated BMR value in calories per day.

    Notes
    -----
    The Harris-Benedict equation is used to calculate BMR:
    - For males: BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    - For females: BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    Examples
    --------
    >>> get_bmr(70, 175, 25, "male")
    1668.872
    >>> get_bmr(60, 165, 30, "female")
    1392.247
    """

def get_tdee(
    bmr: float, 
    activity_level: str
) -> float:
    """
    Calculate the Total Daily Energy Expenditure (TDEE) based on BMR and activity level.

    Parameters:
    - bmr (float): The Basal Metabolic Rate calculated using `calculate_bmr`.
    - activity_level (str): The activity level of the individual. Options are:
        'sedentary', 'lightly active', 'moderately active', 'very active', 'extra active'.

    Returns:
    - float: The calculated TDEE value in kilocalories per day.

    Example:
    --------
    >>> bmr = 1500.0  # Basal Metabolic Rate in kilocalories
    >>> activity_level = 'moderately active'
    >>> tdee = get_tdee(bmr, activity_level)
    >>> print(f"TDEE: {tdee:.2f} kcal/day")
    TDEE: 2310.00 kcal/day  # Example output, actual value depends on implementation
    """
    pass