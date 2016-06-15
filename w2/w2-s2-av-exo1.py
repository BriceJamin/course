# -*- coding: iso-8859-15 -*-

## Je vous rappelle que Python utilise le typage dynamique, c'est-�-dire
## que l'on ne donne pas le type d'un objet � l'�criture du programme,
## ce type est d�termin� � l'ex'ecution. �a simplifie beaucoup l'�criture
## des programmes.

## le type entier
## pour entrer un entier, on n'a rien d'autre � faire que d'�crire
## cet entier
1

## comme on l'a vu dans la vid�o 1, on peut �galement l'affecter � une variable
i = 1

## Comment on connait le type d'un objet en Python ?
## On utilise la fonction built-in type() qui accepte comme
## argument une variable ou un objet. 

type(i)

## en python on a deux type entiers, les int et les long
i = 10 ## cod� sur 32 bits sur une machine 32 bits
l = 23480284028402840289482184018 # pr�cision illimit�e
print l * l     # pr�cision illimit�e sur les long

## Pourquoi avons nous deux types 'entier' en Python ?
## le type int est plus compact que le type long, par cons�quent
## pour les petits entiers, Python va utiliser le type int pour r�duire
## la consommation m�moire, et le type long s'il y a vraiment besoin de
## grands entiers.

## Heureusement, Python fait automatiquement la conversion
## de int vers long s'il y a besoin. Donc en pratique vous n'avez
## pas � vous pr�ocupper du type d'entier que vous utilisez

type(i + l)     

## Les d�cimaux, qu'on appelle aussi 'flottants' on une
## pr�cision limit� � environ 15 chiffres significatifs
# On s�pare la partie enti�re et d�cimale par un .
f = 4.3

## Pour finir on a les nombres complexes qui sont
## construit comme deux nombre d�cimaux. Ils ont donc
## les m�mes limitations de pr�cision. 

c = 1 + 3j

print c.real, c.imag

## On peut 'm�langer' les types num�riques dans une expression, 
## par exemple en ajoutant un entier et un flottant
## Par contre on peut perdre en pr�cision.
## Un int et un long donne toujours un long
## Un type entier (int, long) et un float donne toujours un float
## Un type entier (int, long) ou un float et un complex
## donne toujours un complex

print i + l

print i + l + f

print i + l + f + c

## On peut convertir des types de bases entre eux (avec risque l� aussi
## de perte de pr�cision ou d'information, troncation).

print int(4.32)
print long(5.3)
print float(9879729572895792375948)
print complex(10)

## op�rations de base

print 5 + 3
print 5 - 3
print -3
print 5/3       # division enti�re
print 5%3       # reste de la division enti�re
print 5/3.0     # division sur des floats
print 5/float(3)
print 5.2//3.1  # force la division sur des entiers (5.0/3.0)
print 2 ** 32   # puissances
print abs(-5.3) # valeur absolue

## pour finir, j'aimerais introduire un dernier type qui n'est pas
## � proprement parler un type num�rique, mais qui est impl�ment� comme
## tel, c'est le type bool�en. Ce type est utilis� pour le r�sultat
## de tous les tests en Python et ne contient que deux valeurs True et False
## On verra bient�t cette notion de test en Python, mais regardons un exemple
## simple pour illustrer les bool�ens

1 < 2
1 > 2

## noter la premiere lettre qui est une majuscule

## nous reviendrons tr�s bient�t sur l'utilisation des Bool�ens
