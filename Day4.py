def read_file():
    f = open("day4_input.txt", "r")
    #data = f.read().splitlines()
    # bingo_numbers = f.readline().split(",")
    # for i in range(len(bingo_numbers)):
    #     bingo_numbers[i] = bingo_numbers[i].strip()

    bingo_numbers = [int(x) for x in f.readline().strip("\n").split(",")]

    bingo_boards = []
    while f.readline():
        bingo_board = []
        for i in range(5):
            bingo_board.extend([int(x) for x in f.readline().strip("\n").split(" ") if x != ""])
        bingo_boards.append(bingo_board)

    #bingo_boards = f.read().splitlines()
    f.close()
    #data = [int(x) for x in data]
    return (bingo_numbers, bingo_boards)

def IsWinner(bingo_board):
    index = 0
    # Horizontal
    for i in range(5):
        if bingo_board[index] + bingo_board[index + 1] + bingo_board[index + 2] + bingo_board[index + 3] + bingo_board[index + 4] == 500:
            return True
        index += 5
    # Vertical
    index = 0
    for i in range(5):
        if bingo_board[index] + bingo_board[index + 5] + bingo_board[index + 10] + bingo_board[index + 15] + bingo_board[index + 20] == 500:
            return True
        index += 1
    # No winners!
    return False

bingo_numbers = read_file()[0]
bingo_boards = read_file()[1]

print(bingo_numbers)
print(bingo_boards)
print("\n")

found_a_winner = False

while found_a_winner == False:
    number = bingo_numbers[0]
    bingo_numbers = bingo_numbers[1:]
    for bingo_board in bingo_boards:
        for i in range(len(bingo_board)):
            if bingo_board[i] == number:
                bingo_board[i] = 100
    for bingo_board in bingo_boards:
        if IsWinner(bingo_board):
            sum_of_unmarked = sum([x for x in bingo_board if x != 100])
            print(bingo_board)
            print("Score of winning board: ", sum_of_unmarked)
            print("Last called number: ", number)
            print("Final score: ", sum_of_unmarked * number)
            found_a_winner = True