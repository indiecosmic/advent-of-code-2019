import os
from common.Intcode import Intcode
from common.Point import Point


def get_input():
    file_path = os.path.join(os.path.dirname(__file__), 'day19.txt')
    with open(file_path) as f:
        contents = f.read()
        program_str = contents.strip().split(',')
        instructions = list(map(int, program_str))
        return instructions


def part1(instructions):
    count = 0
    for y in range(50):
        for x in range(50):
            computer = Intcode(instructions, [x, y])
            computer.run_program()
            count += computer.get_output()
    print(count)


if __name__ == "__main__":
    instructions = get_input()
    part1(instructions)
    '''part2(instructions)'''
