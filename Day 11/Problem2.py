"""Day 11 - Problem 1 of Advent of Code 2023"""
from itertools import combinations

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
doubles_rows = set()
for row in range(140):
    if "#" not in input_text[row]:
        doubles_rows.add(row)
doubles_columns = set()
for col in range(140):
    hash_seen = False
    for row in range(140):
        if input_text[row][col] == "#":
            hash_seen = True
            break
    if not hash_seen:
        doubles_columns.add(col)
galaxies = []
for i in range(140):
    for j in range(140):
        if input_text[i][j] == "#":
            galaxies.append((i, j))
for (x1, y1), (x2, y2) in combinations(galaxies, 2):
    output += abs(x2 - x1) + abs(y2 - y1)
    output += len(set(range(min(x1, x2), max(x1, x2) + 1)) & doubles_rows) * 999_999
    output += len(set(range(min(y1, y2), max(y1, y2) + 1)) & doubles_columns) * 999_999
print(output)
