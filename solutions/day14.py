import os
from collections import namedtuple
from typing import List
from math import ceil


Chemical = namedtuple('Chemical', 'output, components')
Component = namedtuple('Component', 'count, chemical')


def get_reactions(chemical, amount, cookbook, store={}):
    if chemical in store:
        if store[chemical] >= amount:
            store[chemical] -= amount
            return {}
        else:
            amount -= store[chemical]
            store[chemical] = 0

    if chemical not in cookbook:
        return {chemical: amount}

    needed = {}
    recipe = cookbook[chemical]
    multiplier = ceil(amount/recipe.output)
    for component in recipe.components:
        component_reqs = get_reactions(
            component.chemical, component.count * multiplier, cookbook, store)
        for c in component_reqs:
            if c in needed:
                needed[c] += component_reqs[c]
            else:
                needed[c] = component_reqs[c]
    if chemical not in store:
        store[chemical] = recipe.output * multiplier
        store[chemical] -= amount
    else:
        store[chemical] += recipe.output * multiplier - amount
    return needed


def create_cookbook(input: str):
    lines = input.splitlines()
    result = {}
    for line in lines:
        input, output = line.split('=>')
        components = [i for i in input.split(',')]
        components = [c.strip().split(' ') for c in components]
        components = [Component(int(c[0]), c[1]) for c in components]
        amount, chemical = output.strip().split(' ')
        result[chemical] = Chemical(int(amount), components)
    return result


def get_input():
    file_path = os.path.join(os.path.dirname(__file__), 'day14.txt')
    with open(file_path) as f:
        contents = f.read()
        return contents


def part1(input: str):
    cookbook = create_cookbook(input)
    needed = get_reactions('FUEL', 1, cookbook)
    return needed['ORE']


def part2(input: str):
    cookbook = create_cookbook(input)
    ore = 1000000000000
    store = {}
    fuels = 0
    while True:
        needed = get_reactions('FUEL', 1, cookbook, store)
        ore -= needed['ORE']
        if fuels % 10000 == 0:
            print(ore)
        if ore < 0:
            break
        fuels += 1
    return fuels


def main():
    input = get_input()
    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()
