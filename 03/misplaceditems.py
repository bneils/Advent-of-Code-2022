#!/usr/bin/env python3
with open("input.txt") as f:
    lines = f.read().splitlines()

def itprior(el):
    el = ord(el)
    a, z, A, Z = map(ord, "azAZ")
    if a <= el <= z:
        return el - a + 1
    elif A <= el <= Z:
        return el - A + 1 + (z - a + 1)

def part1(lines):
    total = 0
    for line in lines:
        m = len(line) // 2
        el = (set(line[:m]) & set(line[m:])).pop()
        total += itprior(el)
    print("Part 1:", total)

def part2(lines):
    total = 0
    for i in range(0, len(lines), 3):
        a, b, c = lines[i:i + 3]
        badge = (set(a) & set(b) & set(c)).pop()
        total += itprior(badge)
    print("Part 2:", total)

part1(lines)
part2(lines)
