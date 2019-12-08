import pytest
from solutions.day8 import create_layers
from solutions.day8 import count_occurences

@pytest.mark.parametrize("input, expected", [
    ('123456789012', [['123','456'], ['789','012']])
])
def test_create_layers(input, expected):
    assert create_layers(input, 3, 2) == expected

@pytest.mark.parametrize('value, layer, expected', [
    ('1',['121','421'],3)
])
def test_count_occurences(value, layer, expected):
    assert count_occurences(value, layer) == expected