from typing import List
from math import floor

def opcode(value:int):
    return int(str(value)[-2:])

def mode(value:int):
    return (floor(value//100) % 10, floor(value//1000) % 10, floor(value//10000) % 10)

def run_opcode(index:int, instructions: List[int], input: int = 1):
    op = opcode(instructions[index])
    m = mode(instructions[index])
    if (op == 99):
        return instructions
    if (op == 1):
        pos1 = instructions[index+1]
        pos2 = instructions[index+2]
        target = instructions[index+3]
        val1 = instructions[pos1] if m[0] == 0 else pos1
        val2 = instructions[pos2] if m[1] == 0 else pos2
        instructions[target] = val1 + val2
        return instructions
    elif (op == 2):
        pos1 = instructions[index+1]
        pos2 = instructions[index+2]
        target = instructions[index+3]
        val1 = instructions[pos1] if m[0] == 0 else pos1
        val2 = instructions[pos2] if m[1] == 0 else pos2
        instructions[target] = val1 * val2
        return instructions
    elif (op == 3):
        target = instructions[index+1]
        instructions[target] = input
        return instructions
    elif op == 4:
        target = instructions[index+1]
        print(instructions[target])
        return instructions
    else:
        raise Exception('invalid opcode: {}'.format(op))
    return instructions

def part1(program):
    index = 0
    while index < len(program):
        op = opcode(program[index])
        if op == 99:
            break
        program = run_opcode(index, program)
        if op == 1 or op == 2:
            index += 4
        else:
            index += 2

if __name__ == '__main__':
    with open('day5.txt') as f:
        contents = f.read()
        program = contents.strip().split(',')
        program = list(map(int, program))
        part1(program)