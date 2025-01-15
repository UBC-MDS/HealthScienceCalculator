import pytest
from healthsciencecalculator import healthsciencecalculator

# Test case 1: wrong input type

def test_valid_input():
    
    with pytest.raises(TypeError):
        unit_convert("a","kg","g")

    with pytest.raises(TypeError):
        unit_convert(10,20,30)

# Test case 2: input and output not belong to the same category

def test_category():

    with pytest.raises(ValueError):
        unit_convert(10,"g","m")

    with pytest.raises(ValueError):
        unit_convert(20,"C","stone")

# Test case 3: input or output not exist

def test_quantites():

    with pytest.raises(ValueError):
        unit_convert(10,"g","mg")

    with pytest.raises(ValueError):
        unit_convert(10,"cm","mm")

# Test case 4: success

def test_success():

    assert unit_convert(1,"kg","g") == 1000

    assert unit_convert(1,"m","cm") == 100

    assert unit_convert(1,"L","mL") == 1000

    assert unit_convert(10,"C","F") == 50