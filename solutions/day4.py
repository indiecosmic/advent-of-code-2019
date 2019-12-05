from math import floor
from collections import defaultdict

def increasing(value:int):
    hundred_thousand = floor(value//100000)
    ten_thousand = floor(value//10000) % 10
    if (ten_thousand < hundred_thousand):
        return False
    thousand = floor(value//1000) % 10
    if (thousand < ten_thousand):
        return False
    hundred = floor(value//100) % 10
    if (hundred < thousand):
        return False
    ten = floor(value//10) % 10
    if (ten < hundred):
        return False
    one = value % 10
    if (one < ten):
        return False
    return True

def contains_doubles(value:int):
    hundred_thousand = floor(value//100000)
    ten_thousand = floor(value//10000) % 10
    if (hundred_thousand == ten_thousand):
        return True
    thousand = floor(value//1000) % 10
    if (thousand == ten_thousand):
        return True
    hundred = floor(value//100) % 10
    if (hundred == thousand):
        return True
    ten = floor(value//10) % 10
    if (ten == hundred):
        return True
    one = value % 10
    if (one == ten):
        return True
    return False

def contains_strict_double(value:int):
    numbers = str(value)
    doubles = defaultdict(lambda:0, {})
    for index, number in enumerate(numbers):
        if (index == 5):
            break
        if (number == numbers[index+1]):
            doubles[number] += 1
    return 1 in doubles.values()

def part1():
    numbers = range(171309,643604)
    numbers = filter(increasing, numbers)
    numbers = filter(contains_doubles, numbers)
    return len(list(numbers))

def part2():
    numbers = range(171309,643604)
    numbers = filter(increasing, numbers)
    numbers = filter(contains_doubles, numbers)
    numbers = filter(contains_strict_double, numbers)
    return len(list(numbers))

if __name__ == '__main__':
    print(part1())
    print(part2())
