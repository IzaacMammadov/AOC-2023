"""Day 23 - Problem 1 of Advent of Code 2023"""
from copy import deepcopy

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
starting_location = None
ending_location = None
for starting_col in range(len(input_text[0])):
    if input_text[0][starting_col] == ".":
        starting_location = (0, starting_col)
        break
for ending_col in range(len(input_text[0])):
    if input_text[-1][ending_col] == ".":
        ending_location = (len(input_text) - 1, ending_col)
        break
possible_paths = [(starting_location, set(), 0)]
while possible_paths:
    start_point, seen, current_steps = possible_paths.pop()
    if start_point == ending_location:
        print(f"Reached in {current_steps=}, considering new path now, {len(possible_paths)=}")
        output = max(output, current_steps)
    else:
        for d_row, d_col in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            new_point = (start_point[0] + d_row, start_point[1] + d_col)
            if 0 <= new_point[0] < len(input_text) and 0 <= new_point[1] < len(input_text[0]) and new_point not in seen:
                match input_text[new_point[0]][new_point[1]]:
                    case "#":
                        pass
                    case ".":
                        new_seen = deepcopy(seen)
                        new_seen.add(start_point)
                        possible_paths.append((new_point, new_seen, current_steps + 1))
                    case "^":
                        if d_row == -1 and (new_point[0] - 1, new_point[1]) not in seen:
                            new_seen = deepcopy(seen)
                            new_seen.add(start_point)
                            new_seen.add(new_point)
                            possible_paths.append(((new_point[0] - 1, new_point[1]), new_seen, current_steps + 2))
                    case "v":
                        if d_row == 1 and (new_point[0] + 1, new_point[1]) not in seen:
                            new_seen = deepcopy(seen)
                            new_seen.add(start_point)
                            new_seen.add(new_point)
                            possible_paths.append(((new_point[0] + 1, new_point[1]), new_seen, current_steps + 2))
                    case ">":
                        if d_col == 1 and (new_point[0], new_point[1] + 1) not in seen:
                            new_seen = deepcopy(seen)
                            new_seen.add(start_point)
                            new_seen.add(new_point)
                            possible_paths.append(((new_point[0], new_point[1] + 1), new_seen, current_steps + 2))
                    case "<":
                        if d_col == -1 and (new_point[0], new_point[1] - 1) not in seen:
                            new_seen = deepcopy(seen)
                            new_seen.add(start_point)
                            new_seen.add(new_point)
                            possible_paths.append(((new_point[0], new_point[1] - 1), new_seen, current_steps + 2))
print(output)
