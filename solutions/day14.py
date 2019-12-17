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

def get_reactions(chemical, amount, cookbook, reaction_list, waste):
    if chemical in waste:
        if waste[chemical] >= amount:
            waste[chemical] -= amount
            return
        else:
            amount -= waste[chemical]
            waste[chemical] = 0
    else:
        waste[chemical] = 0

    if chemical not in cookbook:
        waste[chemical] += amount
        reaction_list.append(amount)
        return
    recipe = cookbook[chemical]
    multiplier = ceil(amount/recipe.output)

    waste[chemical] += recipe.output % amount
    for component in recipe.components:
        get_reactions(component.chemical, component.count * multiplier, cookbook, reaction_list, waste)

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
    required = {}
    get_needed_ingredients('FUEL', 1, cookbook, required)
    return get_needed_ore(required, cookbook)

def main():
    input = get_input()
    print(part1(input))

if __name__ == "__main__":
    main()