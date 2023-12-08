"""Day 8 - Problem 1 of Advent of Code 2023"""
from itertools import cycle

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
instructions = cycle(input_text[0])
node_map = {}
for line in input_text[2:]:
    start, dest_tuple = line.split(" = ")
    left, right = dest_tuple.removeprefix("(").removesuffix(")").split(", ")
    node_map[start] = (left, right)
current_location = "AAA"
while current_location != "ZZZ":
    output += 1
    current_location = node_map[current_location][int(next(instructions) == "R")]
print(output)
