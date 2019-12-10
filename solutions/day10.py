from typing import List

def parse_map(input: str):
    return input.split('\n')

def find_coordinates(map: List[str]):
    coordinates = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == '#':
                coordinates.append((x,y))
    return coordinates

def find_visible(position, coordinates):
    return []

def can_detect(position, target, asteroids):
    return False