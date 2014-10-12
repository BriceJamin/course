# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg

##############################
def validation (f, g, argument_tuples):
    """
retourne une liste de booleens, un par entree dans entrees
qui indique si f(*tuple) == g(*tuple)
    """
    return [ f(*tuple) == g(*tuple) for tuple in argument_tuples ]

#################### les jeux de donn�es
validation_inputs = []

########## dataset #1
from math import factorial
from operator import mul

# factoriel is still valid
fact_inputs = [(0,), (1,), (5,), ]

def fact (n):
    "une version de factoriel � base de reduce"
    return reduce (mul, range(1,n+1), 1)

validation_inputs.append ( (fact, factorial, fact_inputs) )

########## dataset #2
def broken_fact (n):
    return 0 if n <= 0 \
        else 1 if n == 1 \
             else n*fact(n-1)

validation_inputs.append ( (broken_fact, factorial, fact_inputs) )

########## dataset #3
from operator import add

# addition can work too
add_inputs = [ (2,3), (0,4), (4,5) ]

def plus (x1, x2): 
    return x1+x2

validation_inputs.append ( (add, plus, add_inputs) )

########## dataset #4
def plus_broken (x1, x2):
    if x1 != 0: 
        return x1 + x2
    else:
        return 1 + x2

validation_inputs.append ( (add, plus_broken, add_inputs) )

#################### the exercice instance
exo_validation = Exercice (validation, validation_inputs, 
                           correction_columns = (50,40,40))

