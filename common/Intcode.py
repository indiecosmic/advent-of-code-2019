from math import floor
from typing import List

class Intcode:
    def __init__(self, instructions: List[int], inputs: List[int], allow_grow: bool = False):
        self.instructions = instructions.copy()
        self.current_instruction = 0
        self.inputs = inputs
        self.outputs = []
        self.current_input = 0
        self.halted = False
        self.stopped = False
        self.relative_base = 0
        self.allow_grow = allow_grow

    def get_opcode(self, value:int):
        return int(str(value)[-2:])

    def get_mode(self, value:int):
        return (floor(value//100) % 10, floor(value//1000) % 10, floor(value//10000) % 10)

    def extend(self, index, instructions):
        if not self.allow_grow:
            return
        if (index >= len(instructions)):
                instructions.extend([0]*(index + 1 - len(instructions)))

    def get_values(self, index, modes, instructions: List[int]):
        val1 = self.get_value(index + 1, modes[0], instructions)
        val2 = self.get_value(index + 2, modes[1], instructions)
        target = self.get_value(index + 3, 1, instructions)
        return (val1, val2, target)

    def get_value(self, index, mode, instructions):
        if mode == 0:
            pos = instructions[index]
            self.extend(pos, instructions)
            return instructions[pos]
        elif mode == 1:
            self.extend(index, instructions)
            return instructions[index]
        elif mode == 2:
            pos = instructions[index] + self.relative_base
            self.extend(pos, instructions)
            return instructions[pos]
        else:
            raise Exception('invalid mode: {}'.format(mode))

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

    def set_value(self, index, mode, instructions, value):
        if mode == 0:
            pos = instructions[index]
            self.extend(pos, instructions)
            instructions[pos] = value
        elif mode == 2:
            pos = instructions[index] + self.relative_base
            self.extend(pos, instructions)
            instructions[pos] = value
        else:
            raise Exception('invalid mode: {}'.format(mode))

    def run_opcode(self, index:int, instructions: List[int]):
        op = self.get_opcode(instructions[index])
        m = self.get_mode(instructions[index])
        if (op == 99):
            return None
        if (op == 1):
            values = self.get_values(index, m, instructions)
            self.set_value(index + 3, m[2], instructions, values[0] + values[1])
            return index + 4
        elif (op == 2):
            values = self.get_values(index, m, instructions)
            self.extend(values[0], instructions)
            self.extend(values[1], instructions)
            self.extend(values[2], instructions)
            self.set_value(index + 3, m[2], instructions, values[0] * values[1])
            return index + 4
        elif (op == 3):
            input = self.get_input()
            self.set_value(index + 1, m[0], instructions, input)
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
            value = 1 if values[0] < values[1] else 0
            self.set_value(index + 3, m[2], instructions, value)
            return index + 4
        elif op == 8:
            values = self.get_values(index, m, instructions)
            self.extend(values[2], instructions)
            value = 1 if values[0] == values[1] else 0
            self.set_value(index + 3, m[2], instructions, value)
            return index + 4
        elif op == 9:
            param1 = self.get_value(index + 1, m[0], instructions)
            self.relative_base += param1
            return index + 2
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