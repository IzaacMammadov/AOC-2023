"""Day 15 - Problem 1 of Advent of Code 2023"""
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


for input_string in input_text:
    output += hash_algo(input_string)
print(output)
