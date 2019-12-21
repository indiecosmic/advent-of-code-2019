from solutions.day20 import create_map
from solutions.day20 import get_start_and_finish
from solutions.day20 import shortest_path
from solutions.day20 import Type

simple_maze = [
    '         A           ',
    '         A           ',
    '  #######.#########  ',
    '  #######.........#  ',
    '  #######.#######.#  ',
    '  #######.#######.#  ',
    '  #######.#######.#  ',
    '  #####  B    ###.#  ',
    'BC...##  C    ###.#  ',
    '  ##.##       ###.#  ',
    '  ##...DE  F  ###.#  ',
    '  #####    G  ###.#  ',
    '  #########.#####.#  ',
    'DE..#######...###.#  ',
    '  #.#########.###.#  ',
    'FG..#########.....#  ',
    '  ###########.#####  ',
    '             Z       ',
    '             Z       '
]

recursive_maze = [
    '             Z L X W       C                 ',
    '             Z P Q B       K                 ',
    '  ###########.#.#.#.#######.###############  ',
    '  #...#.......#.#.......#.#.......#.#.#...#  ',
    '  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  ',
    '  #.#...#.#.#...#.#.#...#...#...#.#.......#  ',
    '  #.###.#######.###.###.#.###.###.#.#######  ',
    '  #...#.......#.#...#...#.............#...#  ',
    '  #.#########.#######.#.#######.#######.###  ',
    '  #...#.#    F       R I       Z    #.#.#.#  ',
    '  #.###.#    D       E C       H    #.#.#.#  ',
    '  #.#...#                           #...#.#  ',
    '  #.###.#                           #.###.#  ',
    '  #.#....OA                       WB..#.#..ZH',
    '  #.###.#                           #.#.#.#  ',
    'CJ......#                           #.....#  ',
    '  #######                           #######  ',
    '  #.#....CK                         #......IC',
    '  #.###.#                           #.###.#  ',
    '  #.....#                           #...#.#  ',
    '  ###.###                           #.#.#.#  ',
    'XF....#.#                         RF..#.#.#  ',
    '  #####.#                           #######  ',
    '  #......CJ                       NM..#...#  ',
    '  ###.#.#                           #.###.#  ',
    'RE....#.#                           #......RF',
    '  ###.###        X   X       L      #.#.#.#  ',
    '  #.....#        F   Q       P      #.#.#.#  ',
    '  ###.###########.###.#######.#########.###  ',
    '  #.....#...#.....#.......#...#.....#.#...#  ',
    '  #####.#.###.#######.#######.###.###.#.#.#  ',
    '  #.......#.......#.#.#.#.#...#...#...#.#.#  ',
    '  #####.###.#####.#.#.#.#.###.###.#.###.###  ',
    '  #.......#.....#.#...#...............#...#  ',
    '  #############.#.#.###.###################  ',
    '               A O F   N                     ',
    '               A A D   M                     '
]


def test_create_map():
    puzzle_map = create_map(simple_maze)
    start, finish = get_start_and_finish(puzzle_map)
    assert start == (9, 2)
    assert finish == (13, 16)
    assert puzzle_map[(1, 8)].target_pos == (9, 6)


def test_shortest_path():
    puzzle_map = create_map(simple_maze)
    start, finish = get_start_and_finish(puzzle_map)
    assert shortest_path(start, finish, puzzle_map) == 23


def test_create_recursive_map():
    puzzle_map = create_map(recursive_maze)
    start, finish = get_start_and_finish(puzzle_map)
    fx_portals = [v for k,v in puzzle_map.items() if v.type == Type.PORTAL and v.portal_name == 'FX']
    ck_portals = [v for k,v in puzzle_map.items() if v.type == Type.PORTAL and v.portal_name == 'CK']
    hz_portals = [v for k,v in puzzle_map.items() if v.type == Type.PORTAL and v.portal_name == 'HZ']
    assert fx_portals[0].inner == False
    assert fx_portals[1].inner == True
    assert ck_portals[0].inner == False
    assert ck_portals[1].inner == True
    assert hz_portals[0].inner == True
    assert hz_portals[1].inner == False
    assert start == (15, len(recursive_maze) - 3)
    assert finish == (13, 2)
