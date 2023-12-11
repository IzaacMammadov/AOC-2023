"""Day 11 - Problem 1 of Advent of Code 2023"""
from itertools import combinations

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
doubles_rows = []
for row in range(140):
    if "#" not in input_text[row]:
        doubles_rows.append(row)
for row in reversed(doubles_rows):
    input_text = input_text[:row + 1] + ["".join(["." for _ in range(140)])] + input_text[row + 1:]
doubles_columns = []
for col in range(140):
    hash_seen = False
    for row in range(145):
        if input_text[row][col] == "#":
            hash_seen = True
            break
    if not hash_seen:
        doubles_columns.append(col)
for col in reversed(doubles_columns):
    for row in range(145):
        input_text[row] = "".join([input_text[row][: col + 1]] + ["."] + [input_text[row][col + 1:]])
galaxies = []
for i in range(145):
    for j in range(148):
        if input_text[i][j] == "#":
            galaxies.append((i, j))
for (x1, y1), (x2, y2) in combinations(galaxies, 2):
    output += abs(x2 - x1) + abs(y2 - y1)
print(output)
