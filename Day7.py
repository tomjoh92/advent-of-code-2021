def read_file():
    #data = {}
    f = open("day7_input.txt", "r")
    data = [int(x) for x in f.readline().split(",")]
    f.close()
    return data
crab_positions = read_file()
fuel_used = []
lowest_fuel = 0
lowest_pos = 0
temp_fuel = 0
#print(crab_positions)

#print((crab_positions[0]-2))

for index in range(max(crab_positions)):
    #print(index)
    for i in range(len(crab_positions)):
        temp_fuel += abs(crab_positions[i]-index)
    fuel_used.append(temp_fuel)
    if index == 0:
        lowest_fuel = temp_fuel
    else:
        if temp_fuel < lowest_fuel:
            lowest_fuel = temp_fuel
            lowest_pos = index
    temp_fuel = 0
#print(fuel_used)

print("Position: ", fuel_used.index(min(fuel_used)))
print("Total amount of fuel: ", min(fuel_used))
print(lowest_fuel)
print(lowest_pos)

