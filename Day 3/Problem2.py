"""Day 3 - Problem 2 of Advent of Code 2023"""
from collections import defaultdict

output = 0
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
star_hitbox = [[[] for _ in range(140)] for _ in range(140)]
current_star_index = 0
for i in range(140):
    for j in range(140):
        if input_text[i][j] == "*":
            match (i, j):
                case (0, 0):
                    star_hitbox[0][1].append(current_star_index)
                    star_hitbox[1][0].append(current_star_index)
                    star_hitbox[1][1].append(current_star_index)
                case (139, 0):
                    star_hitbox[138][0].append(current_star_index)
                    star_hitbox[138][1].append(current_star_index)
                    star_hitbox[139][1].append(current_star_index)
                case (0, 139):
                    star_hitbox[0][138].append(current_star_index)
                    star_hitbox[1][138].append(current_star_index)
                    star_hitbox[1][139].append(current_star_index)
                case (139, 139):
                    star_hitbox[138][138].append(current_star_index)
                    star_hitbox[138][139].append(current_star_index)
                    star_hitbox[139][138].append(current_star_index)
                case (0, _):
                    star_hitbox[0][j - 1].append(current_star_index)
                    star_hitbox[0][j + 1].append(current_star_index)
                    star_hitbox[1][j - 1].append(current_star_index)
                    star_hitbox[1][j].append(current_star_index)
                    star_hitbox[1][j + 1].append(current_star_index)
                case (139, _):
                    star_hitbox[138][j - 1].append(current_star_index)
                    star_hitbox[138][j].append(current_star_index)
                    star_hitbox[138][j + 1].append(current_star_index)
                    star_hitbox[139][j - 1].append(current_star_index)
                    star_hitbox[139][j + 1].append(current_star_index)
                case (_, 0):
                    star_hitbox[i - 1][0].append(current_star_index)
                    star_hitbox[i - 1][1].append(current_star_index)
                    star_hitbox[i][1].append(current_star_index)
                    star_hitbox[i + 1][0].append(current_star_index)
                    star_hitbox[i + 1][1].append(current_star_index)
                case (_, 139):
                    star_hitbox[i - 1][138].append(current_star_index)
                    star_hitbox[i - 1][139].append(current_star_index)
                    star_hitbox[i][138].append(current_star_index)
                    star_hitbox[i + 1][138].append(current_star_index)
                    star_hitbox[i + 1][139].append(current_star_index)
                case _:
                    star_hitbox[i - 1][j - 1].append(current_star_index)
                    star_hitbox[i - 1][j].append(current_star_index)
                    star_hitbox[i - 1][j + 1].append(current_star_index)
                    star_hitbox[i][j - 1].append(current_star_index)
                    star_hitbox[i][j + 1].append(current_star_index)
                    star_hitbox[i + 1][j - 1].append(current_star_index)
                    star_hitbox[i + 1][j].append(current_star_index)
                    star_hitbox[i + 1][j + 1].append(current_star_index)
            current_star_index += 1

star_to_touching_numbers = defaultdict(list)
for i in range(140):
    current_number = []
    touching_stars = set()
    for j in range(140):
        if input_text[i][j].isnumeric():
            current_number.append(input_text[i][j])
            touching_stars |= set(star_hitbox[i][j])
        else:
            for star in touching_stars:
                star_to_touching_numbers[star].append(int("".join(current_number)))
            current_number = []
            touching_stars = set()
    for star in touching_stars:
        star_to_touching_numbers[star].append(int("".join(current_number)))
for num_list in star_to_touching_numbers.values():
    if len(num_list) >= 2:
        output += num_list[0] * num_list[1]
print(output)
