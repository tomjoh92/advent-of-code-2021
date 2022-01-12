def read_file():
    f = open("day6_input.txt", "r")
    data = f.read().splitlines()
    f.close()
    #data = data[0].split(",")
    data = [int(x) for x in data[0].split(",")]
    return data

initial_state = read_file()
print(initial_state)
current_state = initial_state


for i in range(80):
    for i in range(len(current_state)):
        current_state[i] = current_state[i]-1
        if current_state[i] < 0:
            current_state[i] = 6
            current_state.append(8)

#print(current_state)
print("Total fish: ", len(current_state))