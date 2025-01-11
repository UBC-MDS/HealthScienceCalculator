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



