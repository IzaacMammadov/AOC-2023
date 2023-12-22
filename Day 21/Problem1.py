"""Day 21 - Problem 1 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
starting_point = None
for row in range(len(input_text)):
    for col in range(len(input_text[0])):
        if input_text[row][col] == "S":
            starting_point = (row, col)
            break
    else:
        continue
    break

currently_accessible = [starting_point]
for _ in range(64):
    newly_accessible = set()
    for point_row, point_col in currently_accessible:
        for diff_row, diff_col in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            new_row = point_row + diff_row
            new_col = point_col + diff_col
            in_bounds = 0 <= new_row < len(input_text) and 0 <= new_col < len(input_text[0])
            if in_bounds and input_text[new_row][new_col] in ".S":
                newly_accessible.add((new_row, new_col))
    currently_accessible = list(newly_accessible)
print(len(currently_accessible))
