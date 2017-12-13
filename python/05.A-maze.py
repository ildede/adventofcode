#!/usr/bin/python
print("Start...")

steps = 0

lines = open('05.input').readlines()
pointer = 0
while pointer < len(lines):
    jump_distance = int(lines[pointer])
    lines[pointer] = int(lines[pointer]) + 1
    steps += 1
    pointer += jump_distance

print("...End")
print(steps)
