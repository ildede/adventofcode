#!/usr/bin/python
from numpy import *

class Program(object):
    name = ""
    weight = ""
    childs = list()
    # The class "constructor" - It's actually an initializer 
    def __init__(self, name, weight, childs):
        self.name = name
        self.weight = weight
        self.childs = childs

def new_program(name, weight, childs):
    program = Program(name, weight, childs)
    return program

def total_weight_of_program(name, programs):
    for prog in programs:
        if prog.name == name:
            weight = 0
            weight += prog.weight
            for child in prog.childs:
                weight += total_weight_of_program(child, programs)
            return weight

print("Start...")

file_to_be_check = open('07.input')
rows = file_to_be_check.readlines()
programs = list()

for x in range(0, len(rows)):
    name_of_row = rows[x].split(' ')[0]
    weight_of_row = int(rows[x].split(')')[0].split('(')[1])
    splitted = rows[x].split('->')
    if len(splitted) > 1:
        childs_of_row = rows[x].split('->')[1].replace("\n","").replace(" ","").split(',')
    else:
        childs_of_row = list()
    programs.append(new_program(name_of_row, weight_of_row, childs_of_row))

wrong_programs = list()
for program in programs:
    if len(program.childs) > 0:
        weights = list()
        for child in program.childs:
            weights.append(total_weight_of_program(child, programs))
        if max(weights) > min(weights):
            wrong_programs.append(program)

for program in wrong_programs:
    print(program.name)
    print(program.weight)
    print(program.childs)
    for child in program.childs:
        print(total_weight_of_program(child, programs))

print("...End")