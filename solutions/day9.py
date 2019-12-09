from .Intcode import Intcode

def part1(instructions):
    intcode = Intcode(instructions, [1], True)
    intcode.run_program()
    return intcode.outputs

if __name__ == "__main__":
    with open('day9.txt') as f:
        contents = f.read()
        program_str = contents.strip().split(',')
        instructions = list(map(int, program_str))
        print(part1(instructions))