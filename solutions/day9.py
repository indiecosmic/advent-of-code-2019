import os
from common.Intcode import Intcode

def part1(instructions):
    intcode = Intcode(instructions, [1], True)
    intcode.run_program()
    return intcode.outputs

def part2(instructions):
    intcode = Intcode(instructions, [2], True)
    intcode.run_program()
    return intcode.outputs

def main():
    path = os.path.join(os.path.dirname(__file__), 'day9.txt')
    with open(path) as f:
        contents = f.read()
        program_str = contents.strip().split(',')
        instructions = list(map(int, program_str))
        print(part1(instructions))
        print(part2(instructions))

if __name__ == "__main__":
    main()