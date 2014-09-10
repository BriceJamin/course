# -*- coding: iso-8859-15 -*-

## Pour charger un module il faut utiliser l'instruction
## import

import math

## ensuite, pour utiliser le module, on utilise le m�me nom
## que celui que l'on a utilis� pour l'import. On peut
## voir tous les attributs d'un module avec l'instruction
## dir

print dir(math)

## un attribut est une variable ref�ren�ant un objet.
## Comme en Python tout est un objet, un attribut peut
## r�f�rencer n'importe quel type d'objet : un type de base,
## une fonction, un module, ou d'autres objets que l'on
## verra dans les semaines qui viennent comme les classes.

## Pour acc�der � l'attribut d'un objet, on utilise
## le nom de l'objet - point - le nom de l'attribut. 

print math.log(10)

## et on peut bien s�r combiner des attributs de modules
## puisque ce sont de simples variables.
print math.tan(math.pi/4)


## Pour savoir � quoi correspond un attribut on peut
## utiliser la fonction built-in help()

help(math.log)

## on peut aussi appeler help() directement sur un module
## mais il a y en g�n�ral trop de texte et il est plus
## pratique de regarder directement l'aide fournie avec
## Python ou sur le Web.

help(math)

## Les fontions built-in dir() et help() ne sont pas limit�es
## aux modules et fonctionnent sur n'importe quel objet.

print dir(str)
help(str.title)

# xxx peut-etre l'occasion de rappeler comment donner la doc d'une fonction
# def foo ():
#     "un fonction qui fait le caf�"
#     pass
# 
# help(foo)
