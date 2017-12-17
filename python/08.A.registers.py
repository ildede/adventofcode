#!/usr/bin/python
def is_valid(register, condition, steps):
    if condition == ">":
        return register > steps
    if condition == "<":
        return register < steps
    if condition == ">=":
        return register >= steps
    if condition == "<=":
        return register <= steps
    if condition == "==":
        return register == steps
    if condition == "!=":
        return register != steps
    print("non conosco ritorno false")
    return False

print("Start...")

file_to_be_check = open('08.input')
rows = file_to_be_check.readlines()

known_register = {}

for row in rows:
    instruction = row.split(" ")
    register_affected = instruction[0]
    if register_affected not in known_register:
        known_register[register_affected] = 0
    condition_register = instruction[4]
    if condition_register not in known_register:
        known_register[condition_register] = 0

for row in rows:
    instruction = row.split(" ")

    register_affected = instruction[0]
    register_operation = instruction[1]
    register_steps = int(instruction[2])

    condition_register = instruction[4]
    condition = instruction[5]
    condition_steps = int(instruction[6])

    if (is_valid(known_register[condition_register], condition, int(condition_steps))):
        if register_operation == "inc":
            known_register[register_affected] += register_steps
        if register_operation == "dec":
            known_register[register_affected] -= register_steps

print("...End")
print(max(known_register.values()))