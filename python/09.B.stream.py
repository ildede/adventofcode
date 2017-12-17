#!/usr/bin/python
print("Start...")

file_to_be_check = open('09.input')
rows = file_to_be_check.readlines()

for row in rows:
    garbage_chars = 0
    is_garbage = False

    index = 0
    while index < len(row):
        if not is_garbage:
            if row[index] == "<":
                is_garbage = True
            index += 1
        if is_garbage:
            if row[index] == "!":
                index += 2
            else:
                if row[index] == ">":
                    is_garbage = False
                else:
                    garbage_chars += 1
                index += 1
    print(garbage_chars)

print("...End")