import os
from typing import List


def create_input_signal(input: str):
    return list(map(int, [s for s in input]))


def calculate_signal(input_signal: List[int], times):
    patterns = create_patterns(len(input_signal))
    inp = input_signal
    for _ in range(times):
        result = []
        for phase in range(len(inp)):
            value = 0
            for n, p in zip(inp, patterns[phase]):
                value += n*p
            result.append(abs(value) % 10)
        inp = result
    return inp

def create_patterns(length: int):
    base_pattern = [0, 1, 0, -1]
    patterns = []
    for repeats in range(1, length + 1):
        pattern = []
        for n in base_pattern:
            pattern.extend([n]*repeats)
        while len(pattern) < length + 1:
            pattern += pattern
        patterns.append(pattern[1:length + 1])
    return patterns

def get_input():
    file_path = os.path.join(os.path.dirname(__file__), 'day16.txt')
    with open(file_path) as f:
        contents = f.read()
        return contents.strip()

def part1():
    numbers = get_input()
    signal = create_input_signal(numbers)
    result = calculate_signal(signal, 100)
    print(result[:8])

def part2():
    pass

def main():
    part1()
    part2()
