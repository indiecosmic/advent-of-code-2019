import os
from common.Intcode import Intcode
from common.Point import Point

def part1(instructions):
    intcode = Intcode(instructions, [0], True)
    pos = Point(0,0)
    dir = Point(0,1)
    panels = {}
    while not intcode.stopped:
        intcode.run_program()
        color = intcode.get_output()
        panels[pos] = color
        turn = intcode.get_output()
        dir = Point(-dir.y, dir.x) if turn == 0 else Point(dir.y, -dir.x)
        pos = Point(pos.x + dir.x, pos.y + dir.y)
        if pos in panels:
            intcode.set_input(panels[pos])
        else:
            intcode.set_input(0)
    return len(panels)

def part2(instructions):
    intcode = Intcode(instructions, [1], True)
    pos = Point(0,0)
    dir = Point(0,1)
    panels = {}
    while not intcode.stopped:
        intcode.run_program()
        color = intcode.get_output()
        panels[pos] = color
        turn = intcode.get_output()
        dir = Point(-dir.y, dir.x) if turn == 0 else Point(dir.y, -dir.x)
        pos = Point(pos.x + dir.x, pos.y + dir.y)
        if pos in panels:
            intcode.set_input(panels[pos])
        else:
            intcode.set_input(0)

    xmin,ymin,xmax,ymax = 0,0,0,0
    for point in panels:
        if point.x < xmin:
            xmin = point.x
        if point.x > xmax:
            xmax = point.x
        if point.y < ymin:
            ymin = point.y
        if point.y > ymax:
            ymax = point.y

    for y in range(ymax+1, ymin-1, -1):
        row = ''
        for x in range(xmin-1, xmax+1):
            pos = Point(x,y)
            if pos in panels:
                row += ' ' if panels[pos] == 0 else '1'
            else:
                row += ' '
        print(row)




def main():
    path = os.path.join(os.path.dirname(__file__), 'day11.txt')
    with open(path) as f:
        contents = f.read()
        program_str = contents.strip().split(',')
        instructions = list(map(int, program_str))
        print(part1(instructions))
        part2(instructions)

if __name__ == "__main__":
    main()