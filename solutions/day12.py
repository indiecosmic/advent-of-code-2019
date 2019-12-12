import os
from copy import deepcopy
from math import gcd
from typing import List, Tuple
from common.Point3D import Point3D


class Moon:
    def __init__(self, pos: Point3D, vel: Point3D = Point3D(0, 0, 0)):
        self.pos = pos
        self.vel = vel

    def __repr__(self):
        return 'Moon({0}, {1})'.format(self.pos, self.vel)


def apply_gravity(moons: List[Moon]):
    for moon in moons:
        others = set(moons) - set([moon])
        diff = [0,0,0]
        for axis in range(3):
            for other in others:
                if moon.pos[axis] < other.pos[axis]:
                    diff[axis] += 1
                if moon.pos[axis] > other.pos[axis]:
                    diff[axis] -= 1
        moon.vel = Point3D(moon.vel.x + diff[0], moon.vel.y + diff[1], moon.vel.z + diff[2])
    return moons


def apply_velocity(moons: List[Moon]):
    for moon in moons:
        moon.pos = Point3D(moon.pos.x + moon.vel.x,
                           moon.pos.y + moon.vel.y, moon.pos.z + moon.vel.z)
    return moons


def calculate_energy(moons: List[Moon]):
    return sum([(abs(moon.pos.x) + abs(moon.pos.y) + abs(moon.pos.z)) * (abs(moon.vel.x) + abs(moon.vel.y) + abs(moon.vel.z)) for moon in moons])

def create_moons(positions: List[Point3D]):
    return [Moon(Point3D(pos[0], pos[1], pos[2])) for pos in positions]


def simulate(moons, times):
    for _ in range(1000):
        apply_gravity(moons)
        apply_velocity(moons)
    return moons


def find_repetition_cycles(moons):
    result = [0, 0, 0]
    for axis in range(3):
        states = set()
        t = 0
        while True:
            state = []
            apply_gravity(moons)
            apply_velocity(moons)
            for moon in moons:
                state.append(moon.pos[axis])
                state.append(moon.vel[axis])
            str_state = str(state)
            if str_state in states:
                result[axis] = t
                break
            states.add(str_state)
            t += 1
    return result


def lcm(a, b): return (a*b)//gcd(a, b)


def part1(moons):
    moons = simulate(moons, 1000)
    return calculate_energy(moons)


def part2(moons: List[Moon]):
    cycles = find_repetition_cycles(moons)
    return lcm(lcm(cycles[0], cycles[1]), cycles[2])


def main():
    path = os.path.join(os.path.dirname(__file__), 'day12.txt')
    moons = []
    with open(path) as f:
        lines = f.read().splitlines()
        lines = [line.replace('<x=', '').replace('y=', '').replace(
            'z=', '').replace('>', '') for line in lines]
        positions = [list(map(int, line.split(','))) for line in lines]
        moons = create_moons(positions)
    print(part1(deepcopy(moons)))
    print(part2(moons))


if __name__ == "__main__":
    main()
