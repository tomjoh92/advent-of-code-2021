def read_file():
    f = open("day2_input.txt", "r")
    data = f.read().splitlines()
    f.close()
    # data = [int(x) for x in data]
    return data

def part_one(commands):
    pos_horizontal = 0
    pos_depth = 0
    for i in range(len(commands)):
        inst = commands[i].split()
        if inst[0] == "forward":
            pos_horizontal += int(inst[1])
        elif inst[0] == "down":
            pos_depth += int(inst[1])
        elif inst[0] == "up":
            pos_depth -= int(inst[1])

    print("Horizontal position :", pos_horizontal)
    print("Depth: ", pos_depth)

    return(pos_horizontal * pos_depth)

def part_two(commands):
    pos_horizontal = 0
    pos_depth = 0
    aim = 0
    for i in range(len(commands)):
        #print("aim: ", aim)
        inst = commands[i].split()
        if inst[0] == "forward":
            pos_horizontal += int(inst[1])
            if aim != 0:
                pos_depth += (int(inst[1]) * aim)
        elif inst[0] == "down":
            aim += int(inst[1])
        elif inst[0] == "up":
            aim -= int(inst[1])
    print("Horizontal position :", pos_horizontal)
    print("Depth: ", pos_depth)

    return(pos_horizontal * pos_depth)

commands = read_file()
print("Part one: ", part_one(commands))
print("part two: ", part_two(commands))