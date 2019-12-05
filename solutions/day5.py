from typing import List
from math import floor

def opcode(value:int):
    return value % 10

def mode(value:int):
    return (floor(value//100) % 10, floor(value//1000) % 10, floor(value//10000) % 10)

def run_opcode(index:int, instructions: List[int]):
    op = opcode(instructions[index])
    if (op == 99):
        return
    pos1 = instructions[index+1]
    pos2 = instructions[index+2]
    target = instructions[index+3]
    if (op == 1):           
        instructions[target] = instructions[pos1] + instructions[pos2]
    elif (op == 2):
        instructions[target] = instructions[pos1] * instructions[pos2]
    elif (op == 3):
        parameter = instructions[index+1]
        
    else:
        raise Exception('invalid opcode: {}'.format(opcode))