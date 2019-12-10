import pytest
from solutions.day10 import parse_map
from solutions.day10 import find_coordinates
from solutions.day10 import can_detect
from solutions.day10 import find_best_location

def test_parse_map():
    input = str('.#..#\n'+
            '.....\n'+
            '#####\n'+
            '....#\n'+
            '...##')
    result = parse_map(input)
    assert result == ['.#..#','.....','#####','....#','...##']

def test_find_coordinates():
    input = ['.#..#','.....','#####','....#','...##']
    result = find_coordinates(input)
    assert result == [(1,0),(4,0),(0,2),(1,2),(2,2),(3,2),(4,2),(4,3),(3,4),(4,4)]

@pytest.mark.parametrize("position,target,asteroids,expected", [
    ((4,2), (3,2), [(1,0),(4,0),(0,2),(1,2),(2,2),(3,2),(4,2),(4,3),(3,4),(4,4)], True),
    ((4,2), (2,2), [(1,0),(4,0),(0,2),(1,2),(2,2),(3,2),(4,2),(4,3),(3,4),(4,4)], False),
    ((4,2), (4,4), [(1,0),(4,0),(0,2),(1,2),(2,2),(3,2),(4,2),(4,3),(3,4),(4,4)], False),
    ((4,2), (1,0), [(1,0),(4,0),(0,2),(1,2),(2,2),(3,2),(4,2),(4,3),(3,4),(4,4)], True),
    ((30,34), (21,19), [(24,24)], False),
    ((30,34), (27,19), [(29,29)], False)
])
def test_can_detect(position, target, asteroids, expected):
    assert can_detect(position, target, asteroids) == expected

@pytest.mark.parametrize("asteroids,expected", [
    ([(1,0),(4,0),(0,2),(1,2),(2,2),(3,2),(4,2),(4,3),(3,4),(4,4)], ((3,4),8)),
])
def test_find_best_location(asteroids, expected):
    assert find_best_location(asteroids) == expected

def test_find_best_location_from_map():
    input = str('.#..##.###...#######\n'
                '##.############..##.\n'
                '.#.######.########.#\n'
                '.###.#######.####.#.\n'
                '#####.##.#.##.###.##\n'
                '..#####..#.#########\n'
                '####################\n'
                '#.####....###.#.#.##\n'
                '##.#################\n'
                '#####.##.###..####..\n'
                '..######..##.#######\n'
                '####.##.####...##..#\n'
                '.#####..#.######.###\n'
                '##...#.##########...\n'
                '#.##########.#######\n'
                '.####.#.###.###.#.##\n'
                '....##.##.###..#####\n'
                '.#.#.###########.###\n'
                '#.#.#.#####.####.###\n'
                '###.##.####.##.#..##')
    map = parse_map(input)
    asteroids = find_coordinates(map)
    assert find_best_location(asteroids) == ((11,13), 210)