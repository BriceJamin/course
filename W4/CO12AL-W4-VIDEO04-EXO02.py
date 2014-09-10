# -*- coding: iso-8859-15 -*-

## Une compr�hension de sets s'�crit exactement comme
## une compr�hension de listes � la diff�rence
## qu'au lieu de d�limiter la compr�hension par des crochets
## on la d�limite par des accolades.

print {i**3 for i in range(10)}

## la compr�hension de set est un moyen simple d'obtenir
## un set � partir d'une liste en effectuant au moment
## de la conversion des op�rations et des filtres. Je
## rappelle qu'en Python, le set est la meilleure stucture
## de donn�es pour faire des tests d'appartenance. 

print {i**2 + 3*i - 1 for i in range(100) if i % 11 == 0}

## Regardons maintenant la compr�hension de dictionnaire.
## Elle s'�crit exactement comme une compr�hension de set,
## sauf que l'on s�pare les clefs et les valeurs par un :

print {i : i**2 for i in range(10)}

## Cette exemple est destin� � montrer de mani�re simple
## la syntaxe de la compr�hension de dictionnaire. Mais
## il est �vident qu'un dictionnaire qui � une clef
## enti�re associe comme valeur le carr� de la clef n'a
## aucun int�r�t.

## La compr�hension de dictionnaires est par contre tr�s utile
## pour convertir un dictionnaire d�j� existant.
## Prenons un dictionnaire qui a pour clef un num�ro client
## et pour valeur un nom

d = {123 : 'marc', 145 : 'eric', 543 : 'jean'}
print d

## Les dictionnaires sont optimis�s pour acc�der � des valeurs
## lorsque l'on connait la clef. Je rappelle que le temps
## d'acc�s, d'effacement et d'insertion est constant ind�pendamment
## de la taille du dictionnaire. Cependant, trouver une clef
## correspondant � une valeur donn�e dans un dictionnaire
## est un processus it�ratif, donc lent.
## Si je connais un nom et que je veuille le num�ro client
## correspondant, je ne pourrai pas avoir une recherche efficace
## avec le dictionnaire d. Pour avoir une recherche efficace, 
## il faudrait avoir un nouveau dictionnaire qui a pour clef
## les noms (je suppose ici qu'ils sont uniques) et pour valeur
## les num�ros clients.
## 
## Avec la compr�hension de dictionnaires je peux faire �a
## tr�s simplement.

d2 = {d[k] : k for k in d}
print d2

## Je rappelle que lorsque j'it�re sur un dictionnaire, je parcours
## les clefs. 

## Je peux aussi avec la compr�hension de dictionnaires, ajouter des filtres
## comme avec les autres compr�hensions

d3 = {d[k] : k for k in d if k < 300}
print d3
