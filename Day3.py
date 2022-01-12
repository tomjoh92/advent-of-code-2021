def read_file():
    f = open("day3_input.txt", "r")
    data = f.read().splitlines()
    f.close()
    #data = [int(x) for x in data]
    return data

def part_one (binary_code):
    num_ones = 0
    num_zeros = 0
    gamma = []
    epsilon = []
    for a in range(len(binary_code[0])):
        for i in range(len(binary_code)):
            if (binary_code[i])[a] == "1":
                num_ones += 1
            else:
                num_zeros += 1
        if num_ones > num_zeros:
            gamma.append("1")
        else:
            gamma.append("0")
        num_ones = 0
        num_zeros = 0
    for i in range(len(gamma)):
        if gamma[i] == "1":
            epsilon.append("0")
        else:
            epsilon.append("1")
    gamma_in_deci = int("".join(gamma), 2)
    epsilon_in_deci = int("".join(epsilon), 2)
    print("gamma in binary: ", "".join(gamma))
    print("gamma in decimal: ", gamma_in_deci)
    print("epsilon in binary: ", "".join(epsilon))
    print("epsilon in decimal: ", epsilon_in_deci)
    power_consumption = gamma_in_deci * epsilon_in_deci
    return (power_consumption)

def part_two(binary_code):
    oxygen_candidates = binary_code
    CO2_candidates = binary_code
    index = 0

    while len(oxygen_candidates) > 1:
        one = 0
        zero = 0
        ones = []
        zeroes = []
        for a in range(len(oxygen_candidates)):
            #print(a)
            if oxygen_candidates[a][index] == "0":
                zero += 1
                zeroes.append(oxygen_candidates[a])
            else:
                one += 1
                ones.append(oxygen_candidates[a])
        if zero > one:
            oxygen_candidates = zeroes
        else:
            oxygen_candidates = ones
        #print(oxygen_candidates)
        index += 1
    print("oxygen generator rating: ", oxygen_candidates[0])

    index = 0
    while len(CO2_candidates) > 1:
        one = 0
        zero = 0
        ones = []
        zeroes = []
        for a in range(len(CO2_candidates)):
            #print(a)
            if CO2_candidates[a][index] == "0":
                zero += 1
                zeroes.append(CO2_candidates[a])
            else:
                one += 1
                ones.append(CO2_candidates[a])
        if one < zero:
            CO2_candidates = ones
        else:
            CO2_candidates = zeroes
        index += 1
    print("CO2 generator rating: ", CO2_candidates[0])
    oxygen_in_deci = int(oxygen_candidates[0], 2)
    CO2_in_deci = int(CO2_candidates[0], 2)
    print("oxygen generator rating in decimal: ", oxygen_in_deci)
    print("CO2 generator rating in decimal: ", CO2_in_deci)
    lifesupport_rating = oxygen_in_deci * CO2_in_deci
    return lifesupport_rating




binary_code = read_file()

print("Part one: ", part_one(binary_code))
print("Part two: ", part_two(binary_code))

