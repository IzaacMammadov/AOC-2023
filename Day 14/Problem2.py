"""Day 14 - Problem 2 of Advent of Code 2023"""
from copy import deepcopy

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0


def cycle(current_pos):
    """Does a North-West-South-East cycle of the rocks"""
    # NORTH
    for col in range(len(current_pos[0])):
        next_will_land = 0
        for row in range(len(current_pos)):
            match current_pos[row][col]:
                case "#":
                    next_will_land = row + 1
                case "O":
                    current_pos[row] = "".join([current_pos[row][:col], ".", current_pos[row][col + 1:]])
                    current_pos[next_will_land] = "".join([
                        current_pos[next_will_land][:col], "O", current_pos[next_will_land][col + 1:]
                    ])
                    next_will_land += 1
    # WEST
    for row in range(len(current_pos)):
        next_will_land = 0
        for col in range(len(current_pos[0])):
            match current_pos[row][col]:
                case "#":
                    next_will_land = col + 1
                case "O":
                    current_pos[row] = "".join([current_pos[row][:col], ".", current_pos[row][col + 1:]])
                    current_pos[row] = "".join([
                        current_pos[row][:next_will_land], "O", current_pos[row][next_will_land + 1:]
                    ])
                    next_will_land += 1
    # SOUTH
    for col in range(len(current_pos[0])):
        next_will_land = len(current_pos) - 1
        for row in reversed(range(len(current_pos))):
            match current_pos[row][col]:
                case "#":
                    next_will_land = row - 1
                case "O":
                    current_pos[row] = "".join([current_pos[row][:col], ".", current_pos[row][col + 1:]])
                    current_pos[next_will_land] = "".join([
                        current_pos[next_will_land][:col], "O", current_pos[next_will_land][col + 1:]
                    ])
                    next_will_land -= 1
    # EAST
    for row in range(len(current_pos)):
        next_will_land = len(current_pos[0]) - 1
        for col in reversed(range(len(current_pos[0]))):
            match current_pos[row][col]:
                case "#":
                    next_will_land = col - 1
                case "O":
                    current_pos[row] = "".join([current_pos[row][:col], ".", current_pos[row][col + 1:]])
                    current_pos[row] = "".join([
                        current_pos[row][:next_will_land], "O", current_pos[row][next_will_land + 1:]
                    ])
                    next_will_land -= 1


seen = []
while input_text not in seen:
    seen.append(deepcopy(input_text))
    cycle(input_text)
first_seen = seen.index(input_text)
cycle_length = len(seen) - first_seen
for _ in range((1_000_000_000 - first_seen) % cycle_length):
    cycle(input_text)
for i in range(len(input_text)):
    for j in range(len(input_text[0])):
        if input_text[i][j] == "O":
            output += len(input_text) - i
print(output)
