"""Day 13 - Problem 2 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
patterns = []
current_start = 0
for idx, row in enumerate(input_text):
    if row == "":
        patterns.append(input_text[current_start:idx])
        current_start = idx + 1
patterns.append(input_text[current_start:])
for pattern in patterns:
    valid_vertical_mirrors_perfect = set(range(1, len(pattern[0])))
    valid_vertical_mirrors_smudge = set()
    for row in pattern:
        valid = set()
        for i in range(1, len(row)):
            if row[max(0, 2 * i - len(row)):i] == row[2 * i - 1: i - 1:-1]:
                valid.add(i)
        demoted = valid_vertical_mirrors_perfect - valid
        valid_vertical_mirrors_perfect &= valid
        valid_vertical_mirrors_smudge &= valid
        valid_vertical_mirrors_smudge |= demoted
    if valid_vertical_mirrors_smudge:
        output += valid_vertical_mirrors_smudge.pop()
    valid_horizontal_mirrors_perfect = set(range(1, len(pattern)))
    valid_horizontal_mirrors_smudge = set()
    for col_num in range(len(pattern[0])):
        col = [pattern[i][col_num] for i in range(len(pattern))]
        valid = set()
        for i in range(1, len(col)):
            if col[max(0, 2 * i - len(col)):i] == col[2 * i - 1:i - 1:-1]:
                valid.add(i)
        demoted = valid_horizontal_mirrors_perfect - valid
        valid_horizontal_mirrors_perfect &= valid
        valid_horizontal_mirrors_smudge &= valid
        valid_horizontal_mirrors_smudge |= demoted
    if valid_horizontal_mirrors_smudge:
        output += valid_horizontal_mirrors_smudge.pop() * 100
print(output)
