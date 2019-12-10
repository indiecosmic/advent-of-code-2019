from typing import List
from typing import Tuple
from math import sqrt
from math import isclose
from timeit import timeit
from collections import namedtuple

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
        if is_on(position, target, o):
            return False
    return True

def is_on(a:Tuple[int,int], b:Tuple[int,int], c:Tuple[int,int]):
    "Return true iff point c intersects the line segment from a to b."
    # (or the degenerate case that all 3 points are coincident)
    return (collinear(a, b, c)
            and (within(a[0], c[0], b[0]) if a[0] != b[0] else
                 within(a[1], c[1], b[1])))

def collinear(a:Tuple[int,int], b:Tuple[int,int], c:Tuple[int,int]):
    "Return true iff a, b, and c all lie on the same line."
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])

def within(p, q, r):
    "Return true iff q is between p and r (inclusive)."
    return p <= q <= r or r <= q <= p

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