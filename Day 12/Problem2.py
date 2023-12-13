"""Day 12 - Problem 2 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
for row in input_text:
    arr, group_text = row.split()
    arrangement = ((arr + "?") * 5)[:-1]
    groups = [int(i) for i in group_text.split(",")] * 5
    completed = 0
    group_to_added_count = [[0 for _ in range(groups[i] + 1)] for i in range(len(groups))]
    group_to_added_count[0][0] = 1
    for char in arrangement:
        match char:
            case ".":
                for group in range(len(groups) - 1):
                    group_to_added_count[group + 1][0] += group_to_added_count[group][-1]
                completed += group_to_added_count[-1][-1]
                for group in range(len(groups)):
                    group_to_added_count[group] = [group_to_added_count[group][0]] + [0 for _ in range(groups[group])]
            case "#":
                completed = 0
                for group in range(len(groups)):
                    group_to_added_count[group] = [0] + group_to_added_count[group][:-1]
            case "?":
                completed += group_to_added_count[-1][-1]
                for group in reversed(range(1, len(groups))):
                    group_to_added_count[group] = (
                            [group_to_added_count[group][0] + group_to_added_count[group - 1][-1]]
                            + group_to_added_count[group][:-1]
                    )
                group_to_added_count[0] = [group_to_added_count[0][0]] + group_to_added_count[0][:-1]
    completed += group_to_added_count[-1][-1]
    output += completed
print(output)
