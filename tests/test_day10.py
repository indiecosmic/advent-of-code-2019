from solutions.day10 import parse_map
from solutions.day10 import find_coordinates
from solutions.day10 import find_visible
from solutions.day10 import can_detect

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

def test_can_detect(position, target, asteroids):
    pass