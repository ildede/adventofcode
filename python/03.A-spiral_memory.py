#!/usr/bin/python
from math import *

print("Start...")
result = 0

#Prima cosa trovo quanto è grande il quadrato che contiene quel numero
#considero solo i quadrati con lato dispari, quindi radice+1
#così ho la stessa dimensione in tutte le direzioni (su, giù, destra, sinistra)
puzzle_input = 368078
square_side = floor(sqrt(puzzle_input))+1
#calcolo il numero massimo presente in questo quadrato (il numero in basso a destra)
square_max_number = pow(square_side, 2)
#calcolo la posizione del mio numero, in che lato del quadrato si trova?
step_behind_max = square_max_number - puzzle_input
if step_behind_max < square_side:
    print("Sotto")
#in che metà mi trovo di questo lato?
#qual è il numero esattamente nel centro del lato sotto?
central_number = square_max_number - ((square_side-1)/2)
#da questo punto mi mancanono ((square_side-1)/2) passi per arrivare al centro
#quanti passi per arrivare qui?
step_behind_central = central_number - puzzle_input

result = step_behind_central + ((square_side-1)/2)
print("...End")
print(result)
