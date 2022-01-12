def read_file():
    data = {}
    f = open("day6_input.txt", "r")
    array = [int(x) for x in f.readline().split(",")]
    f.close()
    for value in range(9):
        data[value] = 0
    for element in array:
        data[element] += 1
    return data

initial_state = read_file()
print("Initial state: \t", initial_state)
current_state = initial_state

for days in range(256):
    zeroes = current_state[0]
    current_state[0] = 0
    for index in range(1, len(current_state)):
        current_state[index-1] = current_state[index]
        current_state[index] = 0
    current_state[6] += zeroes
    current_state[8] += zeroes
    #print("After", days+1, "days:\t", current_state)

num_fish = 0
for key in current_state:
    num_fish += current_state[key]
print(current_state)
print("Total fish: ", num_fish)


