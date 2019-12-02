def run_programs(programs):
    for i in range(0, len(programs), 4):
        opcode = programs[i]
        if (opcode == 99):
            break
        pos1 = programs[i+1]
        pos2 = programs[i+2]
        target = programs[i+3]
        if (opcode == 1):           
            programs[target] = programs[pos1] + programs[pos2]
        elif (opcode == 2):
            programs[target] = programs[pos1] * programs[pos2]
        else:
            raise Exception('invalid opcode: {}'.format(opcode))
    return programs

def restore_and_run_programs(noun, verb, programs):
    input = programs.copy()
    input[1] = noun
    input[2] = verb
    return run_programs(input)

def part1(programs):
    return restore_and_run_programs(12, 2, programs)

def part2(programs):
    for noun in range(0, 100, 1):
        for verb in range(0, 100, 1):
            if restore_and_run_programs(noun, verb, programs)[0] == 19690720:
                return (noun, verb)

if __name__ == '__main__':
    with open('day2.txt') as f:
        contents = f.read()
        programs = contents.strip().split(',')
        programs = list(map(int, programs))
        print(part1(programs)[0])
        print(part2(programs))