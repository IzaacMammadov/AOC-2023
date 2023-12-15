"""Day 15 - Problem 2 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().split(",")
output = 0


def hash_algo(string):
    """HASH algorithm run on a string"""
    hash_output = 0
    for char in string:
        hash_output += ord(char)
        hash_output *= 17
        hash_output %= 256
    return hash_output


boxes = [[] for _ in range(256)]
for input_string in input_text:
    if "=" in input_string:
        label, focal_number = input_string.split("=")
        box_number = hash_algo(label)
        for idx, [current_label, _] in enumerate(boxes[box_number]):
            if current_label == label:
                boxes[box_number][idx] = [current_label, focal_number]
                break
        else:
            boxes[box_number].append([label, focal_number])
    else:
        label = input_string[:-1]
        box_number = hash_algo(label)
        for idx, [current_label, _] in enumerate(boxes[box_number]):
            if current_label == label:
                boxes[box_number].pop(idx)
                break

for box_idx, box in enumerate(boxes):
    for position_idx, [_, focus] in enumerate(box):
        output += (box_idx + 1) * (position_idx + 1) * int(focus)
print(output)
