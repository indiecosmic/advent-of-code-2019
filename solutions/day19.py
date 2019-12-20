import os
from common.Intcode import Intcode
from common.Point import Point


def render(map):
    x_min = min([key.x for key in map])
    x_max = max([key.x for key in map])
    y_min = min([key.y for key in map])
    y_max = max([key.y for key in map])
    for y in range(y_min, y_max + 1):
        row = ''
        for x in range(x_min, x_max + 1):
            row += '#' if map[(x, y)] == 1 else '.'
        print(row)


def create_map(instructions, height, width, xs = 0, ys = 0):
    map = {}
    for y in range(ys, ys + height):
        for x in range(xs, xs + width):
            computer = Intcode(instructions, [x, y])
            computer.run_program()
            map[Point(x, y)] = computer.get_output()
    return map


def get_input():
    file_path = os.path.join(os.path.dirname(__file__), 'day19.txt')
    with open(file_path) as f:
        contents = f.read()
        program_str = contents.strip().split(',')
        instructions = list(map(int, program_str))
        return instructions


def get_beam_width(instructions, y, start_x_at=0):
    x = start_x_at
    start_pos = 0
    end_pos = 0
    while True:
        computer = Intcode(instructions, [x, y])
        computer.run_program()
        output = computer.get_output()
        if start_pos == 0 and output == 1:
            start_pos = x
        elif output == 1:
            end_pos = x
        if end_pos != 0 and output == 0:
            break
        x += 1
    return (end_pos - start_pos, start_pos, end_pos)


def get_beam_height(instructions, x):
    y = 0
    start_pos = 0
    end_pos = 0
    while True:
        computer = Intcode(instructions, [x, y])
        computer.run_program()
        output = computer.get_output()
        if start_pos == 0 and output == 1:
            start_pos = y
        elif output == 1:
            end_pos = y
        if end_pos != 0 and output == 0:
            break
        y += 1
    return (end_pos - start_pos, start_pos, end_pos)


def can_fit_square(instructions, lower_left: Point, upper_right: Point):
    if get_value(instructions, lower_left.x, lower_left.y) == 0:
        return False
    if get_value(instructions, upper_right.x, upper_right.y) == 0:
        return False
    return True


def get_value(instructions, x, y):
    computer = Intcode(instructions, [x, y])
    computer.run_program()
    return computer.get_output()


def part1(map):
    count = sum([v for k, v in map.items() if v == 1])
    print(count)


def part2(instructions):
    lower_limit = 0
    upper_limit = 0
    beam_start_x = 0
    y = 500
    while True:
        beam_width, beam_start_x, beam_end_x = get_beam_width(instructions, y, beam_start_x - 5)
        can_fit = can_fit_square(instructions, Point(beam_end_x - 99, y + 99), Point(beam_end_x, y))
        print('{0}-{1}:{2} w:{3}'.format(Point(beam_end_x-99, y), Point(beam_end_x, y + 99), can_fit, beam_width))
        if not can_fit:
            lower_limit=y
            y += 100
        else:
            upper_limit=y
            break
    y=lower_limit + (upper_limit - lower_limit) // 2
    while upper_limit - lower_limit > 1:
        beam_width, beam_start_x, beam_end_x = get_beam_width(instructions, y, beam_start_x - 50)
        can_fit = can_fit_square(instructions, Point(beam_end_x - 99, y + 99), Point(beam_end_x, y))
        print('Testing at {0}: {1} (lower {2} upper {3})'.format(y, can_fit, lower_limit, upper_limit))
        if can_fit:
            upper_limit=y
        else:
            lower_limit=y
        y=lower_limit + (upper_limit - lower_limit) // 2
    beam_width, beam_start_x, beam_end_x = get_beam_width(instructions, upper_limit, beam_start_x - 5)
    x_start = beam_end_x - 99
    target=Point(x_start, upper_limit)
    print(target.x * 10000 + target.y)


if __name__ == "__main__":
    instructions=get_input()
    map = create_map(instructions, 50, 50)
    part1(map)
    part2(instructions)
    
