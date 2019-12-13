import os
from collections import defaultdict
from common.Intcode import Intcode
from common.Point import Point


def create_state(input):
    tiles = defaultdict(lambda: 0)
    for index in range(0, len(input), 3):
        tiles[Point(input[index],input[index+1])] = input[index+2]
    return tiles

def handle_input(computer):
    inp = input()
    if inp == '1':
        computer.set_input(-1)
    if inp == '':
        computer.set_input(0)
    if inp == '2':
        computer.set_input(1)

def update(computer, state):
    computer.run_program()
    for index in range(0, len(computer.outputs), 3):
        state[Point(computer.outputs[index],computer.outputs[index+1])] = computer.outputs[index+2]
    return state

def render(computer, state):
    x_max = max([key.x for key in state])
    y_max = max([key.y for key in state])
    for y in range(y_max + 1):
        row = ''
        for x in range(x_max + 1):
            if state[(x,y)] == 0:
                row += '░'
            elif state[(x,y)] == 1:
                row += '█'
            elif state[(x,y)] == 2:
                row += '★'
            elif state[(x,y)] == 3:
                row += '─'
            elif state[(x,y)] == 4:
                row += '●'
            else:
                row += str(state[(x,y)])
        print(row)
    print('Score: ' + str(state[(-1, 0)]))

def part1(instructions):
    computer = Intcode(instructions, [])
    computer.run_program()
    tiles = create_state(computer.outputs)
    block_tiles = [k for k,v in tiles.items() if v == 2]
    return len(block_tiles)

def part2(instructions):
    computer = Intcode(instructions, [])
    computer.memory[0] = 2
    computer.run_program()
    state = create_state(computer.outputs)
    render(computer, state)
    while computer.stopped == False:
        handle_input(computer)
        update(computer, state)
        render(computer, state)
    pass

def get_input():
    file_path = os.path.join(os.path.dirname(__file__), 'day13.txt')
    with open(file_path) as f:
        contents = f.read()
        program_str = contents.strip().split(',')
        instructions = list(map(int, program_str))
        return instructions

def main():
    instructions = get_input()
    print(part1(instructions))
    print(part2(instructions))

if __name__ == "__main__":
    main()