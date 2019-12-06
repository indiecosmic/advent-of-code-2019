import pytest
from solutions.day6 import create_map,orbit_count, create_tree, total_orbit_count, find_common_parent, number_of_transfers

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

def test_find_common_parent():
    tree = create_tree(['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN'])
    common = find_common_parent('YOU', 'SAN', tree)
    assert common == 'D'

def test_number_of_transfers():
    tree = create_tree(['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN'])
    count = number_of_transfers('YOU', 'SAN', tree)
    assert count == 4