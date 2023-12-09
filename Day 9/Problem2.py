"""Day 9 - Problem 2 of Advent of Code 2023"""
from numpy import diff

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
for line in input_text:
    nums = [[int(i) for i in line.split()]]
    while any(i != 0 for i in nums[-1]):
        nums.append(list(diff(nums[-1])))
    next_diff = 0
    while nums:
        next_diff = nums.pop()[0] - next_diff
    output += next_diff
print(output)
