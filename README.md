# healthsciencecalculator

## Summary 

This package healthsciencecalculator.py is designed to provide tools for calculating and analyzing important health metrics. It aims to support health professionals, researchers, and fitness enthusiasts by offering reliable functions to convert relevant units, compute Total Daily Energy Expenditure (TDEE), Basal Metabolic Rate (BMR), and Body Mass Index (BMI).

## Functions 

get_tdee

    Description: Calculates Total Daily Energy Expenditure (TDEE) based on BMR and activity level.

    Inputs: Weight, height, age, sex, and activity level.

get_bmi

    Description: Calculates Body Mass Index (BMI) and provides category classification.

    Inputs: Weight and height.

get_bmr

    Description: Computes Basal Metabolic Rate (BMR) using the Harris-Benedict equation.

    Inputs: Weight, height, age, and sex.

convert_units

    Description: convert between various health-related units such as weight (kg to lbs), temperature (Celsius to Fahrenheit), and length (cm to inches). This function simplifies converting clinical data for international research or patient records.


## Python Ecosystem Fit

The healthsciencecalculator.py package fits well within the broader Python ecosystem, complementing existing data science and health analysis libraries. There are several Python packages with similar functionalities, such as: 

[`health-indicator](https://pypi.org/project/health-indicator/)
    This package collects health indices like BMI and health indicators like birth rate

[`health-records 0.0.7`]https://pypi.org/project/health-records/)
    This package maintains personal health records in a text file that can be privately stored in your computer.

The healthsciencecalculator.py package is unique in that it performs health-related calculations with high accuracy and precision, tailored specifically for healthcare professionals and data analysts.

## Installation

```bash
$ pip install healthsciencecalculator
```

## Usage

After installation, you can start using the various functions provided by the package. 


The **get_bmi** function calculates the Body Mass Index (BMI) and provides detailed classification information, including the BMI category and associated health risk level.

```
from healthsciencecalculator.healthsciencecalculator import get_bmi  

# Example usage
weight = 70.0  # Weight in kilograms
height = 1.75  # Height in meters

# Calculate BMI
bmi_result = get_bmi(weight, height)

# Access BMI details
print(f"BMI: {bmi_result.bmi:.2f}")
print(f"Category: {bmi_result.category}")
print(f"Risk Level: {bmi_result.risk_level}")
```

The **get_tdee** function calculates the Total Daily Energy Expenditure (TDEE) based on the Basal Metabolic Rate (BMR) and an individual's activity level.

```
from healthsciencecalculator.healthsciencecalculator import get_tdee  

# Example usage
bmr = 1500.0  # Basal Metabolic Rate in kilocalories
activity_level = 'moderately active'  # Choose from: 'sedentary', 'lightly active', 'moderately active', 'very active', 'extra active'

# Calculate TDEE
tdee = get_tdee(bmr, activity_level)

# Display TDEE
print(f"TDEE: {tdee:.2f} kcal/day")

```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`healthsciencecalculator` was created by Forgive Agbesi, Jiayi Li, Hala Arar, Tengwei Wang. It is licensed under the terms of the MIT license.

## Credits

`healthsciencecalculator` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contributors

Forgive Agbesi
Hala Arar
Jiayi Li
Tengwei Wang
