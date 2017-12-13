#!/usr/bin/python
print("Start...")

result = 0
import csv
with open('code02') as csvfile:
    file_to_be_check = csv.reader(csvfile, delimiter='	')
    for row in file_to_be_check:
        num_max = 0
        num_min = 999999
        for cell in row:
            number = int(cell)
            if number > num_max:
                num_max = number
            if number < num_min:
                num_min = number
        difference = num_max - num_min
        result += difference

print("...End")
print(result)
