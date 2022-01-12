def read_file():
    codes = []
    f = open("day8_input.txt", "r")
    code = f.readline()
    while code:
        code = [x for x in code.split()]
        codes.append(code[-4:])
        code = f.readline()
    f.close()
    return codes

codes = read_file()
count_value = 0
for code in range(len(codes)):
    print(codes[code])
    for digit in range(4):
        # print(len(codes[code][digit]))
        num_of_segments = len(codes[code][digit])
        print(num_of_segments)
        if num_of_segments in (2, 3, 4, 7):
            count_value += 1

print(count_value)