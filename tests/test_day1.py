import pytest
from solutions.day1 import fuel_requirement
from solutions.day1 import fuel_requirement_r

@pytest.mark.parametrize("test_input,expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)])
def test_fuel_requirement(test_input, expected):
    assert fuel_requirement(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [(14, 2), (1969, 966), (100756, 50346)])
def test_fuel_requirement_r(test_input, expected):
    assert fuel_requirement_r(test_input) == expected
