#!/usr/bin/python
print("Start...")

file_to_be_check = open('09.input')
rows = file_to_be_check.readlines()

for row in rows:
    score = 0
    value_of_group = 0
    is_garbage = False

    index = 0
    while index < len(row):
        if not is_garbage:
            if row[index] == "<":
                is_garbage = True
            if row[index] == "{":
                value_of_group += 1
                score += value_of_group
            if row[index] == "}":
                value_of_group -= 1
            index += 1
        if is_garbage:
            if row[index] == "!":
                index += 2
            else:
                if row[index] == ">":
                    is_garbage = False
                index += 1
    print(score)

print("...End")