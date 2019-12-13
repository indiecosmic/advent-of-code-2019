import pytest
from solutions.day13 import draw_tiles

def test_draw_tiles():
    output = [1,2,3,6,5,4]
    expected = {
        (1,2):3,
        (6,5):4
        }
    assert draw_tiles(output) == expected