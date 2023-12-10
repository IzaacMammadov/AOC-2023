"""Day 10 - Problem 1 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 1
starting_square = None
for i in range(140):
    for j in range(140):
        if input_text[i][j] == "S":
            starting_square = (i, j)
            break
current_square = (starting_square[0] + 1, starting_square[1])
next_move = (1, 0)
while current_square != starting_square:
    output += 1
    current_square = (current_square[0] + next_move[0], current_square[1] + next_move[1])
    match input_text[current_square[0]][current_square[1]]:
        case "|":
            if next_move == (1, 0):
                next_move = (1, 0)
            else:
                next_move = (-1, 0)
        case "-":
            if next_move == (0, 1):
                next_move = (0, 1)
            else:
                next_move = (0, -1)
        case "L":
            if next_move == (1, 0):
                next_move = (0, 1)
            else:
                next_move = (-1, 0)
        case "J":
            if next_move == (1, 0):
                next_move = (0, -1)
            else:
                next_move = (-1, 0)
        case "7":
            if next_move == (0, 1):
                next_move = (1, 0)
            else:
                next_move = (0, -1)
        case "F":
            if next_move == (0, -1):
                next_move = (1, 0)
            else:
                next_move = (0, 1)
print(output // 2)
