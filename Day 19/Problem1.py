"""Day 19 - Problem 1 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
workflows = {}
workflow = True
for line in input_text:
    if line == "":
        workflow = False
    elif workflow:
        workflow_name, instructions = line.split("{")
        instructions = instructions[:-1]
        instructions = instructions.split(",")
        workflows[workflow_name] = instructions
    else:
        values = line[1:-1].split(",")
        values = [int(value.split("=")[-1]) for value in values]
        values = {"x": values[0], "m": values[1], "a": values[2], "s": values[3]}
        current_location = "in"
        while current_location not in ("A", "R"):
            relevant_workflow = workflows[current_location]
            for step in relevant_workflow:
                if ":" in step:
                    condition, destination = step.split(":")
                    if "<" in condition:
                        letter, threshold = condition.split("<")
                        if values[letter] < int(threshold):
                            current_location = destination
                            break
                    elif ">" in condition:
                        letter, threshold = condition.split(">")
                        if values[letter] > int(threshold):
                            current_location = destination
                            break
                else:
                    current_location = step
                    break
        if current_location == "A":
            output += sum(values.values())
print(output)
