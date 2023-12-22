"""Day 21 - Problem 2 of Advent of Code 2023"""
from pickle import dump, load

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
starting_point = (65, 65)
even_parity_dots = 7311  # accessible
odd_parity_dots = 7218  # accessible
steps_walked = 26501365
# # 0: top left, 1: top, 2: top right, 3: left, 4: right, 5: bottom left, 6: bottom, 7: bottom right
# entry_from = [[(1, 0)], [(0, 1)], [(1, 0)], [(0, 1)], [(0, 1)], [(1, 0)], [(0, 1)], [(1, 0)]]
# starting_locations = ([(0, 0)], [(0, 65)], [(0, 130)], [(65, 0)], [(65, 130)], [(130, 0)], [(130, 65)], [(130, 130)])
# for entry_from_idx, currently_accessible in enumerate(starting_locations):
#     if entry_from[entry_from_idx][0] == (1, 0):
#         even_seen = {currently_accessible[0]}
#         odd_seen = set()
#     else:
#         even_seen = set()
#         odd_seen = {currently_accessible[0]}
#     while len(even_seen) + len(odd_seen) < even_parity_dots + odd_parity_dots:
#         newly_accessible = set()
#         for point_row, point_col in currently_accessible:
#             for diff_row, diff_col in ((-1, 0), (1, 0), (0, 1), (0, -1)):
#                 new_row = point_row + diff_row
#                 new_col = point_col + diff_col
#                 in_bounds = 0 <= new_row < len(input_text) and 0 <= new_col < len(input_text[0])
#                 new_point = (new_row, new_col) not in even_seen | odd_seen
#                 if in_bounds and input_text[new_row][new_col] in ".S" and new_point:
#                     newly_accessible.add((new_row, new_col))
#                     if (new_row + new_col) % 2 == 0:
#                         even_seen.add((new_row, new_col))
#                     else:
#                         odd_seen.add((new_row, new_col))
#         entry_from[entry_from_idx].append((len(even_seen), len(odd_seen)))
#         currently_accessible = list(newly_accessible)
# with open("entry_from.pkl", "wb+") as pickle_file:
#     dump(entry_from, pickle_file)
with open("entry_from.pkl", "rb") as pickle_file:
    entry_from = load(pickle_file)
full_odd_blocks = 0
full_even_blocks = 0
extra_steps = 0
# S starts at (0, 0) and is even parity, we walk an odd number of steps
# y = 0
full_even_blocks += 1  # (0, 0)
# Blocks on the axis
full_blocks = (steps_walked - 130) // 131
if full_blocks % 2 == 0:
    full_odd_blocks += full_blocks // 2 * 4
    full_even_blocks += full_blocks // 2 * 4
else:
    full_odd_blocks += (full_blocks // 2 + 1) * 4
    full_even_blocks += full_blocks // 2 * 4
remainder = (steps_walked - 66) - 131 * full_blocks
for entry_direction in (1, 3, 4, 6):
    extra_steps += entry_from[entry_direction][remainder][full_blocks % 2]
    if remainder >= 131:
        extra_steps += entry_from[entry_direction][remainder - 131][(full_blocks + 1) % 2]
# Blocks off the axis
y = 1
while full_blocks >= 0:
    full_blocks = (steps_walked - 130 - 131 * y) // 131
    true_full_blocks = max(0, full_blocks)
    if true_full_blocks % 2 == 0:
        full_odd_blocks += true_full_blocks // 2 * 4
        full_even_blocks += true_full_blocks // 2 * 4
    else:
        full_odd_blocks += (true_full_blocks // 2 + ((y + 1) % 2)) * 4
        full_even_blocks += (true_full_blocks // 2 + (y % 2)) * 4
    remainder = (steps_walked - 132) - 131 * (true_full_blocks + y - 1)
    for entry_direction in (0, 2, 5, 7):
        if remainder >= 0:
            extra_steps += entry_from[entry_direction][remainder][(true_full_blocks + y) % 2]
        if remainder >= 131:
            extra_steps += entry_from[entry_direction][remainder - 131][(true_full_blocks + y + 1) % 2]
    y += 1
print(extra_steps + even_parity_dots * full_odd_blocks + odd_parity_dots * full_even_blocks)
