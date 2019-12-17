import pytest
from solutions.day14 import create_cookbook
from solutions.day14 import get_reactions
from solutions.day14 import get_needed_ingredients
from solutions.day14 import get_needed_ore

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
    ('FUEL', 1, str(
        '2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG\n'
        '17 NVRVD, 3 JNWZP => 8 VPVL\n'
        '53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL\n'
        '22 VJHF, 37 MNCFX => 5 FWMGM\n'
        '139 ORE => 4 NVRVD\n'
        '144 ORE => 7 JNWZP\n'
        '5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC\n'
        '5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV\n'
        '145 ORE => 6 MNCFX\n'
        '1 NVRVD => 8 CXFTF\n'
        '1 VJHF, 6 MNCFX => 4 RFSQX\n'
        '176 ORE => 6 VJHF'), 180697)
    ])
def test_get_reactions(chemical, amount, input, expected):
    cookbook = create_cookbook(input)
    needed = get_reactions(chemical, amount, cookbook)
    ore_required = needed['ORE']
    assert ore_required == expected

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
    ('FUEL', 1, str(
        '157 ORE => 5 NZVS\n'
        '165 ORE => 6 DCFZ\n'
        '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL\n'
        '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ\n'
        '179 ORE => 7 PSHF\n'
        '177 ORE => 5 HKGWZ\n'
        '7 DCFZ, 7 PSHF => 2 XJWVT\n'
        '165 ORE => 2 GPVTF\n'
        '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT\n'), 13312),
    ('FUEL', 1, str(
        '2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG\n'
        '17 NVRVD, 3 JNWZP => 8 VPVL\n'
        '53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL\n'
        '22 VJHF, 37 MNCFX => 5 FWMGM\n'
        '139 ORE => 4 NVRVD\n'
        '144 ORE => 7 JNWZP\n'
        '5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC\n'
        '5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV\n'
        '145 ORE => 6 MNCFX\n'
        '1 NVRVD => 8 CXFTF\n'
        '1 VJHF, 6 MNCFX => 4 RFSQX\n'
        '176 ORE => 6 VJHF'), 180697)
    ])
def test_get_needed_ingredients(chemical, amount, input, expected):
    cookbook = create_cookbook(input)
    required = {}
    get_needed_ingredients(chemical, amount, cookbook, required)
    assert get_needed_ore(required, cookbook) == expected

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