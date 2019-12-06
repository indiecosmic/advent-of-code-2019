import pytest
from solutions.day6 import create_map,orbit_count, create_tree, total_orbit_count

@pytest.mark.parametrize("test_input,expected", [
    (["COM)B"], {'COM': ['B']}),
    (["B)C", "B)G"], {'B': ['C','G']})
    ])
def test_create_map(test_input, expected):
    assert create_map(test_input) == expected

def test_orbit_count():
    tree = create_tree(['COM)B', 'B)C', 'C)D','D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L'])
    assert orbit_count('L', tree) == 7

def test_total_orbit_count():
    assert total_orbit_count(['COM)B', 'B)C', 'C)D','D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']) == 42