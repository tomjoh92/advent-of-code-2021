def read_file():
    lines = []
    f = open("day5_input_test.txt", "r")
    #coordinates = [int(x) for x in f.readline().strip(" -> ").split(",")]
    line = f.readline()
    while line:
        #print(line)
        line = line.strip("\n").split()
        #print(line)
        left = [int(x) for x in line[0].split(",")]
        #print(left)
        right = [int(x) for x in line[2].split(",")]
        #print(right)
        lines.append([left, right])
        line = f.readline()
    f.close()
    return lines


coordinates = read_file()
print(coordinates)
# print(coordinates[0][0])        #x1 och y1
# print(coordinates[0][0][1])     #y1

w, h = 10, 10
map = [[0 for x in range(w)] for y in range(h)]
line_points = []

for i in range(len(coordinates)):
    if coordinates[i][0][1] == coordinates[i][1][1]:
        #print("y är lika")
        y = coordinates[i][0][1]
        x1 = coordinates[i][0][0]
        x2 = coordinates[i][1][0]
        if  x1 < x2:
            #x1 < x2
            while x1 <= x2:
                line_points.append([x1, y])
                x1 +=1
        else:   #x1 > x2
            while x1 >= x2:
                line_points.append([x1, y])
                x1 -=1
    elif coordinates[i][0][0] == coordinates[i][1][0]:
        #print("x är lika")
        x = coordinates[i][0][0]
        y1 = coordinates[i][0][1]
        y2 = coordinates[i][1][1]
        if y1 < y2:
            while y1 <= y2:
                line_points.append([x, y1])
                y1 += 1
        else:   #y1 > y2
            while y1 >= y2:
                line_points.append([x, y1])
                y1 -= 1
    else:   #varken x och y är lika, part 2
        x1 = coordinates[i][0][0]
        x2 = coordinates[i][1][0]
        y1 = coordinates[i][0][1]
        y2 = coordinates[i][1][1]
        steps = (abs(x1-x2)+1)
        print(coordinates[i])
        for steps in range(steps):
            if x2 > x1:
                if y2 >= y1:
                    line_points.append([x1, y1])
                    y1 += 1
                else:
                    # y1 > y2
                    line_points.append([x1, y1])
                    y1 -= 1
                x1 += 1
            else:   # x1 > x2
                if y2 > y1:
                    line_points.append([x1, y1])
                    y1 += 1
                else:
                    # y1 > y2
                    line_points.append([x1, y1])
                    # print("x1: ", x1, "y1: ", y1)
                    # print("steps:", steps)
                    y1 -= 1
                x1 -= 1

print(line_points)
for i in range(len(line_points)):
    map[line_points[i][1]][line_points[i][0]] += 1

print("\nThe diagram will look like this: ")
for i in range(h):
    print(map[i])

warning_points = 0
test = [1, 2, 3, 1, 1, 5]
# warning_points += 1 sum([x for x in test if x >= 2])
for y in range(h):
    for x in range(w):
        if map[y][x] >= 2:
            warning_points += 1

print("Total overlap points: ", warning_points)
