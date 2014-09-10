# -*- coding: iso-8859-15 -*-

## les s�quences sont des structures de donn�es qui
## ont �t� optimis�es pour l'acc�s, la modification,
## et l'effacement d'�l�ments par num�ro de s�quence.
## Donc lorsque je connais le num�ro de s�quence
## d'un �l�ment, la vitesse d'acc�s, de modification,
## et d'effacement est ind�pendante de la position
## de l'�l�ment dans la s�quence. 
##
## Mais comment se comporte une s�quence avec
## le test d'appartenance...

def f(a):
    for i in range(5):
        print 'x' in a

f(range(10))
f(range(50000000))

## on voit que le test d'appartenance est fonction du nombre
## d'�l�ments dans la s�quence. C'est normal puisque le seul
## moyen de trouver un �l�ment dans une s�quence est de la
## parcourir s�quentiellement. Donc si on teste un �l�ment
## qui n'est pas dans la s�quence on doit comparer cet
## �l�ment avec tous ceux de la s�quence, plus il y a d'�l�ments
## plus c'est long. 

## Cependant, le test d'appartenance est une op�ration tr�s
## courante, par cons�quent, il serait tr�s utile d'avoir
## une structure de donn�es optimis�e non seulement pour
## l'acc�s, la modification et l'effacement, mais aussi pour
## le test d'appartenance.

## Mais, il y a une autre limitation des s�quences. Supposons
## que je veuille utiliser autre chose que des entiers comme
## indice, par exemple des cha�nes des caract�res pour faire
## un annuaire, �a n'est pas possible avec les s�quences.

a = []
#a['diane'] = '0118252627'

## il existe une structure de donn�es qui permet un acc�s
## une modification, un effacement et un test d'appartenance
## avec une performance ind�pendante de la taille de la
## structure, et qui, de plus, permet d'avoir des indices
## d'un type immuable quelconque, c'est la table de hash.
## regardons comment fonctionne une table de hash

