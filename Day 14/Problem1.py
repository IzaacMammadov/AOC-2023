"""Day 14 - Problem 1 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
for col in range(len(input_text[0])):
    next_will_land = 0
    for row in range(len(input_text)):
        match input_text[row][col]:
            case "#":
                next_will_land = row + 1
            case "O":
                output += len(input_text) - next_will_land
                next_will_land += 1
print(output)
