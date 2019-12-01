def fuel_requirement(mass):
    return (mass // 3) - 2

def fuel_requirement_r(mass):
    fuel = fuel_requirement(mass)
    if (fuel <= 0):
        return 0
    return fuel + fuel_requirement_r(fuel)

def part1(lines):
    numbers = list(map(int, lines))
    return sum(map(fuel_requirement, numbers))

def part2(lines):
    numbers = list(map(int, lines))
    return sum(map(fuel_requirement_r, numbers))

if __name__ == '__main__':
    with open('day1.txt') as f:
        lines = [line.strip() for line in list(f)]
        print(part1(lines))
        print(part2(lines))

