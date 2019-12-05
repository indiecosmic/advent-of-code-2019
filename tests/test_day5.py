import pytest
from solutions.day5 import opcode
from solutions.day5 import get_mode
from solutions.day5 import run_opcode
from solutions.day5 import run_program

@pytest.mark.parametrize("test_input,expected", [(1002, 2), (1101, 1), (99, 99)])
def test_opcode(test_input, expected):
    assert opcode(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [(1002, (0,1,0))])
def test_get_mode(test_input, expected):
    assert get_mode(test_input) == expected

@pytest.mark.parametrize("index, instructions, expected", [
    (0, [1002,4,3,4,33], [1002,4,3,4,99]),
    (0, [1,0,0,0,99], [2,0,0,0,99]),
    (0, [1101,100,-1,4,0], [1101,100,-1,4,99])
    ])
def test_run_opcode(index, instructions, expected):
    run_opcode(index, instructions)
    assert instructions == expected

@pytest.mark.parametrize("program, input, expected_output", [
    ([3,9,8,9,10,9,4,9,99,-1,8], 8, '1\n'),
    ([3,9,8,9,10,9,4,9,99,-1,8], 7, '0\n'),
    ([3,9,7,9,10,9,4,9,99,-1,8], 7, '1\n'),
    ([3,9,7,9,10,9,4,9,99,-1,8], 8, '0\n'),
    ([3,3,1108,-1,8,3,4,3,99], 8, '1\n'),
    ([3,3,1108,-1,8,3,4,3,99], 7, '0\n'),
    ([3,3,1107,-1,8,3,4,3,99], 7, '1\n'),
    ([3,3,1107,-1,8,3,4,3,99], 8, '0\n'),
    ([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0, '0\n'),
    ([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 3, '1\n'),
    ([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0, '0\n'),
    ([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 3, '1\n'),
    ([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 7, '999\n'),
    ([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 8, '1000\n'),
    ([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 20, '1001\n'),
    ])
def test_run_program(program, input, expected_output:str, capsys):
    run_program(program, input)
    captured = capsys.readouterr()
    assert captured.out == expected_output
    