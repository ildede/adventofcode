#!/usr/bin/python
print("Start...")

steps = 0

lines = open('code08').readlines()
pointer = 0
while pointer < len(lines):
    jump_distance = int(lines[pointer])
    lines[pointer] = int(lines[pointer]) + 1
    result += 1
    pointer += jump_distance

print("...End")
print(steps)
