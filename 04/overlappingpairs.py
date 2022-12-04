#!/usr/bin/env python3

def part1(lines):
    result = 0
    for pair in lines:
        nums = [int(i) for r in pair.split(",") for i in r.split("-")]
        a, b, c, d = nums
        l1, l2 = b - a, d - c
        if l1 < l2:
            a, b, c, d = c, d, a, b
        # now a, b has a >= interval than c, d
        # a c d b
        if a <= c <= d <= b:
            result += 1
    print("Part 1:", result)

def part2(lines):
    result = 0
    for pair in lines:
        nums = [int(i) for r in pair.split(",") for i in r.split("-")]
        a, b, c, d = nums
        if c < a:
            a, b, c, d = c, d, a, b
        # now a <= c
        # a c b d
        if a <= c <= b or c <= b <= d:
            result += 1
    print("Part 2:", result)

with open("input") as f:
    lines = f.read().splitlines()

part1(lines)
part2(lines)
