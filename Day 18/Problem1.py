"""Day 18 - Problem 1 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
trench_length = 0
current_row = 0
for instruction in input_text:
    direction, num, _ = instruction.split()
    num = int(num)
    trench_length += num
    match direction:
        case "U":
            current_row -= num
        case "D":
            current_row += num
        case "R":
            output += num * -current_row
        case "L":
            output -= num * -current_row
print(output + int(trench_length / 2) + 1)
