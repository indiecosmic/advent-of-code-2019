def create_wires(paths):
    x = 0
    y = 0
    wires = [(x,y)]
    for path in paths:
        direction = path[0]
        length = int(path[1:])
        if (direction == 'U'):
            y -= length
        elif (direction == 'D'):
            y += length
        elif (direction == 'L'):
            x -= length
        else:
            x += length
        wires.append((x,y))
    return wires
if __name__ == '__main__':
    """with open('day2.txt') as f:
        contents = f.read()
        programs = contents.strip().split(',')
        programs = list(map(int, programs))
        print(part1(programs)[0])
        print(part2(programs))"""
    path = 'R8,U5,L5,D3'.split(',')
    print(create_wires(path))