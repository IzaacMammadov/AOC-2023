"""Day 20 - Problem 1 of Advent of Code 2023"""
from collections import defaultdict

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
low_pulses = 0
high_pulses = 0
module_destinations = {}
conjunctions = set()
flip_flop_states = {}
conjunction_states = defaultdict(dict)
for line in input_text:
    name, destinations_string = line.split(" -> ")
    match line[0]:
        case "%":
            name = name[1:]
            flip_flop_states[name] = False
        case "&":
            name = name[1:]
            conjunctions.add(name)
    destinations = destinations_string.split(", ")
    module_destinations[name] = destinations
for module, destinations in module_destinations.items():
    for destination in destinations:
        if destination in conjunctions:
            conjunction_states[destination][module] = False
for _ in range(1000):
    signals_to_process = [(False, "broadcaster", "button")]
    while signals_to_process:
        signal_level, destination, from_module = signals_to_process.pop(0)
        if signal_level:
            high_pulses += 1
        else:
            low_pulses += 1
        if destination in flip_flop_states:
            if not signal_level:
                flip_flop_states[destination] = not flip_flop_states[destination]
                for new_destination in module_destinations[destination]:
                    signals_to_process.append((flip_flop_states[destination], new_destination, destination))
        elif destination in conjunction_states:
            conjunction_states[destination][from_module] = signal_level
            pulse_to_send = (set(conjunction_states[destination].values()) != {True})
            for new_destination in module_destinations[destination]:
                signals_to_process.append((pulse_to_send, new_destination, destination))
        elif destination == "broadcaster":  # broadcaster
            for new_destination in module_destinations["broadcaster"]:
                signals_to_process.append((False, new_destination, "broadcaster"))
print(high_pulses * low_pulses)
