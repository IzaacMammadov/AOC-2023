"""Day 18 - Problem 2 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
trench_length = 0
current_row = 0
for instruction in input_text:
    hex_string = instruction.split()[2][2:-1]
    direction = int(hex_string[-1])
    num_moves = int(hex_string[:-1], 16)
    trench_length += num_moves
    match direction:
        case 3:
            current_row -= num_moves
        case 1:
            current_row += num_moves
        case 0:
            output += num_moves * -current_row
        case 2:
            output -= num_moves * -current_row
print(output + int(trench_length / 2) + 1)
