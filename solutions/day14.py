import os
from collections import namedtuple
from typing import List
from math import ceil


Chemical = namedtuple('Chemical', 'output, components')
Component = namedtuple('Component', 'count, chemical')

def get_needed_ingredients(chemical, amount, cookbook, required):
    if chemical not in cookbook:
        return
    if chemical not in required:
        required[chemical] = amount
    else:
        required[chemical] += amount
    recipe = cookbook[chemical]
    multiplier = ceil(amount/recipe.output)
    for component in recipe.components:
        get_needed_ingredients(component.chemical, component.count * multiplier, cookbook, required)

def get_needed_ore(required, cookbook):
    sum = 0
    for c, a in required.items():
        recipe = cookbook[c]
        for comp in recipe.components:
            if comp.chemical == 'ORE':
                sum += (ceil(a/recipe.output) * comp.count)
    return sum

def get_reactions(chemical, amount, cookbook, store = {}):
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
        component_reqs = get_reactions(component.chemical, component.count * multiplier, cookbook, store)
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
        components = [Component(int(c[0]),c[1]) for c in components]
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

def main():
    input = get_input()
    print(part1(input))

if __name__ == "__main__":
    main()