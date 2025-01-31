import pytest
from healthsciencecalculator.unit_convert import unit_convert

# Test case 1: wrong input type

def test_valid_input():
    """
    Test whether unit_convert raises TypeError 
    when wrong datatypes are input
    """
    
    with pytest.raises(TypeError):
        unit_convert("a","kg","g")

    with pytest.raises(TypeError):
        unit_convert(10,20,30)

    with pytest.raises(TypeError):
        unit_convert(10,"kg",30)

# Test case 2: input and output not belong to the same category

def test_category():
    """
    Test whether unit_convert raises ValueError 
    when two unrelated units are input
    """
    with pytest.raises(ValueError):
        unit_convert(10,"g","m")

    with pytest.raises(ValueError):
        unit_convert(20,"C","stone")

# Test case 3: input or output not exist

def test_units():
    """
    Test whether unit_convert raises ValueError
    when unit does not exist
    """
    with pytest.raises(ValueError):
        unit_convert(10,"g","mg")

    with pytest.raises(ValueError):
        unit_convert(10,"cm","mm")

    with pytest.raises(ValueError):
        unit_convert(20,"aaa","stone")

# Test case 4: success

def test_success():
    """
    Test whether unit_convert return right answers
    """
    assert unit_convert(1,"kg","g") == 1000

    assert unit_convert(1,"kg","kg") == 1

    assert unit_convert(1,"m","cm") == 100

    assert unit_convert(1,"L","mL") == 1000

    assert unit_convert(10,"C","F") == 50

    assert unit_convert(50,"F","C") == 10
