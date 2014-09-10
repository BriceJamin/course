# -*- coding: iso-8859-15 -*-

## La syntaxe de la compr�hension de listes est simple
## et intuitive puisqu'elle est proche du langage naturel.
## Mais elle est �galement incroyablement puissante.
## Commen�ons par un exemple simple. Cr�ons une liste
## des carr�s des entiers allant de 0 � 10. 
## La compr�hension de liste commence toujours par un crochet
## ouvrant et termine par un crochet fermant, indiquant que le
## r�sultat est une liste. On a ensuite une expression sur
## une suivi de for, du nom de
## variable utilis� dans l'expression suivi de in et de
## l'objet it�rable que va parcourir la variable. 

print [x**2 for x in range(10)]

## On peut en plus ajouter une condition dans la
## compr�hension de liste. Par exemple si l'on veut
## les carr�s de tous les entiers allant de 0 � 100
## et qui sont divisible par 7, il suffit d'�crire

print [x**2 for x in range(101) if x % 7 == 0]

## notons que lorsque l'on lit cette expression on est proche
## du langage naturel et que la compr�hension
## remplace en une seule expression les fonctions
## built-in map et filter.




