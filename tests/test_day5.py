import pytest
from solutions.day5 import opcode
from solutions.day5 import mode

@pytest.mark.parametrize("test_input,expected", [(1002, 2), (1101, 1)])
def test_opcode(test_input, expected):
    assert opcode(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [(1002, (0,1,0))])
def test_mode(test_input, expected):
    assert mode(test_input) == expected