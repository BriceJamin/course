# -*- coding: iso-8859-15 -*-

## Supposons maintenant que dans le fichier que l'on vient
## de cr�er je veuille remplacer l'espace entre le nombre
## et son carr� par une virgule, nous allons voir que grace
## � la puissance des it�rateurs cela ne demande que quelques
## lignes de code. 

## Commen�onms par ouvrir le fichier que l'on vient de cr�er
## en mode lecture
f = open('C:\Temp\spam.txt', 'r')

## et ouvrons un nouveau fichier en mode �criture
f2 = open('C:\Temp\spam2.txt', 'w')

## Les fichiers en Python sont des it�rateurs
it = f.__iter__()

print it is f

## Donc on peut faire directement une boucle for sur un
## fichier. Chaque it�ration va retourner une nouvelle
## ligne du fichier.

## Cependant, comme le fichier est directement un it�rateur
## (et non un objet qui peut avoir plusieurs it�rateurs)
## on ne peut it�rer qu'une seule fois sur un objet fichier.
## Pour it�rer de nouveau, il faut cr�er un nouvel objet
## fichier avec la fonction built-in open()

## regardons maintenant comment lire le fichier,
## remplacer les espaces par des virgules et �crire
## le r�sultat dans un nouveau fichier.

for line in f:
    f2.write(line.replace(' ', ','))

f.close()
f2.close()

             
