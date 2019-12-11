from typing import List
from typing import Tuple
from math import sqrt
from math import isclose
from math import atan2, degrees
from common.Point import Point

def parse_map(input: str):
    return input.split('\n')

def find_coordinates(map: List[str]):
    coordinates = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == '#':
                coordinates.append(Point(x,y))
    return coordinates

def find_coordinates_and_laser(map: List[str]):
    coordinates = []
    laser = ()
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == '#':
                coordinates.append(Point(x,y))
            elif cell == 'X':
                laser = Point(x,y)
    return coordinates, laser

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
    q = (b[0] - a[0]) * (c[1] - a[1])
    w = (c[0] - a[0]) * (b[1] - a[1])
    return isclose(q,w, abs_tol = 0.01)

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

def vaporize_rotation(laser_pos, asteroids):
    upper_bounds = Point(max([a.x for a in asteroids]), max([a.y for a in asteroids]))
    q1 = (
        Point(laser_pos.x, 0),
        Point(upper_bounds.x, laser_pos.y)
        )
    q2 = (
        Point(laser_pos.x, laser_pos.y),
        Point(upper_bounds.x, upper_bounds.y)
        )
    q3 = (
        Point(0, laser_pos.y),
        Point(laser_pos.x, upper_bounds.y)
    )
    q4 = (
        Point(0,0),
        Point(laser_pos.x, laser_pos.y)
    )
    visible = find_visible(laser_pos, asteroids)
    vaporized = []
    for q in [q1,q2,q3,q4]:
        vap_order = get_vap_order(laser_pos, visible, q)
        vaporized += vaporize_quadrant(visible, vap_order)

    return vaporized

def vaporize_all(laser_pos, asteroids):
    result = []
    while len(asteroids) > 0:
        vaporized = vaporize_rotation(laser_pos, asteroids)
        asteroids = set(asteroids) - set(vaporized)
        result += vaporized
    return result

def get_vap_order(laser_pos, visible, q):
    in_q = [a for a in visible if a.x >= q[0].x and a.x <= q[1].x and a.y >= q[0].y and a.y <= q[1].y]
    vap_order = sorted([(degrees(atan2(a.y-laser_pos.y, a.x-laser_pos.x)),a) for a in in_q], key=lambda ast: ast[0])
    return vap_order

def vaporize_quadrant(visible, vap_order):
    vaporized = []
    for a in vap_order:
        vaporized.append(a[1])
        visible.remove(a[1])
    return vaporized

def find_visible(pos, asteroids):
    visible = []
    for target in asteroids:
        if pos == target:
            continue
        if can_detect(pos, target, asteroids):
            visible.append(target)
    return visible

def part1(asteroids):
    return find_best_location(asteroids)

def part2(pos, asteroids):
    asteroids.remove(pos)
    vaporized = vaporize_all(pos, asteroids)
    return vaporized[199].x * 100 + vaporized[199].y

if __name__ == "__main__":
    with open('day10.txt') as f:
        contents = f.read()
        map = parse_map(contents)
        asteroids = find_coordinates(map)
        print(part1(asteroids))
        print(part2(Point(30,34),asteroids))