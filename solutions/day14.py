from collections import namedtuple
from typing import List
from math import ceil

Chemical = namedtuple('Chemical', 'output, components')
Component = namedtuple('Component', 'count, chemical')

def get_reactions(chemical, amount, cookbook, reaction_list, waste):
    recipe = cookbook[chemical]
    multiplier = ceil(amount/recipe[0])
    if chemical not in waste:
        waste[chemical] = 0
    waste[chemical] += recipe[0] % amount
    reactions = []
    for reaction in recipe[1]:
        if waste[chemical] >= reaction[1] * multiplier:
            waste[chemical] -= reaction[1] * multiplier
        else:
            reactions.append((reaction[0], reaction[1] * multiplier))
    for r, a in reactions:
        if r != 'ORE':
            get_reactions(r, a, cookbook, reaction_list, waste)
    reaction_list += reactions

def create_cookbook(input: str):
    lines = input.splitlines()
    result = {}
    for line in lines:
        input, output = line.split('=>')
        components = [i for i in input.split(',')]
        components = [c.strip().split(' ') for c in components]
        components = [(c[1], int(c[0])) for c in components]
        amount, chemical = output.strip().split(' ')
        result[chemical] = (int(amount), components)
    return result