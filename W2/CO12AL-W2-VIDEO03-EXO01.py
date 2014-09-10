# -*- coding: iso-8859-15 -*-

## une s�quence est un ensemble fini d'�l�ments ordonn�s qui sont
## index�s par des entiers commen�ant � 0

## Pour illustrer le fonctionnement des s�quences commen�ons par
## regarder les cha�nes de caract�res

s = 'egg, bacon' # dix lettres

print s[0]
print s[9]

## il existe des fonctions et des op�rations communes � toutes les s�quences
## c'est-�-dire non seulement aux cha�nes de caract�res mais aussi aux listes
## et aux tuples. Commen�ons par regarder ces fonctions et op�rations communes
## � toutes les s�quences

## test d'appartenance

print 'g' in s
print 'g' not in s # noter que c'est presque du langage naturel

## concat�nation, retourne une nouvelle s�quence de m�me type

print s + ' and spam'

## l'acc�s direct � un �l�ment par un indice n�gatif

print s[-3]

## le nombre d'�l�ments

print len(s)

## le plus petit ou plus grand �l�ment de la s�quence

print min(s)
print max(s)

## premiere occurence dans s

print s.index('g')

## nombre d'occurence

print s.count('g')

## n shallow copy de s concat�n�s, on reviendra sur la notion de shallow copy
## cette semaine.

print s*3

print '-'*30

## et pour finir on a la notion de slicing qui s'applique �
## toutes les s�quences. Le slicing permet d'obtenir une
## nouvelle s�quence qui est un sous ensemble de la s�quence
## d'origine. C'est une op�ration tr�s puissante qu'il est
## important de bien maitriser. Regardons comment le slicing
## fonctionne






