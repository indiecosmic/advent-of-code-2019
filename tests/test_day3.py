import pytest
from shapely.geometry import LineString
from shapely.geometry import MultiPoint
from shapely.geometry import Point
from solutions.day3 import create_wire
from solutions.day3 import find_intersection
from solutions.day3 import find_closest_distance
from solutions.day3 import steps_to_reach
from solutions.day3 import best_steps_to_reach

@pytest.mark.parametrize("test_input,expected", [('U7,R6,D4,L4', LineString([[0, 0], [0, 7], [6, 7], [6, 3], [2, 3]]))])
def test_create_wire(test_input, expected):
    assert create_wire(test_input) == expected

@pytest.mark.parametrize("test_input1,test_input2,expected", [('R8,U5,L5,D3', 'U7,R6,D4,L4', MultiPoint([[0,0], [3,3], [6,5]]))])
def test_find_intersection(test_input1, test_input2, expected):
    assert find_intersection(test_input1, test_input2) == expected

@pytest.mark.parametrize("test_input1,test_input2,expected", [
    ('R8,U5,L5,D3', 'U7,R6,D4,L4', 6),
    ('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83', 159),
    ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7', 135)])
def test_find_closest_distance(test_input1, test_input2, expected):
    assert find_closest_distance(test_input1, test_input2) == expected

@pytest.mark.parametrize("wire,point,expected", [
    ('R8,U5,L5,D3', Point(3,3), 20),
    ('U7,R6,D4,L4', Point(3,3), 20),
    ('R8,U5,L5,D3', Point(6,5), 15),
    ('R8,U5,L5,D3', Point(6,5), 15)
    ])
def test_steps_to_reach(wire, point, expected):
    assert steps_to_reach(wire, point) == expected

@pytest.mark.parametrize("input1,input2,expected", [
    ('R8,U5,L5,D3', 'U7,R6,D4,L4', 30),
    ('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83', 610),
    ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7', 410)
    ])
def test_best_steps_to_reach(input1, input2, expected):
    assert best_steps_to_reach(input1, input2) == expected