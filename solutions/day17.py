import os
from common.Intcode import Intcode
from common.Point import Point

def is_intersection(pos: Point, map):
    neighbours = get_connected_tiles(pos, map)
    if len(neighbours) < 4:
        return False
    for n in neighbours:
        if map[n] not in ['#','^','v','<','>']:
            return False
    return True

def get_connected_tiles(pos: Point, map):
    connected = []
    for c in [
        Point(pos.x, pos.y + 1),
        Point(pos.x, pos.y - 1),
        Point(pos.x + 1, pos.y),
        Point(pos.x - 1, pos.y)
    ]:
        if c in map:
            connected.append(c)
    return connected

def part1(instructions):
    computer = Intcode(instructions, [])
    computer.run_program()
    map = {}
    y = 0
    x = 0
    for o in computer.outputs:
        if o == 10:
            y += 1
            x = 0
        else:
            map[Point(x, y)] = chr(o)
        x += 1
    scaffolds = [key  for (key, value) in map.items() if value in ['#','^','v','<','>']]
    intersections = []
    for s in scaffolds:
        if is_intersection(s, map):
            intersections.append(s)
    parameters = []
    for i in intersections:
        parameters.append(i.x * i.y)
    print(sum(parameters))

def get_input():
    file_path = os.path.join(os.path.dirname(__file__), 'day17.txt')
    with open(file_path) as f:
        contents = f.read()
        program_str = contents.strip().split(',')
        instructions = list(map(int, program_str))
        return instructions

def main():
    instructions = get_input()
    part1(instructions)

if __name__ == "__main__":
    main()