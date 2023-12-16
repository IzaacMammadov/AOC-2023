"""Day 16 - Problem 2 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0


def next_tile(current_tile, current_direction):
    """Returns a list of next tiles and directions from a given starting tile and direction"""
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


starting_options = (
        [((0, i), (1, 0)) for i in range(110)] +
        [((109, i), (-1, 0)) for i in range(110)] +
        [((i, 0), (0, 1)) for i in range(110)] +
        [((1, 109), (0, -1)) for i in range(110)]
)
for t_start, d_start in starting_options:
    to_explore = [(t_start, d_start)]
    seen = set()
    energised = set()
    while to_explore:
        t, d = to_explore.pop(0)
        if (t, d) not in seen and 0 <= t[0] < 110 and 0 <= t[1] < 110:
            energised.add(t)
            seen.add((t, d))
            results = next_tile(t, d)
            if results:
                to_explore += results
    output = max(output, len(energised))
print(output)
