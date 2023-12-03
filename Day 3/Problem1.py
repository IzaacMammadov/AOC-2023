"""Day 3 - Problem 1 of Advent of Code 2023"""
output = 0
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
symbol_hitbox = [[False] * 140 for _ in range(140)]
for i in range(140):
    for j in range(140):
        if (not input_text[i][j].isnumeric()) and (input_text[i][j] != "."):
            match (i, j):
                case (0, 0):
                    symbol_hitbox[0][1] = True
                    symbol_hitbox[1][0] = True
                    symbol_hitbox[1][1] = True
                case (139, 0):
                    symbol_hitbox[138][0] = True
                    symbol_hitbox[138][1] = True
                    symbol_hitbox[139][1] = True
                case (0, 139):
                    symbol_hitbox[0][138] = True
                    symbol_hitbox[1][138] = True
                    symbol_hitbox[1][139] = True
                case (139, 139):
                    symbol_hitbox[138][138] = True
                    symbol_hitbox[138][139] = True
                    symbol_hitbox[139][138] = True
                case (0, _):
                    symbol_hitbox[0][j - 1] = True
                    symbol_hitbox[0][j + 1] = True
                    symbol_hitbox[1][j - 1] = True
                    symbol_hitbox[1][j] = True
                    symbol_hitbox[1][j + 1] = True
                case (139, _):
                    symbol_hitbox[138][j - 1] = True
                    symbol_hitbox[138][j] = True
                    symbol_hitbox[138][j + 1] = True
                    symbol_hitbox[139][j - 1] = True
                    symbol_hitbox[139][j + 1] = True
                case (_, 0):
                    symbol_hitbox[i - 1][0] = True
                    symbol_hitbox[i - 1][1] = True
                    symbol_hitbox[i][1] = True
                    symbol_hitbox[i + 1][0] = True
                    symbol_hitbox[i + 1][1] = True
                case (_, 139):
                    symbol_hitbox[i - 1][138] = True
                    symbol_hitbox[i - 1][139] = True
                    symbol_hitbox[i][138] = True
                    symbol_hitbox[i + 1][138] = True
                    symbol_hitbox[i + 1][139] = True
                case _:
                    symbol_hitbox[i - 1][j - 1] = True
                    symbol_hitbox[i - 1][j] = True
                    symbol_hitbox[i - 1][j + 1] = True
                    symbol_hitbox[i][j - 1] = True
                    symbol_hitbox[i][j + 1] = True
                    symbol_hitbox[i + 1][j - 1] = True
                    symbol_hitbox[i + 1][j] = True
                    symbol_hitbox[i + 1][j + 1] = True
for i in range(140):
    current_number = []
    touches_symbol = False
    for j in range(140):
        if input_text[i][j].isnumeric():
            current_number.append(input_text[i][j])
            if symbol_hitbox[i][j]:
                touches_symbol = True
        else:
            if current_number and touches_symbol:
                output += int("".join(current_number))
            current_number = []
            touches_symbol = False
    if current_number and touches_symbol:
        output += int("".join(current_number))
print(output)
