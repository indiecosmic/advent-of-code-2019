import pytest
from solutions.day5 import opcode
from solutions.day5 import mode
from solutions.day5 import run_opcode

@pytest.mark.parametrize("test_input,expected", [(1002, 2), (1101, 1), (99, 99)])
def test_opcode(test_input, expected):
    assert opcode(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [(1002, (0,1,0))])
def test_mode(test_input, expected):
    assert mode(test_input) == expected

@pytest.mark.parametrize("index, instructions, expected", [
    (0, [1002,4,3,4,33], [1002,4,3,4,99]),
    (0, [1,0,0,0,99], [2,0,0,0,99]),
    (0, [1101,100,-1,4,0], [1101,100,-1,4,99])
    ])
def test_run_opcode(index, instructions, expected):
    assert run_opcode(index, instructions) == expected