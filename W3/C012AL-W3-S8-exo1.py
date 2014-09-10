# -*- coding: iso-8859-15 -*-

## Tous les types built-in ont un it�rateur, et comme une boucle
## for peut directement it�rer sur un objet qui a un it�rateur,
## on peut faire une boucle for sur tous les types built-in.

s = {1, 2, 3, 'a'}
for i in s:
    print i, 

## Mais regardons comment une boucle for fait pour utiliser
## un objet qui a un it�rateur.

## La boucle for commence par r�cup�rer l'it�rateur avec
## la m�thode __iter__() sur l'objet

print

it = s.__iter__()
print it

## ensuite, la boucle for appelle la m�thode next() pour obtenir
## chaque �l�ment de l'objet. Lorsqu'on a parcouru tous les
## �l�ments de l'objet, la m�thode next retourne une exception qui
## s'appelle StopIteration. La boucle for capture automatiquement
## cette exception et se termine

print it.next()
print it.next()
print it.next()
print it.next()
print it.next()

## �videment, vous n'avez pas � appeler vous-m�me les m�thodes
## __iter__() et next(), le but de cet exemple est de vous montrer le
## fonctionnement des it�rateurs. La compr�hension de ce
## fonctionnement sera utile lorsque vous cr�erez vos propres
## it�rateurs.

## Vous pouvez aussi avoir le sentiment que ce fonctionnement, m�me s'il
## est pratique, est lourd et lent. �a n'est pas le cas, le fonctionnement
## des it�rateurs est parmi ce qui a �t� le plus optimis� dans la machine
## virtuelle CPython. 


