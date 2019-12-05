import pytest
from solutions.day4 import increasing
from solutions.day4 import contains_doubles
from solutions.day4 import contains_strict_double

@pytest.mark.parametrize("test_input,expected", [(111111, True), (223450, False), (123789, True)])
def test_increasing(test_input, expected):
    assert increasing(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [(111111, True), (223450, True), (123789, False)])
def test_contains_doubles(test_input, expected):
    assert contains_doubles(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [(112233, True), (123444, False), (111122, True)])
def test_contains_strict_double(test_input, expected):
    assert contains_strict_double(test_input) == expected
