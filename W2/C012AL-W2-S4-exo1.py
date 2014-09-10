# -*- coding: iso-8859-15 -*-

## une liste est une s�quence, donc toutes les fonctions et op�rations
## que l'on a vues pour les s�quences s'appliques aux listes : en particulier
## testes d'appartenance in, not in ; concat�nation avec le signe + ;
## longeur avec la fonction built-in len ; r�cup�ration d'un �l�ment
## par son index entre crochet ; et le slicing.

## on cr�e une liste vide ainsi
a = []

## on s�pare les �l�ments d'une liste par des virgules
## notons que l'on peut directement mettre un objet dans
## la liste, ou utiliser une variable r�f�rencant l'objet

i = 4

a = [i, 'spam', 3.2, True]

print a[0]

a[0] = 20

print a

## on peut �galement directement effectuer une op�ration et r�affecter
## cette op�ration � un �l�ment de la liste. Je rappelle qu'en Python
## on �value d'abord ce qu'il y a � droite du signe �gal et ensuite
## on affecte le r�sultat � la variable de gauche.

a[0] = a[0] + 1

print a

## on peut utiliser le slicing dans une liste parce que c'est
## une s�quence

print a[1:2]

## mais comme une liste est mutable on peut affecter sur slice

a[1:2] = ['egg', 'beans']

print a

## il faut bien comprendre ce que fait cette op�ration. Python commence
## par effacer les �l�ments sp�cifi�s par le slide dans l, puis il va
## ajouter les �l�ments de la liste de droite � la place. S'il y a plus
## d'�l�ments la liste est agrandie, s'il y en a moins, elle est raccoucie

## on peut donc supprimer des �l�ments sur un slice en affectant un slice � une
## liste vide

a[1:2] = []

print a

## je peux �galement utiliser l'instruction del pour effacer tous les �l�ments
## sp�cifi�s dans un slice

del a[0:3:2]

print a

## par contre s'il on �crit L[1] = ['spam', 'good'], on va simplement ajouter
## une liste � la position 1 de la liste l

a[1] = ['spam', 'good']

print a

## avant de continuer, sur les fonctions sp�cifiques aux listes, je vais
## introduire la fonction built-in range() qui permet d'obtenir une liste
## d'entiers.

print range(10)

print range(1, 10)

print range(1, 10, 2)

## la notation de range est similaire � la notation
## que l'on a vu avec le slicing. 
range(100)[4:10:2] == range(4,10,2)
range(100)[18:12:-2] == range(18,12,-2)

## Regardons maintenant les 7 fonctions qui permettent de modifier
## les listes en place.

a = range(10)

a.append('spam')
print a

a.extend([11, 12])
print a

## ins�re l'objet juste avant la position, mais n'efface et ne remplace rien
a.insert(2, 'egg')
print a

a.sort() # attention sort ne retourne pas la liste, mais la modifie en place
print a

a.reverse()
print a

print a.pop()

print a.pop(2)

print a

a.remove(5) # efface la premiere occurence de l'�l�ment pass� en parametre

## 8 minutes
