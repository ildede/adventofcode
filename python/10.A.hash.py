#!/usr/bin/python
from math import *

print("Start...")

file_to_be_check = open('10.input')
row = file_to_be_check.readline()
lenghts = row.split(",")

for x in range(0, len(lenghts)):
    lenghts[x] = int(lenghts[x])

numbers = list()
for x in range(0,256):
    numbers.append(x)

current_position = 0
skip_size = 0
for lenght in lenghts:
    if lenght <= len(numbers):
        begin_of_to_be_reversed = current_position
        end_of_to_be_reversed = current_position + lenght - 1
        if end_of_to_be_reversed >= len(numbers):
            end_of_to_be_reversed = end_of_to_be_reversed - len(numbers)
        for x in range(0, int(floor(lenght/2))):
            tmp = numbers[begin_of_to_be_reversed]
            numbers[begin_of_to_be_reversed] = numbers[end_of_to_be_reversed]
            numbers[end_of_to_be_reversed] = tmp
            begin_of_to_be_reversed += 1
            if begin_of_to_be_reversed >= len(numbers):
                begin_of_to_be_reversed = 0
            end_of_to_be_reversed -= 1
            if end_of_to_be_reversed < 0:
                end_of_to_be_reversed = len(numbers)-1
        current_position += lenght+skip_size
        skip_size += 1
        if current_position >= len(numbers):
            current_position -= len(numbers) 
print(numbers)

print(numbers[0] * numbers[1])
print("...End")