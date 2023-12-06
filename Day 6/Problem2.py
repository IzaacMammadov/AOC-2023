"""Day 6 - Problem 2 of Advent of Code 2023"""
from math import sqrt, floor, ceil

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
times = input_text[0].split()[1:]
distances = input_text[1].split()[1:]
time = int("".join(times))
distance = int("".join(distances))
x1 = (time - sqrt(time ** 2 - 4 * distance)) / 2
x2 = (time + sqrt(time ** 2 - 4 * distance)) / 2
output = (floor(x2) - ceil(x1) + 1)
print(output)
