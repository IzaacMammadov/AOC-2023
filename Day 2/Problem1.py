"""Day 2 - Problem 1 of Advent of Code 2023"""
output = 0
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
for idx, string in enumerate(input_text):
    _, string = string.split(": ")
    games = string.split("; ")
    double_break = False
    for game in games:
        colour_set = game.split(", ")
        for num_colour in colour_set:
            num, colour = num_colour.split(" ")
            num = int(num)
            if (colour == "red" and num > 12) or (colour == "green" and num > 13) or (colour == "blue" and num > 14):
                double_break = True
                break
        if double_break:
            break
    if not double_break:
        output += (idx + 1)
print(output)
