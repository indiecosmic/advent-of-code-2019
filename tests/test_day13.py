import pytest
from solutions.day13 import create_state

def test_create_state():
    output = [1,2,3,6,5,4]
    expected = {
        (1,2):3,
        (6,5):4
        }
    assert create_state(output) == expected