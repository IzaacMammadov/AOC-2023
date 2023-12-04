"""Day 4 - Problem 1 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

copies = [1] * 202

for idx, line in enumerate(input_text):
    w, m = line.split(": ")[1].split(" | ")
    length = len(set(int(i) for i in w.split()) & set(int(i) for i in m.split()))
    if length >= 1:
        for i in range(idx + 1, idx + 1 + length):
            copies[i] += copies[idx]
print(sum(copies))
