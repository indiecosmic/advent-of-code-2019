import pytest
from solutions.day8 import create_layers
from solutions.day8 import count_occurences
from solutions.day8 import merge_layers

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

@pytest.mark.parametrize('input, expected', [
    ('0222112222120000', ['01', '10'])
])
def test_merge_layers(input, expected):
    layers = create_layers(input, 2, 2)
    assert merge_layers(layers, 2, 2) == expected