from typing import List
from math import floor

def opcode(value:int):
    return int(str(value)[-2:])

def get_mode(value:int):
    return (floor(value//100) % 10, floor(value//1000) % 10, floor(value//10000) % 10)

def get_values(index, modes, instructions: List[int]):
    pos1 = instructions[index+1]
    pos2 = instructions[index+2]
    target = instructions[index+3]
    val1 = instructions[pos1] if modes[0] == 0 else pos1
    val2 = instructions[pos2] if modes[1] == 0 else pos2
    return (val1, val2, target)

def get_value(index, mode, instructions):
    pos = instructions[index]
    return instructions[pos] if mode == 0 else pos

def run_opcode(index:int, instructions: List[int], input: int = 1):
    op = opcode(instructions[index])
    m = get_mode(instructions[index])
    if (op == 99):
        return None
    if (op == 1):
        values = get_values(index, m, instructions)
        instructions[values[2]] = values[0] + values[1]
        return index + 4
    elif (op == 2):
        values = get_values(index, m, instructions)
        instructions[values[2]] = values[0] * values[1]
        return index + 4
    elif (op == 3):
        target = instructions[index+1]
        instructions[target] = input
        return index + 2
    elif op == 4:
        value = get_value(index + 1, m[0], instructions)
        print(value)
        return index + 2
    elif op == 5:
        param1 = get_value(index + 1, m[0], instructions)
        if param1 != 0:
            return get_value(index + 2, m[1], instructions)
        return index + 3
    elif op == 6:
        param1 = get_value(index + 1, m[0], instructions)
        if param1 == 0:
            return get_value(index + 2, m[1], instructions)
        return index + 3
    elif op == 7:
        values = get_values(index, m, instructions)
        instructions[values[2]] = 1 if values[0] < values[1] else 0
        return index + 4
    elif op == 8:
        values = get_values(index, m, instructions)
        instructions[values[2]] = 1 if values[0] == values[1] else 0
        return index + 4
    else:
        raise Exception('invalid opcode: {}'.format(op))

def run_program(program, input):
    index = 0
    while index < len(program):
        op = opcode(program[index])
        if op == 99:
            break
        index = run_opcode(index, program, input)

def part1(program):
    run_program(program, 1)

def part2(program):
    run_program(program, 5)

if __name__ == '__main__':
    with open('day5.txt') as f:
        contents = f.read()
        program_str = contents.strip().split(',')
        program = list(map(int, program_str))
        part1(program)
        program = list(map(int, program_str))
        part2(program)