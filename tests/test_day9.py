import pytest
from common.Intcode import Intcode

@pytest.mark.parametrize("instructions, inputs, expected", [
    ([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], [0], [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]),
    ([1102,34915192,34915192,7,4,7,99,0], [0], [1219070632396864]),
    ([104,1125899906842624,99], [0], [1125899906842624])
])
def test_run_program(instructions, inputs, expected):
    intcode = Intcode(instructions, inputs)
    intcode.run_program()
    assert intcode.outputs == expected
