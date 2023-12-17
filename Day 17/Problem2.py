"""Day 17 - Problem 2 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
# 1 = R, 2 = L, 3 = U, 4 = D
# (row, col, num_steps_taken, direction) : distance
tenacious = {(0, 0, 0, 1): 0, (0, 0, 0, 4): 0}
fixed = {}
seen = set()
while True:
    next_move = min(tenacious, key=lambda i: tenacious[i])
    next_move_distance = tenacious[next_move]
    if next_move[0] == len(input_text) - 1 and next_move[1] == len(input_text[0]) - 1 and next_move[2] >= 4:
        print(next_move_distance)
        break
    if (next_move[0], next_move[1]) not in seen:
        seen.add((next_move[0], next_move[1]))
    del tenacious[next_move]
    fixed[next_move] = next_move_distance
    for move_row, move_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        new_row, new_col = next_move[0] + move_row, next_move[1] + move_col
        if 0 <= new_row < len(input_text) and 0 <= new_col < len(input_text[0]):
            can_turn = next_move[2] >= 4
            match (move_row, move_col, next_move[3], can_turn):
                case (1, 0, 4, _) | (-1, 0, 3, _) | (0, 1, 1, _) | (0, -1, 2, _):
                    new_num_steps = next_move[2] + 1
                    new_direction = next_move[3]
                case (1, 0, 3, _) | (-1, 0, 4, _) | (0, 1, 2, _) | (0, -1, 1, _):
                    continue
                case (1, 0, _, True):
                    new_num_steps = 1
                    new_direction = 4
                case (-1, 0, _, True):
                    new_num_steps = 1
                    new_direction = 3
                case (0, 1, _, True):
                    new_num_steps = 1
                    new_direction = 1
                case (0, -1, _, True):
                    new_num_steps = 1
                    new_direction = 2
                case _:
                    continue
            new_move = (new_row, new_col, new_num_steps, new_direction)
            if new_num_steps <= 10 and new_move not in fixed:
                tenacious[new_move] = min(
                    tenacious.get(new_move, 10 ** 10), next_move_distance + int(input_text[new_row][new_col])
                )
