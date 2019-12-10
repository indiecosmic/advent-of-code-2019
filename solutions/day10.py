from typing import List
from math import sqrt
from math import isclose

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
    for o in obstacles:
        if o[0] < min(position[0], target[0]) or o[0] > max(position[0], target[0]):
            continue
        if o[1] < min(position[1], target[1]) or o[1] > max(position[1], target[1]):
            continue
        if is_between(position, o, target):
            return False
    return True

def distance(a,b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_between(a,c,b):
    return isclose(distance(a,c) + distance(c,b), distance(a,b))

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

def part1(asteroids):
    return find_best_location(asteroids)

if __name__ == "__main__":
    with open('day10.txt') as f:
        contents = f.read()
        map = parse_map(contents)
        asteroids = find_coordinates(map)
        print(part1(asteroids))