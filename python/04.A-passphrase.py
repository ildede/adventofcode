#!/usr/bin/python
print("Start...")

result = 0
import csv
with open('04.input') as csvfile:
    file_to_be_check = csv.reader(csvfile, delimiter=' ')
    row_number = 0
    for row in file_to_be_check:
        row_is_valid = True
        i = 0
        while i <= len(row)-1:
            word_to_check = row[i]
            k = i+1
            while k <= len(row)-1:
                if word_to_check == row[k]:
                    row_is_valid = False
                k += 1
            i += 1
        if row_is_valid:
            result += 1
print("...End")
print(result)
