#!/usr/bin/python
print("Start...")

result = 0
import csv
with open('code02') as csvfile:
    file_to_be_check = csv.reader(csvfile, delimiter='	')
    for row in file_to_be_check:
        i = 0
        while i <= len(row)-1:
            number = float(row[i])
            k = 0
            while k <= len(row)-1:
                if k != i:
                    division = number / float(row[k])
                    if division.is_integer():
                        result += division
                k += 1
            i += 1

print("...End")
print(result)
