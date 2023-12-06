"""Day 5 - Problem 1 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
seeds = []
for seed in input_text[0].split(": ")[1].split():
    seeds.append(int(seed))


def mapping(mapping_line_start, mapping_line_end):
    """Maps from a seed -> soil etc. etc."""
    for input_idx, input_seed in enumerate(seeds):
        for line in range(mapping_line_start, mapping_line_end):
            destination_start, source_start, length = input_text[line].split()
            destination_start = int(destination_start)
            source_start = int(source_start)
            length = int(length)
            if source_start <= input_seed < source_start + length:
                seeds[input_idx] = destination_start + input_seed - source_start


mapping(3, 23)
mapping(25, 72)
mapping(74, 107)
mapping(109, 149)
mapping(151, 179)
mapping(181, 228)
mapping(230, 258)

print(min(seeds))
