import os
from enum import Enum
from typing import List, Dict
from queue import PriorityQueue
from string import ascii_uppercase
from sys import maxsize
from common.Point import Point


class Type(Enum):
    WALL = 1
    OPEN = 2
    PORTAL = 3
    START = 4
    FINISH = 5


class Tile:
    def __init__(self, symbol: str):
        self.symbol = symbol
        if symbol in ascii_uppercase:
            self.type = Type.PORTAL
            self.portal_pos = None
            self.target_pos = None
            self.portal_name = ''
        elif symbol == '#':
            self.type = Type.WALL
        elif symbol == '.':
            self.type = Type.OPEN

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol


def create_map(input: List[str]) -> Dict[Point, Tile]:
    map = {}
    for y in range(len(input)):
        for x in range(len(input[y])):
            tile = input[y][x]
            if tile != ' ':
                map[Point(x, y)] = Tile(tile)

    portals = [k for k, v in map.items() if v.type == Type.PORTAL]
    for pos in portals:
        current = map[pos]
        adjacent = get_adjacent_tiles(pos, map)
        for t in adjacent:
            tile = map[t]
            if tile.type == Type.OPEN:
                current.portal_pos = t
            elif tile.type == Type.PORTAL:
                current.portal_name = ''.join(
                    sorted(current.symbol + tile.symbol))
    for pos in portals:
        current = map[pos]
        if current.portal_pos == None:
            current.type = Type.WALL
        elif current.portal_name == 'AA':
            current.type = Type.START
        elif current.portal_name == 'ZZ':
            current.type = Type.FINISH
    for portal in [v for k, v in map.items() if v.type == Type.PORTAL]:
        targets = [v for k, v in map.items() if v.type == Type.PORTAL and v.portal_name ==
                   portal.portal_name and v.portal_pos != portal.portal_pos]
        portal.target_pos = targets[0].portal_pos

    return map


def shortest_path(source: Point, target: Point, map):
    dist = {}
    q = PriorityQueue()
    tiles = [k for k, v in map.items() if v.type == Type.OPEN]
    for tile in tiles:
        dist[tile] = maxsize
    q.put((0, source))
    dist[source] = 0
    while not q.empty():
        _, u = q.get()
        if u == target:
            break
        for v in get_connected_tiles(u, map):
            if dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                q.put((dist[v], v))
    return dist[target]


def get_start_and_finish(map):
    portals = [v for k, v in map.items() if v.type in [
        Type.START, Type.FINISH]]
    return (portals[0].portal_pos, portals[1].portal_pos) if portals[0].type == Type.START else (portals[1].portal_pos, portals[0].portal_pos)


def get_connected_tiles(pos: Point, map):
    connected = []
    adjacent = get_adjacent_tiles(pos, map)
    for a in adjacent:
        tile = map[a]
        if tile.type == Type.OPEN:
            connected.append(a)
        if tile.type == Type.PORTAL:
            connected.append(tile.target_pos)
    return connected


def get_adjacent_tiles(pos: Point, map):
    adjacent = []
    for c in [
        Point(pos.x, pos.y + 1),
        Point(pos.x, pos.y - 1),
        Point(pos.x + 1, pos.y),
        Point(pos.x - 1, pos.y)
    ]:
        if c in map:
            adjacent.append(c)
    return adjacent


def get_input() -> List[str]:
    file_path = __file__.replace('.py', '.txt')
    with open(file_path) as f:
        contents = f.read()
        contents = contents.splitlines()
        return contents
def part1(map):
    start, finish = get_start_and_finish(map)
    shortest = shortest_path(start, finish, map)
    print(shortest)

if __name__ == "__main__":
    input = get_input()
    puzzle_map = create_map(input)
    part1(puzzle_map)
