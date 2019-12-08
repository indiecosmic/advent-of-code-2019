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

def merge_layers(layers, width, height):
    res = []
    for rownum in range(height):
        row = ''
        for colnum in range(width):
            for layernum in range(len(layers)):
                current = layers[layernum][rownum][colnum]
                if current in ['0','1']:
                    row += current
                    break
        res.append(row)
    return res

def part1(layers):
    min = maxsize
    res = []
    for layer in layers:
        occ = count_occurences('0', layer)
        if (occ < min):
            min = occ
            res = layer
    return count_occurences('1', res) * count_occurences('2', res)

def part2(layers, width, height):
    merged = merge_layers(layers, width, height)
    res = ''
    for row in merged:
        res += row.replace('0', ' ') + '\n'
    return res

if __name__ == "__main__":
    with open('day8.txt') as f:
        contents = f.read()
        layers = create_layers(contents, 25, 6)
        print(part1(layers))
        print(part2(layers, 25, 6))