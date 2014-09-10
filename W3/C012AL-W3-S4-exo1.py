# -*- coding: iso-8859-15 -*-

## Nous avons vu la notion de shallow copie pour les s�quences

a = range(10)
a2 = a[:]

## mais on peut �galement faire une shallow copy pour un dictionnaire
## ou un set

d = {'marc' : 30, 'alice' : 35}
d2 = d.copy()

print d, d2

s = {1,2,7,89,0}
s2 = s.copy()

print s, s2

# xxx il y a un complement deja ecrit sur ce sujet, si tu veux gagner 
# un peu de temps tu peux zapper ca

## pour finir, j'aimerais aborder un probl�me d'optimisation de CPython
a = [1, 2]
b = a
print a == b
print a is b

b = [1, 2]
print a == b
print a is b

a = 18
b = 18
print a == b
print a is b

## Python r�utilise certains objets immuables (petits entiers, petites
## cha�nes de caract�res) pour minimiser la consommation m�moire. Il n'y
## a jamais de probl�mes avec les r�f�rences partag�es dans ce cas
## parce que ces objets r�utilis�s sont immuables et ne sont pas
## composites (c'est-�-dire qu'ils ne peuvent pas contenir d'autres objets). 
