"""Day 4 - Problem 1 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

output = 0

for idx, line in enumerate(input_text):
    w, m = line.split(": ")[1].split(" | ")
    length = len(set(int(i) for i in w.split()) & set(int(i) for i in m.split()))
    if length >= 1:
        output += 2 ** (length - 1)
print(output)
