from typing import List
from math import floor
from itertools import permutations

class Intcode:
    def __init__(self, instructions: List[int], inputs: List[int]):
        self.instructions = instructions.copy()
        self.current_instruction = 0
        self.inputs = inputs
        self.outputs = []
        self.current_input = 0
        self.halted = False
        self.stopped = False

    def get_opcode(self, value:int):
        return int(str(value)[-2:])

    def get_mode(self, value:int):
        return (floor(value//100) % 10, floor(value//1000) % 10, floor(value//10000) % 10)

    def get_values(self, index, modes, instructions: List[int]):
        pos1 = instructions[index+1]
        pos2 = instructions[index+2]
        target = instructions[index+3]
        val1 = instructions[pos1] if modes[0] == 0 else pos1
        val2 = instructions[pos2] if modes[1] == 0 else pos2
        return (val1, val2, target)

    def get_value(self, index, mode, instructions):
        pos = instructions[index]
        return instructions[pos] if mode == 0 else pos
    
    def get_input(self):
        if self.current_input >= len(self.inputs):
            raise Exception('Waiting for input')
        input = self.inputs[self.current_input]
        self.current_input += 1
        return input

    def should_wait_for_input(self):
        return True if self.current_input >= len(self.inputs) else False

    def set_output(self, value):
        self.outputs.append(value)
    
    def set_input(self, value):
        self.inputs += value

    def run_opcode(self, index:int, instructions: List[int]):
        op = self.get_opcode(instructions[index])
        m = self.get_mode(instructions[index])
        if (op == 99):
            return None
        if (op == 1):
            values = self.get_values(index, m, instructions)
            instructions[values[2]] = values[0] + values[1]
            return index + 4
        elif (op == 2):
            values = self.get_values(index, m, instructions)
            instructions[values[2]] = values[0] * values[1]
            return index + 4
        elif (op == 3):
            target = instructions[index+1]
            instructions[target] = self.get_input()
            return index + 2
        elif op == 4:
            value = self.get_value(index + 1, m[0], instructions)
            self.set_output(value)
            return index + 2
        elif op == 5:
            param1 = self.get_value(index + 1, m[0], instructions)
            if param1 != 0:
                return self.get_value(index + 2, m[1], instructions)
            return index + 3
        elif op == 6:
            param1 = self.get_value(index + 1, m[0], instructions)
            if param1 == 0:
                return self.get_value(index + 2, m[1], instructions)
            return index + 3
        elif op == 7:
            values = self.get_values(index, m, instructions)
            instructions[values[2]] = 1 if values[0] < values[1] else 0
            return index + 4
        elif op == 8:
            values = self.get_values(index, m, instructions)
            instructions[values[2]] = 1 if values[0] == values[1] else 0
            return index + 4
        else:
            raise Exception('invalid opcode: {}'.format(op))

    def run_program(self):
        self.outputs = []
        self.halted = False
        while self.current_instruction < len(self.instructions):
            op = self.get_opcode(self.instructions[self.current_instruction])
            if op == 99:
                self.stopped = True
                break
            if op == 3 and self.should_wait_for_input():
                self.halted = True
                break
            self.current_instruction = self.run_opcode(self.current_instruction, self.instructions)

def create_phase_settings(phase_settings):
    return permutations(phase_settings)

def run_program_sequence(instructions: List[int], phase_settings):
    input = 0
    for setting in phase_settings:
        amp = Intcode(instructions, [setting, input])
        amp.run_program()
        input = amp.outputs[0]
    return input

def run_feedback_sequence(instructions: List[int], phase_settings):
    input = [0]
    amplifiers = []
    for setting in phase_settings:
        amp = Intcode(instructions, [setting])
        amplifiers.append(amp)
    index = 0
    while not amplifiers[-1].stopped:
        amplifiers[index].set_input(input)
        amplifiers[index].run_program()
        input = amplifiers[index].outputs
        index += 1
        if index > 4:
            index = 0
    return amplifiers[-1].outputs[0]

def run_combinations(instructions: List[int], phase_settings: List[int]):
    combinations = create_phase_settings(phase_settings)
    max = 0
    best_combination = ()
    for combination in combinations:
        result = run_program_sequence(instructions, combination)
        if result > max:
            max = result
            best_combination = combination
    return (max, best_combination)

def run_feedback_combinations(instructions: List[int], phase_settings: List[int]):
    combinations = create_phase_settings(phase_settings)
    max = 0
    for combination in combinations:
        result = run_feedback_sequence(instructions, combination)
        max = result if result > max else max
    return max

def part1(instructions):
    phase_settings = [0,1,2,3,4]
    result = run_combinations(instructions, phase_settings)
    return result

def part2(instructions):
    phase_settings = [5,6,7,8,9]
    result = run_feedback_combinations(instructions, phase_settings)
    return result

if __name__ == '__main__':
    with open('day7.txt') as f:
        contents = f.read()
        program_str = contents.strip().split(',')
        instructions = list(map(int, program_str))
        print(part1(instructions))
        print(part2(instructions))