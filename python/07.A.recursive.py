#!/usr/bin/python
from numpy import *

print("Start...")

file_to_be_check = open('07.input')
rows = file_to_be_check.readlines()
programs = list()

for x in range(0, len(rows)):
    program_of_row = rows[x].split(' ')[0]
    programs.append(program_of_row)

for x in range(0, len(programs)):
    how_many = 0
    for row in rows:
        if programs[x] in row:
            how_many += 1
    if how_many == 1:
        print(programs[x])

print("...End")