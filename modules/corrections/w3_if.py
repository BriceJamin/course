# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

inputs_dispatch1 = [(a, b) for a in range (3, 6) for b in range (7, 10)]

# @BEG@ 3 7 dispatch1
def dispatch1(a, b):
    """dispatch1 comme sp�cifi�"""
    # si les deux arguments sont pairs
    if a%2 == 0 and b%2 == 0:
        return a*a + b*b
    # si a est pair et b est impair
    elif a%2 == 0 and b%2 != 0:
        return a*(b-1)
    # si a est impair et b est pair
    elif a%2 != 0 and b%2 == 0:
        return (a-1)*b
    # sinon - c'est que a et b sont impairs
    else:
        return a*a - b*b
# @END@

exo_dispatch1 = Exercice(dispatch1, inputs_dispatch1)

####################
samples_A = [(2, 4, 6), [2, 4, 6]]
samples_B = [{6, 8, 10}]

inputs_dispatch2 = [
        (a, b, A, B) for a, A in zip(range(3, 5), samples_A) for b in range(7, 10) for B in samples_B
]

# @BEG@ 3 7 dispatch2
def dispatch2(a, b, A, B):
    """dispatch2 comme sp�cifi�"""
    # les deux cas de la diagonale \ 
    if (a in A and b in B) or (a not in A and b not in B):
        return a*a + b*b
    # sinon si b n'est pas dans B
    # ce qui alors implique que a est dans A
    elif b not in B: 
        return a*(b-1)
    # le dernier cas, on sait forc�ment que
    # b est dans B et a n'est pas dans A
    else:
        return (a-1)*b
# @END@

exo_dispatch2 = Exercice(dispatch2, inputs_dispatch2,
                          correction_columns=(50, 30, 30))

