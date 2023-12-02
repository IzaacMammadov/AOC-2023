"""Day 1 - Problem 1 of Advent of Code 2023"""
output = 0
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
for string in input_text:
    n = len(string)
    first_num = None
    last_num = None
    for i in range(n):
        if string[i].isnumeric():
            first_num = string[i]
            break
    for i in range(n - 1, -1, -1):
        if string[i].isnumeric():
            last_num = string[i]
            break
    num = int(f"{first_num}{last_num}")
    output += num
print(output)
