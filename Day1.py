def read_file():
    f = open("day1_input.txt", "r")
    depth_measurement = f.read().splitlines()
    f.close()
    depth_measurement = [int(x) for x in depth_measurement]
    return depth_measurement

def part_one(depth_measurement):
    num_of_incr = 0
    for i in range(len(depth_measurement)):
    #print(len(depth_measurement))
        if i > 0:
            if depth_measurement[i] > depth_measurement[i-1]:
                num_of_incr += 1
                #print(num_of_incr)
    return num_of_incr

def part_two(depth_measurement):
    num_of_incr = 0
    sum_of_three = 0
    #prev_sum_of_three = depth_measurement[0] + depth_measurement[1] + depth_measurement[2]
    prev_sum_of_three = sum(depth_measurement[:3])

    for i in range(3, len(depth_measurement)):
        curr_sum = prev_sum_of_three + depth_measurement[i] - depth_measurement[i-3]
        if curr_sum > prev_sum_of_three:
            num_of_incr += 1
        prev_sum_of_three = sum_of_three

    return num_of_incr



depth_measurement = read_file()


print(f"Part one: {part_one(depth_measurement)}")
print(f"Part two: {part_two(depth_measurement)}")
