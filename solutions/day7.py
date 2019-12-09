from typing import List
from math import floor
from itertools import permutations
from solutions.Intcode import Intcode

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