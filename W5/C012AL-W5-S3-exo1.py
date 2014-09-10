# -*- coding: iso-8859-15 -*-

## cr�ons un fichier spam.py
x = 1
def f():
    print 'x dans spam.py', x

## puis du prompt interactif jouons avec ce module
## commen�ons par importer 
import spam

## on peut acc�der aux variables du module spam en utilisant
## la notation spam.nom, nom �tant un nom de variable
print spam.x
print spam.f()

## si on cr�e un variable x, elle sera dans l'espace
## de nommage du prompte interactif et non de spam
x = 10

## x dans spam vaut toujours 1
print spam.x

## Par contre, on peut modifier x dans spam puisque les modules
## sont des objets mutables
spam.x = 2

print spam.x
spam.f()

## c'est tr�s important. Comme il n'y a qu'un seul
## objet module par module import�, par exemple
## le module spam, tous les autres modules qui importeront
## spam verrons les variables de spam modifi�es.

## En particulier, comme un module est mutable, on peut
## ajouter n'importe quel objet dans l'espace de nommage
## du module

spam.y = 100
def g():
    print spam.y ## attention le scope est textuel,
                 ## donc y est cherch� dans l'espace de
                 ## nommage du terminal interactif.
                 ## Pour bien trouver y,
                 ## il faut donner son espace de nommage
spam.g = g
spam.g()


## Regardons maintenant une autre mani�re d'importer un module

print x
from spam import x
print x

## avec l'instruction from, la variable x a �t� import�
## dans l'espace de nommage du module courant.
## Qu'est-ce que �a veut dire exactement ? On cr�e une
## variable locale x qui r�f�rence l'objet r�f�renc� par
## la variable spam.x, mais la variable x existe toujours
## dans l'espace de nommage de spam. On a donc maintenant
## deux variables x, une dans l'espace de nommage du module
## courant et une dans l'espace de nommage de x. Ces
## variables vont �voluer ind�pendemment.

spam.x = 5
x = 6
print spam.x
print x

## En r�sum�, nous avons deux mani�res d'importer des modules
## avec des propri�t�s tr�s diff�rentes. 
## L'instruction import permet d'importer un objet module. Avec
## cette importation, il y a une parfaire isolation des espaces
## de nommage puisque l'on ne peut acc�der aux variables
## du module import� qu'� partir de son nom point la
## variable, par exemple spam.x. Par contre, on a un acc�s
## direct aux variables du module, il faut donc faire
## attention si on les modifies puisqu'elles seront
## modifi�e dans l'espace de nommage du module. 

## L'autre mani�re d'importer un module est d'utiliser
## l'instruction from module import variable. Cette
## instruction va cr�er une nouvelle variable dans
## l'espace de nommage local qui r�f�rence le m�me objet 
## que la variable dans l'espace de nommage du module import�.
## L'avantage de cette importation est que l'on peut acc�der
## directement � l'objet d�fini dans le module sans utiliser
## le nom du module point le nom de la variable. 
## C'est tr�s utile pour les fonctions que l'on utilise
## tr�s souvent. 

import math
math.cos(10)

from math import cos
cos(10)

## Par contre, comme la fonction est import� dans l'espace
## de nommage local, il faut faire attention aux collisions,
## c'est-�-dire que le nom de variable import� n'existe
## par d�j� localement, sinon il sera remplac� par le
## nom de variable import�. De plus, l'instruction
## from math import cos ne va importer que la fonction cos,
## mais ni le module math, ni aucune autre fonction de math. 

