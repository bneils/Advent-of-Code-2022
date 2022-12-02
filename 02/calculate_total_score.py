#!/usr/bin/env python3
"""Calculate the total score you would receive in the rock-paper-scissors
tournament if you were to follow the strategy guide."""

with open("input") as f:
    rows = f.readlines()

shape_values = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

# A & X = Rock
# B & Y = Paper
# C & Z = Scissors

LOSS_VALUE = 0
DRAW_VALUE = 3
WIN_VALUE = 6

outcome_values = {
    "AX": DRAW_VALUE,
    "AY": WIN_VALUE,
    "AZ": LOSS_VALUE,
    "BX": LOSS_VALUE,
    "BY": DRAW_VALUE,
    "BZ": WIN_VALUE,
    "CX": WIN_VALUE,
    "CY": LOSS_VALUE,
    "CZ": DRAW_VALUE,
}

part2_outcome_values = {
    "X": LOSS_VALUE,
    "Y": DRAW_VALUE,
    "Z": WIN_VALUE,
}

total_score = 0
part2_total_score = 0
for row in rows:
    opponent_move, your_move = row.split()
    total_score += outcome_values[opponent_move + your_move]
    total_score += shape_values[your_move]

    outcome_value = part2_outcome_values[your_move]
    part2_total_score += outcome_value
    your_actual_move = None
    for key, val in outcome_values.items():
        if key[0] == opponent_move and val == outcome_value:
            your_actual_move = key[1]
    part2_total_score += shape_values[your_actual_move]

print("Part 1:", total_score)
print("Part 2:", part2_total_score)
