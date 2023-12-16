"""Day 16 - Problem 1 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
energised = set()
seen = set()


def next_tile(current_tile, current_direction):
    """Returns a list of next tiles and directions from a given starting tile and direction"""
    if 0 <= current_tile[0] < 110 and 0 <= current_tile[1] < 110:
        energised.add(current_tile)
        new_direction = None
        match input_text[current_tile[0]][current_tile[1]]:
            case "\\":
                match current_direction:
                    case (1, 0):
                        new_direction = [(0, 1)]
                    case (-1, 0):
                        new_direction = [(0, -1)]
                    case (0, 1):
                        new_direction = [(1, 0)]
                    case (0, -1):
                        new_direction = [(-1, 0)]
            case "/":
                match current_direction:
                    case (1, 0):
                        new_direction = [(0, -1)]
                    case (-1, 0):
                        new_direction = [(0, 1)]
                    case (0, 1):
                        new_direction = [(-1, 0)]
                    case (0, -1):
                        new_direction = [(1, 0)]
            case "-":
                match current_direction:
                    case (1, 0):
                        new_direction = [(0, 1), (0, -1)]
                    case (-1, 0):
                        new_direction = [(0, 1), (0, -1)]
                    case _:
                        new_direction = [current_direction]
            case "|":
                match current_direction:
                    case (0, 1):
                        new_direction = [(1, 0), (-1, 0)]
                    case (0, -1):
                        new_direction = [(1, 0), (-1, 0)]
                    case _:
                        new_direction = [current_direction]
            case ".":
                new_direction = [current_direction]
        new_tiles = [(current_tile[0] + new_dir[0], current_tile[1] + new_dir[1]) for new_dir in new_direction]
        return list(zip(new_tiles, new_direction))


to_explore = [((0, 0), (0, 1))]
while to_explore:
    t, d = to_explore.pop(0)
    if (t, d) not in seen:
        seen.add((t, d))
        results = next_tile(t, d)
        if results:
            to_explore += results

print(len(energised))
