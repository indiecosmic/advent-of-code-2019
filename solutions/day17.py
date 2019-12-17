import os
from typing import List
from typing import Dict
from typing import Tuple
from common.Intcode import Intcode
from common.Point import Point

class Robot:
    def __init__(self, pos: Point, dir: Point):
        self.pos = pos
        self.dir = dir

def render(map):
    x_min = min([key.x for key in map])
    x_max = max([key.x for key in map])
    y_min = min([key.y for key in map])
    y_max = max([key.y for key in map])
    for y in range(y_min, y_max + 1):
        row = ''
        for x in range(x_min, x_max + 1):
            if (x,y) not in map:
                row += ' '
            else:
                row += map[(x,y)]
        print(row)

def print_message(ascii: List[int]):
    print([chr(c) for c in ascii])

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

def walk_to_edge(robot, dir, map):
    steps = 0
    pos = robot
    while True:
        pos = Point(pos.x + dir.x, pos.y + dir.y)
        if pos in map and map[pos] != '.':
            steps += 1
        else:
            break
    return steps

def turn(robot, dir, map):
    # can turn right
    turn = Point(-dir.y, dir.x)
    next = Point(robot.x + turn.x, robot.y + turn.y)
    if next in map and map[next] != '.':
        return ('R', turn)
    # can turn right
    turn = Point(dir.y, -dir.x)
    next = Point(robot.x + turn.x, robot.y + turn.y)
    if next in map and map[next] != '.':
        return ('L', turn)
    return None

def convert_to_ascii(text: str):
    res = []
    for t in text:
        res.append(ord(t))
    return res + [10]

def part1(instructions):
    computer = Intcode(instructions, [])
    computer.run_program()
    map = create_map(computer.outputs)
    render(map)
    intersections = get_intersections(map)
    parameters = []
    for i in intersections:
        parameters.append(i.x * i.y)
    print(sum(parameters))

def part2(instructions):
    computer = Intcode(instructions, [])
    computer.run_program()
    map = create_map(computer.outputs)
    robot = [key for (key,value) in map.items() if value == '^'][0]
    dir = Point(0, -1)
    movements = []
    while True:
        #walk to edge
        dist = walk_to_edge(robot, dir, map)
        if dist > 0:
            movements.append(dist)
            robot = Point(robot.x + dir.x * dist, robot.y + dir.y * dist)
        #try turn
        direction = turn(robot, dir, map)
        if direction != None:
            movements.append(direction[0])
            dir = direction[1]
        if dist == 0 and direction == None:
            break
    print(movements)
    computer = Intcode(instructions, [])
    computer.memory[0] = 2
    computer.run_program()
    #Main routine: [A,B,B,C,C,A,B,B,C,A]
    computer.inputs += convert_to_ascii('A,B,B,C,C,A,B,B,C,A')
    computer.run_program()
    print_message(computer.outputs)
    #Function A: 'R', 4, 'R', 12, 'R', 10, 'L', 12
    computer.inputs += convert_to_ascii('R,4,R,12,R,10,L,12')
    computer.run_program()
    print_message(computer.outputs)
    #Function B: 'L', 12, 'R', 4, 'R', 12
    computer.inputs += convert_to_ascii('L,12,R,4,R,12')
    computer.run_program()
    print_message(computer.outputs)
    #Function C: 'L', 12, 'L', 8, 'R', 10
    computer.inputs += convert_to_ascii('L,12,L,8,R,10')
    computer.run_program()
    print_message(computer.outputs)
    computer.inputs += convert_to_ascii('n')
    computer.run_program()
    print(computer.outputs[-1])

def create_map(inputs: List[int]) -> Dict[Point, str]:
    map = {}
    y = 0
    x = 0
    for i in inputs:
        if i == 10:
            y += 1
            x = 0
        else:
            map[Point(x, y)] = chr(i)
            x += 1
    return map

def get_intersections(map):
    intersections = []
    scaffolds = [key  for (key, value) in map.items() if value in ['#','^','v','<','>']]
    for s in scaffolds:
        if is_intersection(s, map):
            intersections.append(s)
    return intersections

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
    part2(instructions)

if __name__ == "__main__":
    main()