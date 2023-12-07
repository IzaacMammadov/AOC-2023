"""Day 7 - Problem 1 of Advent of Code 2023"""
from collections import defaultdict

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
output = 0
hand_bids = []
for line in input_text:
    hand, bid = line.split()
    hand_bids.append((hand, int(bid)))
value_map = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}


def order(hand_to_consider):
    """Outputs a sorting value for each hand to be ordered by"""
    value_counts = defaultdict(int)
    tie_breaker = []
    for card in hand_to_consider:
        value_counts[card] += 1
        tie_breaker.append(value_map[card])
    match sorted(list(value_counts.values())):
        case [*_, 5]:
            type_points = 6
        case [*_, 4]:
            type_points = 5
        case [*_, 2, 3]:
            type_points = 4
        case [*_, 3]:
            type_points = 3
        case [*_, 2, 2]:
            type_points = 2
        case [*_, 2]:
            type_points = 1
        case _:
            type_points = 0
    return type_points, tie_breaker


hand_bids.sort(key=lambda hand_bid: order(hand_bid[0]))
for idx, (_, bid) in enumerate(hand_bids):
    output += (idx + 1) * bid

print(output)
