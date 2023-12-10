"""Day 10 - Problem 2 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
starting_square = None
for i in range(len(input_text)):
    for j in range(len(input_text[0])):
        if input_text[i][j] == "S":
            starting_square = (i, j)
            new_line = list(input_text[i])
            new_line[j] = "7"
            input_text[i] = "".join(new_line)
            break
current_square = (starting_square[0] + 1, starting_square[1])
next_move = (1, 0)
pipes = {starting_square, current_square}
while current_square != starting_square:
    current_square = (current_square[0] + next_move[0], current_square[1] + next_move[1])
    pipes.add(current_square)
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

for i in range(len(input_text)):
    for j in range(len(input_text[0])):
        if (i, j) not in pipes:
            pipes_crossed = 0
            last_corner_entry = None
            for new_j in range(j + 1, len(input_text)):
                if (i, new_j) in pipes:
                    corner_exit_L7 = input_text[i][new_j] == "7" and last_corner_entry == "L"
                    corner_exit_FJ = input_text[i][new_j] == "J" and last_corner_entry == "F"
                    if input_text[i][new_j] == "|" or corner_exit_L7 or corner_exit_FJ:
                        pipes_crossed += 1
                    elif input_text[i][new_j] in ("F", "L"):
                        last_corner_entry = input_text[i][new_j]
            if pipes_crossed % 2 == 1:
                output += 1
print(output)
