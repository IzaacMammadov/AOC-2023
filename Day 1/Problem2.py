"""Day 1 - Problem 2 of Advent of Code 2023"""
output = 0
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}
for string in input_text:
    n = len(string)
    first_num = None
    last_num = None
    for i in range(n):
        if string[i].isnumeric():
            first_num = string[i]
            break
        double_break = False
        for j in range(i):
            if string[j:i + 1] in mapping:
                first_num = mapping[string[j:i + 1]]
                double_break = True
                break
        if double_break:
            break
    for i in range(n - 1, -1, -1):
        if string[i].isnumeric():
            last_num = string[i]
            break
        double_break = False
        for j in range(i + 1, n):
            if string[i:j + 1] in mapping:
                last_num = mapping[string[i:j + 1]]
                double_break = True
                break
        if double_break:
            break
    num = int(f"{first_num}{last_num}")
    output += num
print(output)
