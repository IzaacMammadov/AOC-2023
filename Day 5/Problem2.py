"""Day 5 - Problem 2 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
seeds_begin_ends = []
seed_boundaries = input_text[0].split(": ")[1].split()
for i in range(10):
    seeds_begin_ends.append((
        int(seed_boundaries[2 * i]), int(seed_boundaries[2 * i]) + int(seed_boundaries[2 * i + 1])
    ))


def mapping(seeds_begin_ends_param, mapping_line_start, mapping_line_end):
    """Maps from seed to soil etc. etc."""
    new_seed_begin_ends = []
    for line in range(mapping_line_start, mapping_line_end):
        destination_start, source_start, length = input_text[line].split()
        destination_start = int(destination_start)
        source_start = int(source_start)
        length = int(length)
        for input_idx, (seed_start, seed_end) in enumerate(seeds_begin_ends_param):
            if source_start <= seed_start and seed_end <= source_start + length:
                new_seed_begin_ends.append((
                    seed_start - source_start + destination_start, seed_end - source_start + destination_start
                ))
                seeds_begin_ends_param[input_idx] = (-1, -1)
            elif source_start <= seed_start < source_start + length:
                new_seed_begin_ends.append((
                    seed_start - source_start + destination_start, destination_start + length
                ))
                seeds_begin_ends_param[input_idx] = (source_start + length, seed_end)
            elif source_start < seed_end <= source_start + length:
                new_seed_begin_ends.append((
                    destination_start, seed_end - source_start + destination_start
                ))
                seeds_begin_ends_param[input_idx] = (seed_start, source_start)
            elif seed_start < source_start and seed_end > source_start + length:
                new_seed_begin_ends.append((
                    destination_start, destination_start + length
                ))
                seeds_begin_ends_param[input_idx] = (seed_start, source_start)
                seeds_begin_ends_param.append((source_start + length, seed_end))
    seeds_begin_ends_param += new_seed_begin_ends


mapping(seeds_begin_ends, 3, 23)
mapping(seeds_begin_ends, 25, 72)
mapping(seeds_begin_ends, 74, 107)
mapping(seeds_begin_ends, 109, 149)
mapping(seeds_begin_ends, 151, 179)
mapping(seeds_begin_ends, 181, 228)
mapping(seeds_begin_ends, 230, 258)
print(min(begin_end for begin_end in seeds_begin_ends if begin_end != (-1, -1))[0])
