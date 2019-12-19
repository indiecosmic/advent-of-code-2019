import os
from typing import List
from common.Point import Point

keys = ['abcdefghijklmnopqrstuvwxyz']
doors = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']

class Tile:
    def __init__(self, symbol: str):
        self.symbol = symbol
        if symbol in keys:
            self.key = True
        elif symbol in doors:
            self.door = True
            self.open = False
        elif symbol == '#':
            self.wall = True
    def passable(self):
        if self.wall:
            return False
        if self.door:
            return True if self.open else False
        return True

def create_map(lines: List[str]):
    map = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            map[Point(x, y)] = Tile(lines[y][x])
    return map


def get_input():
    file_path = os.path.join(os.path.dirname(__file__), 'day18.txt')
    with open(file_path) as f:
        lines = f.read().splitlines()
        return lines


def part1():
    lines = get_input()
    map = create_map(lines)
    pass


if __name__ == '__main__':
    part1()
