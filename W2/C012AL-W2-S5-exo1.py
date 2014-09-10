# -*- coding: iso-8859-15 -*-

## Pour d�finir un tuple on utilise des paranth�ses

t = () #tuple vide

t = (4,) # tuple avec un seul �l�ment. Attention � la virgule � la fin,
         # Python pense que les parenth�se sont juste pour regrouper des
         # op�rations
print t
## les parenth�ses sont facultatives. !! attention �a n'est pas le cas
## avec les listes

t = 5,

## lorsque j'ai plusieurs �l�ments, je les s�pare par des virgules

t = (3, 4.1, 'spam')

t = 3, 4.1, 'spam'

## on a sur les tuples, toutes les op�rations des s�quences

print 3 in t

## par contre on ne peut pas modifier un tuple et on a donc aucune
## fonction pour modifier en place un tuple

#t[1] = 8

## on peut facilement convertir un tuple en list et une liste en tuple
## en utilisant les fonction built-in list() et tuple()

a = list(t)

print a

a.append(11)
print a

t = tuple(a)

print t
