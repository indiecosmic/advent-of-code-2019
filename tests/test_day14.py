import pytest
from solutions.day14 import create_cookbook
from solutions.day14 import get_reactions

@pytest.mark.parametrize("chemical,amount,input,expected", [
    ('A', 10, str(
        '10 ORE => 10 A\n'
        '1 ORE => 1 B\n'
        '7 A, 1 B => 1 C\n'
        '7 A, 1 C => 1 D\n'
        '7 A, 1 D => 1 E\n'
        '7 A, 1 E => 1 FUEL\n'), 10),
    ('FUEL', 1, str(
        '10 ORE => 10 A\n'
        '1 ORE => 1 B\n'
        '7 A, 1 B => 1 C\n'
        '7 A, 1 C => 1 D\n'
        '7 A, 1 D => 1 E\n'
        '7 A, 1 E => 1 FUEL\n'), 31),
    ('FUEL', 1, str(
        '9 ORE => 2 A\n'
        '8 ORE => 3 B\n'
        '7 ORE => 5 C\n'
        '3 A, 4 B => 1 AB\n'
        '5 B, 7 C => 1 BC\n'
        '4 C, 1 A => 1 CA\n'
        '2 AB, 3 BC, 4 CA => 1 FUEL\n'), 165),
    ])
def test_get_reactions(chemical, amount, input, expected):
    cookbook = create_cookbook(input)
    result = []
    waste = {}
    get_reactions(chemical, amount, cookbook, result, waste)
    ore_required = sum([a for r,a in result if r == 'ORE'])
    assert ore_required == expected

def test_create_cookbook():
    input = str(
        '10 ORE => 10 A\n'
        '1 ORE => 1 B\n'
        '7 A, 1 B => 1 C\n'
        '7 A, 1 C => 1 D\n'
        '7 A, 1 D => 1 E\n'
        '7 A, 1 E => 1 FUEL\n')
    cookbook = create_cookbook(input)
    assert cookbook == {
        'FUEL': (1, [('A', 7), ('E', 1)]),
        'A': (10, [('ORE', 10)]),
        'B': (1, [('ORE', 1)]),
        'C': (1, [('A', 7), ('B', 1)]),
        'D': (1, [('A', 7), ('C', 1)]),
        'E': (1, [('A', 7), ('D', 1)])
    }