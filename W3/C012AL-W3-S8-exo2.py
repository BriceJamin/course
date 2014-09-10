# -*- coding: iso-8859-15 -*-

## Prenons une liste de 3 �l�ments

L = [1, 2, 3]

## essayons d'appeler next() sur la liste L
#L.next()

## �a retourne une exception parce que la liste L
## n'est pas un it�rateur. Par contre les listes ont
## des it�rateurs.

## recup�rons l'it�rateur de cette liste

it = L.__iter__()

## nous voyons que la liste et l'it�rateur sont diff�rents
print L is it

## par contre si on appelle __iter__() sur l'it�rateur
## on remarque de l'on a le m�me objet, donc
## l'appelle de __iter__() sur un it�rateur retourne bien
## l'it�rateur lui m�me.

it2 = it.__iter__()

print it is it2

## on peut faire directement une boucle for sur l'it�rateur
## c'est �quivallent � faire une boucle for sur l'objet
## qui a cet it�rateur puisque la boucle for app�lera toujours
## en premier la fonction __iter__() sur l'objet.

for i in it:
    print i,

## par contre, une fois que l'it�rateur a retourn� tous les
## �l�ments, next() retournera toujours StopIteration, on ne
## peut donc plus faire de boucle for dessus. Il faudra dans
## ce cas cr�er un autre it�rateur.

#iterateur.next()

for i in it:
    print i, 

it3 = L.__iter__() # nouvel it�rateur

print
print it is it3

for i in it3:
    print i,
    
## Il faut faire attention lorsque l'on manipule directement des it�rateurs
## de g�n�rer un nouvel it�rateur � chaque fois que l'on fait une nouvelle
## boucle. On n'a pas de ce probl�me avec les objets qui ont des it�rateurs
## puisque la boucle for se chargera elle m�me de g�nerer un nouvelle it�rateur
    
