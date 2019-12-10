from typing import List
from shapely.geometry import Point
from shapely.geometry import LineString

def parse_map(input: str):
    return input.split('\n')

def find_coordinates(map: List[str]):
    coordinates = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == '#':
                coordinates.append((x,y))
    return coordinates

def can_detect(position, target, asteroids):
    obstacles = set(asteroids) - set([position,target])
    line = LineString([position, target])
    for o in obstacles:
        if line.intersects(Point(o)):
            return False
    return True

def find_best_location(asteroids):
    max = 0
    maxpos = ()
    for pos in asteroids:
        count = 0
        for target in asteroids:
            if pos == target:
                continue
            if can_detect(pos, target, asteroids):
                count += 1
        if count > max:
            max = count
            maxpos = pos
    return (maxpos, max)

def part1():
    pass

if __name__ == "__main__":
    with open('day10.txt') as f:
        contents = f.read()
        map = parse_map(contents)
        asteroids = find_coordinates(map)
        print(find_best_location(asteroids))