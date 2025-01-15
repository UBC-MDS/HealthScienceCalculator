# read version from installed package
from importlib.metadata import version
from healthsciencecalculator.healthsciencecalculator import get_bmi

__version__ = version("healthsciencecalculator")

__all__ = ['get_bmi']