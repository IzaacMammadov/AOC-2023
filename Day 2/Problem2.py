"""Day 2 - Problem 2 of Advent of Code 2023"""
output = 0
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
for idx, string in enumerate(input_text):
    _, string = string.split(": ")
    games = string.split("; ")
    min_blue = 0
    min_red = 0
    min_green = 0
    for game in games:
        colour_set = game.split(", ")
        for num_colour in colour_set:
            num, colour = num_colour.split(" ")
            num = int(num)
            if colour == "red":
                min_red = max(min_red, num)
            if colour == "green":
                min_green = max(min_green, num)
            if colour == "blue":
                min_blue = max(min_blue, num)
    output += min_blue * min_red * min_green
print(output)
