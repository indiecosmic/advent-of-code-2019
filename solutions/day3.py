from shapely.geometry import LineString
from shapely.geometry import MultiPoint
from shapely.geometry import Point
from shapely.ops import nearest_points
from sys import maxsize



def create_wire(input: str):
    
    paths = input.split(',')
    x = 0
    y = 0
    points = [[0, 0]]
    for path in paths:
        direction = path[0]
        length = int(path[1:])
        if (direction == 'U'):
            y += length
        elif (direction == 'D'):
            y -= length
        elif (direction == 'L'):
            x -= length
        else:
            x += length
        points.append([x,y])
    return LineString(points)

def find_intersection(input1: str, input2: str) -> MultiPoint:
    wire1 = create_wire(input1)
    wire2 = create_wire(input2)
    return wire1.intersection(wire2)

def find_closest_distance(input1: str, input2: str):
    intersections = find_intersection(input1, input2)
    if (len(intersections.geoms) == 0):
        return None
    points = list(intersections.geoms)
    if (Point(0,0) in points):
        points.remove(Point(0,0))
    min_distance = maxsize
    for point in points:
        distance = manhattan_distance(point)
        if (distance < min_distance):
            min_distance = distance
    return min_distance

def manhattan_distance(point: Point) -> int:
    return abs(point.x) + abs(point.y)

def steps_to_reach(input: str, point: Point):
    wire = create_wire(input)
    return wire.project(point)

def best_steps_to_reach(input1: str, input2: str):
    intersections = find_intersection(input1, input2)
    if (len(intersections.geoms) == 0):
        return None
    points = list(intersections.geoms)
    if (Point(0,0) in points):
        points.remove(Point(0,0))
    min_steps = maxsize
    for point in points:
        steps = steps_to_reach(input1, point) + steps_to_reach(input2, point)
        if (steps < min_steps):
            min_steps = steps
    return min_steps

def part1(parts):
    return find_closest_distance(parts[0], parts[1])

def part2(parts):
    return best_steps_to_reach(parts[0], parts[1])

if __name__ == '__main__':
    with open('day3.txt') as f:
        contents = f.read()
        parts = contents.strip().split('\n')
        print(part1(parts))
        print(part2(parts))
        