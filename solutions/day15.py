import os
from sys import maxsize
from common.Intcode import Intcode
from common.Point import Point
import pickle

WALL = 0
PATH = 1
GOAL = 2
UNEXPLORED = -1

def render(state, pos):
    x_min = min([key.x for key in state])
    x_max = max([key.x for key in state])
    y_min = min([key.y for key in state])
    y_max = max([key.y for key in state])
    for y in range(y_min, y_max + 1):
        row = ''
        for x in range(x_min, x_max + 1):
            if (x,y) == pos:
                row += 'D'
            elif (x,y) not in state:
                row += ' '
            elif state[(x,y)] == 0:
                row += '#'
            elif state[(x,y)] == 1:
                row += '.'
            elif state[(x,y)] == 2:
                row += '★'
        print(row)

def get_target_pos(pos: Point, direction: int):
    if direction == 1:
        return Point(pos.x, pos.y - 1)
    elif direction == 2:
        return Point(pos.x, pos.y + 1)
    elif direction == 3:
        return Point(pos.x - 1, pos.y)
    else:
        return Point(pos.x + 1, pos.y)

def get_available_moves(pos: Point, map):
    moves = [1,2,3,4]
    options = []
    for direction in moves:
        target = get_target_pos(pos, direction)
        if target not in map:
            options.append(direction)
    return options

def get_connected_tiles(pos: Point, map):
    return [
        Point(pos.x, pos.y + 1),
        Point(pos.x, pos.y - 1),
        Point(pos.x + 1, pos.y),
        Point(pos.x - 1, pos.y)
    ]

def get_direction(pos: Point, target: Point):
    if target == (pos.x, pos.y + 1):
        return 1
    elif target == (pos.x, pos.y - 1):
        return 2
    elif target == (pos.x + 1, pos.y):
        return 4
    elif target == (pos.x - 1, pos.y):
        return 3
    else:
        raise Exception('Unknown path: {0}=>{1}'.format(pos, target))

def find_unexplored(map):
    unexplored = []
    for pos in map:
        if map[pos] == WALL:
            continue
        neighbours = get_connected_tiles(pos, map)
        for neighbour in neighbours:
            if neighbour not in map:
                unexplored.append(neighbour)
    return unexplored

def find_reachable(map):
    reachable = []
    for pos in map:
        if map[pos] == WALL:
            continue
        reachable.append(pos)
    return reachable

def reading_order(a:Point, b:Point):
    if a.y > b.y:
        return 1
    elif a.y < b.y:
        return -1
    elif a.x > b.x:
        return 1
    elif a.x < b.x:
        return -1
    return 0

def find_closest(distances, unexplored):
    min_distance = maxsize
    closest = None
    for u in unexplored:
        d = distances[u]
        if d < min_distance:
            min_distance = d
            closest = u
    return closest

def find_shortest_distance(origin, target, map):
    reachable = find_reachable(map)
    shortest_path_set = set([])
    origins = {}
    distances = {}
    for r in reachable:
        origins[r] = None
        distances[r] = maxsize
    distances[origin] = 0
    while len(shortest_path_set) < len(distances):
        selected_tile = None
        min_distance = maxsize
        tiles = set(distances.keys())-shortest_path_set
        for tile in tiles:
            distance = distances[tile]
            if distance < min_distance:
                min_distance = distance
                selected_tile = tile
        shortest_path_set.add(selected_tile)
        connected = get_connected_tiles(selected_tile, map)
        for c in connected:
            if c in distances and c not in shortest_path_set and distances[c] >= distances[selected_tile] + 1:
                if distances[c] > distances[selected_tile] + 1:
                    origins[c] = selected_tile
                    distances[c] = distances[selected_tile] + 1
                else:
                    if origins[c] == None:
                        origins[c] = selected_tile
                    elif reading_order(origins[c], selected_tile) > 0:
                        origins[c] = tile
    return distances[target]

def calculate_next_move(current_pos, map):
    unexplored = find_unexplored(map)
    reachable = find_reachable(map)
    shortest_path_set = set([])
    origins = {}
    distances = {}
    for r in reachable:
        origins[r] = None
        distances[r] = maxsize
    for u in unexplored:
        origins[u] = None
        distances[u] = maxsize
    distances[current_pos] = 0
    while len(shortest_path_set) < len(distances):
        selected_tile = None
        min_distance = maxsize
        tiles = set(distances.keys())-shortest_path_set
        for tile in tiles:
            distance = distances[tile]
            if distance < min_distance:
                min_distance = distance
                selected_tile = tile
        shortest_path_set.add(selected_tile)
        connected = get_connected_tiles(selected_tile, map)
        for c in connected:
            if c in distances and c not in shortest_path_set and distances[c] >= distances[selected_tile] + 1:
                if distances[c] > distances[selected_tile] + 1:
                    origins[c] = selected_tile
                    distances[c] = distances[selected_tile] + 1
                else:
                    if origins[c] == None:
                        origins[c] = selected_tile
                    elif reading_order(origins[c], selected_tile) > 0:
                        origins[c] = tile
    closest_unexplored = find_closest(distances, unexplored)
    if closest_unexplored == None:
        return None
    next_move = origins[closest_unexplored]
    previous = closest_unexplored
    while next_move != current_pos:
        previous = next_move
        next_move = origins[next_move]
    return previous

def fill_with_oxygen(map):
    done = set([])
    count = 0
    open_spaces = [key  for (key, value) in map.items() if value == PATH]
    while len(open_spaces) > 0:
        oxygen_tiles = [key  for (key, value) in map.items() if value == GOAL]
        oxygen_tiles = set(oxygen_tiles)-done
        for otile in oxygen_tiles:
            connected = get_connected_tiles(otile, map)
            for c in connected:
                if c in map and map[c] == PATH:
                    map[c] = GOAL
            done.add(otile)
        count += 1
        open_spaces = [key  for (key, value) in map.items() if value == PATH]
    return count

def explore_map(instructions):
    computer = Intcode(instructions, [])
    computer.run_program()
    pos = Point(0,0)
    map = {}
    map[pos] = 1
    while not computer.stopped:
        next = calculate_next_move(pos, map)
        if next == None:
            break
        direction = get_direction(pos, next)
        computer.set_input(direction)
        computer.run_program()
        output = computer.get_output()
        if output == 0:
            map[next] = 0
        elif output == 1:
            map[next] = 1
            pos = next
        elif output == 2:
            map[next] = 2
            pos = next
            print(find_shortest_distance((0,0), pos, map))
    print(fill_with_oxygen(map))

def get_input():
    file_path = os.path.join(os.path.dirname(__file__), 'day15.txt')
    with open(file_path) as f:
        contents = f.read()
        program_str = contents.strip().split(',')
        instructions = list(map(int, program_str))
        return instructions

def main():
    instructions = get_input()
    explore_map(instructions)

if __name__ == "__main__":
    main()