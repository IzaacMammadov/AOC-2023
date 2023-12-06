"""Day 6 - Problem 1 of Advent of Code 2023"""
from math import sqrt, floor, ceil

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 1
times = input_text[0].split()[1:]
distances = input_text[1].split()[1:]
for i in range(4):
    time = int(times[i])
    distance = int(distances[i])
    x1 = (time - sqrt(time ** 2 - 4 * distance)) / 2
    x2 = (time + sqrt(time ** 2 - 4 * distance)) / 2
    output *= (floor(x2) - ceil(x1) + 1)
print(output)
