from math import floor
from typing import List
from collections import defaultdict

class Intcode:
    def __init__(self, instructions: List[int], inputs: List[int]):
        self.memory = defaultdict(lambda: 0, enumerate(instructions))
        self.ptr = 0
        self.inputs = inputs
        self.outputs = []
        self.current_input = 0
        self.current_output = 0
        self.halted = False
        self.stopped = False
        self.relative_base = 0

    def get_opcode(self):
        return self.memory[self.ptr] % 100

    def get_mode(self):
        value = self.memory[self.ptr]
        return (floor(value//100) % 10, floor(value//1000) % 10, floor(value//10000) % 10)

    def get_values(self, modes):
        val1 = self.get_value(self.ptr + 1, modes[0])
        val2 = self.get_value(self.ptr + 2, modes[1])
        target = self.get_value(self.ptr + 3, 1)
        return (val1, val2, target)

    def get_value(self, index, mode):
        if mode == 0:
            pos = self.memory[index]
            return self.memory[pos]
        elif mode == 1:
            return self.memory[index]
        elif mode == 2:
            pos = self.memory[index] + self.relative_base
            return self.memory[pos]
        else:
            raise Exception('invalid mode: {}'.format(mode))

    def get_input(self):
        if self.current_input >= len(self.inputs):
            raise Exception('Waiting for input')
        input = self.inputs[self.current_input]
        self.current_input += 1
        return input
    
    def get_output(self):
        if self.current_output >= len(self.outputs):
            raise Exception('Out of output bounds')
        output = self.outputs[self.current_output]
        self.current_output += 1
        return output

    def should_wait_for_input(self):
        return True if self.current_input >= len(self.inputs) else False

    def set_output(self, value):
        self.outputs.append(value)
    
    def set_input(self, value):
        if type(value) is list:
            self.inputs += value
        else:
            self.inputs.append(value)

    def set_value(self, index, mode, value):
        if mode == 0:
            pos = self.memory[index]
            self.memory[pos] = value
        elif mode == 2:
            pos = self.memory[index] + self.relative_base
            self.memory[pos] = value
        else:
            raise Exception('invalid mode: {}'.format(mode))

    def run_opcode(self):
        op = self.get_opcode()
        mode = self.get_mode()
        if (op == 99):
            return None
        if (op == 1):
            values = self.get_values(mode)
            self.set_value(self.ptr + 3, mode[2], values[0] + values[1])
            return self.ptr + 4
        elif (op == 2):
            values = self.get_values(mode)
            self.set_value(self.ptr + 3, mode[2], values[0] * values[1])
            return self.ptr + 4
        elif (op == 3):
            input = self.get_input()
            self.set_value(self.ptr + 1, mode[0], input)
            return self.ptr + 2
        elif op == 4:
            value = self.get_value(self.ptr + 1, mode[0])
            self.set_output(value)
            return self.ptr + 2
        elif op == 5:
            param1 = self.get_value(self.ptr + 1, mode[0])
            if param1 != 0:
                return self.get_value(self.ptr + 2, mode[1])
            return self.ptr + 3
        elif op == 6:
            param1 = self.get_value(self.ptr + 1, mode[0])
            if param1 == 0:
                return self.get_value(self.ptr + 2, mode[1])
            return self.ptr + 3
        elif op == 7:
            values = self.get_values(mode)
            value = 1 if values[0] < values[1] else 0
            self.set_value(self.ptr + 3, mode[2], value)
            return self.ptr + 4
        elif op == 8:
            values = self.get_values(mode)
            value = 1 if values[0] == values[1] else 0
            self.set_value(self.ptr + 3, mode[2], value)
            return self.ptr + 4
        elif op == 9:
            param1 = self.get_value(self.ptr + 1, mode[0])
            self.relative_base += param1
            return self.ptr + 2
        else:
            raise Exception('invalid opcode: {}'.format(op))

    def run_program(self):
        self.outputs = []
        self.current_output = 0
        self.halted = False
        while True :
            op = self.get_opcode()
            if op == 99:
                self.stopped = True
                break
            if op == 3 and self.should_wait_for_input():
                self.halted = True
                break
            self.ptr = self.run_opcode()