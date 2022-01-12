def read_file():
    codes = []
    patterns = []
    lines = []
    f = open("day8_input.txt", "r")
    line = f.readline()
    while line:
        line = [x for x in line.split()]
        # codes.append(line[-4:])
        # patterns.append(line[:10])

        codes = line[-4:]
        patterns = sorted(line[:10], key=len)
        lines.append([patterns, codes])
        line = f.readline()
    f.close()
    #print(test[0])
    #print(codes)
    #print(patterns)
    return lines

def cmp_string(a,b):
    count = str()
    for char in a:
        if char in b:
            count += char
    return count

#codes, patterns = read_file()
input = read_file()
patterns = []
codes = []
decoded_code = []
decoded_codes = []

# for i in range(len(input)):
#     patterns.append(input[i][0])
#     codes.append(input[i][1])
# print("All patterns: ", patterns)
# print("All codes: ", codes)


for problem in input:
    ten = problem[0]
    four = problem[1]
    print("ten: ", ten)
    print("four: ", four)
    # 1, 4, 7, 8
    setup = dict({ten[0]: 1, ten[1]: 7, ten[2]: 4, ten[9]: 8})
    #print(setup)
    fives = [ten[3], ten[4], ten[5]]
    sixes = [ten[6], ten[7], ten[8]]
    # 6
    for index in range(len(sixes)):
        if len(cmp_string(ten[0], sixes[index])) == 1:
            setup[sixes[index]] = 6
            del(sixes[index])
            break
    # 3
    for index in range(len(fives)):
        if len(cmp_string(ten[0], fives[index])) == 2:
            setup[fives[index]] = 3
            del(fives[index])
            break
    # 5
    for index in range(len(fives)):
        if len(cmp_string(ten[2], fives[index])) == 3:
            setup[fives[index]] = 5
            del(fives[index])
            break
    # 0
    for index in range(len(sixes)):
        if len(cmp_string(ten[2], sixes[index])) == 3:
            setup[sixes[index]] = 0
            del(sixes[index])
            break
    # 9
    setup[sixes[0]] = 9
    # 2
    setup[fives[0]] = 2
    print(setup)

    for index in range(len(four)):
        #print(index)
        for key, value in setup.items():
            #print("key: ", "".join(sorted(key)))
            #print("code:", "".join(sorted(four[index])))
            #print("value: ", value)
            if "".join(sorted(four[index])) == "".join(sorted(key)):
                #print(value)
                decoded_code.append(value)
                break
    print(decoded_code)
    decoded_codes.append(decoded_code)
    decoded_code = []
print(decoded_codes)
total_value = 0
for index in range(len(decoded_codes)):
    print(decoded_codes[index])
    code_value = 0

    s = [str(i) for i in decoded_codes[index]]
    # print("s: ", s)
    res = int("".join(s))
    # print("res: ", res)
    total_value += res
    print(total_value)





