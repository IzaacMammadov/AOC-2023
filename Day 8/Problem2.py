"""Day 8 - Problem 2 of Advent of Code 2023"""
from itertools import cycle
from math import lcm

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

node_map = {}
for line in input_text[2:]:
    start, dest_tuple = line.split(" = ")
    left, right = dest_tuple.removeprefix("(").removesuffix(")").split(", ")
    node_map[start] = (left, right)
current_locations = [node for node in node_map if node[2] == "A"]
# Have to use inspection to see that actually each node ends up on a "Z" destination at periodic intervals
cycle_lengths = []
for location in current_locations:
    cycle_length = 0
    instructions = cycle(input_text[0])
    while location[2] != "Z":
        cycle_length += 1
        location = node_map[location][int(next(instructions) == "R")]
    cycle_lengths.append(cycle_length)

print(lcm(*cycle_lengths))
