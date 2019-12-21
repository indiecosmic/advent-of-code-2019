from solutions.day20 import create_map
from solutions.day20 import get_start_and_finish
from solutions.day20 import shortest_path


def test_create_map():
    input = [
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
    puzzle_map = create_map(input)
    start, finish = get_start_and_finish(puzzle_map)
    assert start == (9, 2)
    assert finish == (13, 16)
    assert puzzle_map[(1, 8)].target_pos == (9, 6)


def test_shortest_path():
    input = [
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
    puzzle_map = create_map(input)
    start, finish = get_start_and_finish(puzzle_map)
    assert shortest_path(start, finish, puzzle_map) == 23
