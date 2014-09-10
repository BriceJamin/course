# -*- coding: iso-8859-15 -*-

## l'instruction print permet d'afficher simplement la valeur d'un
## objet sur le terminal. On dit �galement que l'on affiche une valeur
## sur la sortie standard

## print peut aussi bien accepter une variable (et dans ce cas il affiche
## la valeur de l'objet r�f�renc� par la variable) ou directement un objet.
## regardons cela en pratique

s = 'spam'
print s

print 'egg'

## l'instruction print permet aussi d'afficher plusieurs objets ou variable
## en les s�parant par une virgule
## lorsqu'il y a une virgule entre les arguments (variable ou objet) pass�
## � print, print ajoute un espace entre les valeurs des arguments retourn�s


i = 10

print i, s


## lorsque l'on est dans le terminal interactif (et uniquement dans ce cas)
## on peut aussi directement
## taper le nom de la variable suivi d'un retour chariot.

i

## On voit ainsi la repr�sentation interne de l'objet.
## C'est la plupart du temps �quivalent � print
## La repr�sentation interne peut donner des informations
## suppl�mentaires.

