"""Day 12 - Problem 1 of Advent of Code 2023"""
from itertools import combinations

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0


def is_valid_arrangement(arrangement, groups):
    """Checks if a certain arrangement of #s and .s matches up with the groupings we expect"""
    groups_seen = []
    current_streak = 0
    for char in arrangement:
        if char == "#":
            current_streak += 1
        elif current_streak:
            groups_seen.append(current_streak)
            current_streak = 0
    if current_streak:
        groups_seen.append(current_streak)
    return groups_seen == groups


for row in input_text:
    arr, group_text = row.split()
    group_nums = [int(i) for i in group_text.split(",")]
    unknowns = [i for i in range(len(arr)) if arr[i] == "?"]
    num_damaged_to_add = sum(group_nums) - arr.count("#")
    for extra_damaged in combinations(unknowns, num_damaged_to_add):
        arr_to_test = list(arr)
        for unknown in unknowns:
            arr_to_test[unknown] = "."
        for to_damage in extra_damaged:
            arr_to_test[to_damage] = "#"
        arr_to_test = "".join(arr_to_test)
        output += int(is_valid_arrangement(arr_to_test, group_nums))

print(output)
