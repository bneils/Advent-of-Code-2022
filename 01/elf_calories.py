#!/usr/bin/env python3
"""Find the amount of calories that the elf with the most calories has"""

with open("input") as f:
    calorie_lines = f.readlines()

elves = []
elf_calories = 0
for calorie_line in calorie_lines:
    if not calorie_line.rstrip():
        elves.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories += int(calorie_line)
elves.append(elf_calories)

print("Part 1:", max(elves))

top_three = sorted(elves, reverse=True)[:3]
print("Part 2:", sum(top_three))
