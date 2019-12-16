import pytest
from solutions.day16 import create_patterns
from solutions.day16 import calculate_signal

def test_create_patterns():
    patterns = create_patterns(8)
    assert patterns == [
        [1, 0, -1, 0, 1, 0, -1, 0],
        [0, 1, 1, 0, 0, -1, -1, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1]
    ]

@pytest.mark.parametrize("signal,times,expected", [
    ([1,2,3,4,5,6,7,8], 1, [4,8,2,2,6,1,5,8]),
    ([1,2,3,4,5,6,7,8], 2, [3,4,0,4,0,4,3,8]),
    ([1,2,3,4,5,6,7,8], 3, [0,3,4,1,5,5,1,8]),
    ([1,2,3,4,5,6,7,8], 4, [0,1,0,2,9,4,9,8]),
])
def test_calculate_signal(signal, times, expected):
    assert calculate_signal(signal, times) == expected

@pytest.mark.parametrize("signal,times,expected", [
    ([8,0,8,7,1,2,2,4,5,8,5,9,1,4,5,4,6,6,1,9,0,8,3,2,1,8,6,4,5,5,9,5], 100, [2,4,1,7,6,1,7,6]),
    ([1,9,6,1,7,8,0,4,2,0,7,2,0,2,2,0,9,1,4,4,9,1,6,0,4,4,1,8,9,9,1,7], 100, [7,3,7,4,5,4,1,8]),
    ([6,9,3,1,7,1,6,3,4,9,2,9,4,8,6,0,6,3,3,5,9,9,5,9,2,4,3,1,9,8,7,3], 100, [5,2,4,3,2,1,3,3])
])
def test_calculate_large_signal(signal, times, expected):
    result = calculate_signal(signal, times)
    assert result[:8] == expected