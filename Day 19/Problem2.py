"""Day 19 - Problem 2 of Advent of Code 2023"""
from collections import defaultdict
from copy import deepcopy
from math import prod

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
workflows = {}
workflow = True
for line in input_text:
    if line == "":
        break
    elif workflow:
        workflow_name, instructions = line.split("{")
        instructions = instructions[:-1]
        instructions = instructions.split(",")
        workflows[workflow_name] = instructions

current_locations = defaultdict(list)
current_locations["in"] = [{"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}]
while not set(current_locations.keys()) <= {"A", "R"}:
    relevant_workflow_name = (set(current_locations.keys()) - {"A", "R"}).pop()
    relevant_workflow = workflows[relevant_workflow_name]
    for step in relevant_workflow:
        if ":" in step:
            condition, destination = step.split(":")
            if "<" in condition:
                letter, threshold = condition.split("<")
                threshold = int(threshold)
                to_remove = []
                for idx, letter_product in enumerate(current_locations[relevant_workflow_name]):
                    if letter_product[letter][0] < threshold <= letter_product[letter][1]:
                        new_letter_product = deepcopy(letter_product)
                        letter_product[letter] = [threshold, letter_product[letter][1]]
                        new_letter_product[letter] = [new_letter_product[letter][0], threshold - 1]
                        current_locations[destination].append(new_letter_product)
                    elif letter_product[letter][1] < threshold:
                        to_remove.append(idx)
                        current_locations[destination].append(deepcopy(letter_product))
                for idx in reversed(to_remove):
                    current_locations[relevant_workflow_name].pop(idx)
            elif ">" in condition:
                letter, threshold = condition.split(">")
                threshold = int(threshold)
                to_remove = []
                for idx, letter_product in enumerate(current_locations[relevant_workflow_name]):
                    if letter_product[letter][0] <= threshold < letter_product[letter][1]:
                        new_letter_product = deepcopy(letter_product)
                        letter_product[letter] = [letter_product[letter][0], threshold]
                        new_letter_product[letter] = [threshold + 1, new_letter_product[letter][1]]
                        current_locations[destination].append(new_letter_product)
                    elif threshold < letter_product[letter][0]:
                        to_remove.append(idx)
                        current_locations[destination].append(deepcopy(letter_product))
                for idx in reversed(to_remove):
                    current_locations[relevant_workflow_name].pop(idx)
        else:
            current_locations[step] += current_locations[relevant_workflow_name]
            del current_locations[relevant_workflow_name]
for letter_product in current_locations["A"]:
    output += prod(letter_product[letter][1] - letter_product[letter][0] + 1 for letter in "xmas")
print(output)
