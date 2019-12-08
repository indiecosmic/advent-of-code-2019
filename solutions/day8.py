from typing import List
from sys import maxsize

def create_layers(numbers:str, width:int, height:int):
    layers = []
    rows = []
    row = ''
    for _,number in enumerate(numbers):
        row += number
        if len(row) == width:
            rows.append(row)
            row = ''
            if len(rows) == height:
                layers.append(rows)
                rows = []
    return layers

def count_occurences(value:str, layer:List[str]):
    return sum([row.count(value) for row in layer])

def part1(layers):
    min = maxsize
    res = []
    for layer in layers:
        occ = count_occurences('0', layer)
        if (occ < min):
            min = occ
            res = layer
    return count_occurences('1', res) * count_occurences('2', res)

if __name__ == "__main__":
    with open('day8.txt') as f:
        contents = f.read()
        layers = create_layers(contents, 25, 6)
        print(part1(layers))