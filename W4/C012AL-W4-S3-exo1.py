# -*- coding: iso-8859-15 -*-

## La syntaxe d'une fonction lambda est simple.
## Elle commence par le mot clef lambda, suivi
## d'une liste d'arguments s�par�s par des virgules
## et d'une expression pouvant utiliser ses arguments.

lambda x: x**2 + 2*x -1

## Cependant les fonctions lambda n'ont pas de nom
## alors comment les utiliser ? Le r�sultat
## de l'�valuation du code de la fonction lambda est une
## r�f�rence vers l'objet fonction qui vient d'�tre cr��

## On peut donc utiliser une fonction lambda de deux
## manieres, soit on lui donne un nom en l'assignant �
## une variable, soit on la d�finit directement l� o�
## elle va �tre utilis�e. 

f = lambda x: x**2 + 2*x - 1

print f(1)

L = [lambda x: x**2 + 2*x - 1, lambda x: x**3 -2]

print L[0](10), L[1](10)

## on peut �galement directement passer une fonction
## lambda � une fonction

def func(x):
    for i in range(10):
        print i, x(i)

## Je suppose lors de l'�criture de ma fonction func
## que l'argument x sera une fonction. Si x n'est pas
## une fonction j'aurai une exception

# func(1)

func(lambda x: x**2 -3)

## il est tr�s important de comprendre que je peux
## faire exactement la m�me chose avec une fonction
## classique. Apr�s tout en Python, tout est un objet
## et une variable n'est qu'un nom qui r�f�rence un
## objet, en particulier, le nom d'un fonction
## r�f�rence l'objet fonction d�fini par le def.

def g(x):
    return x**2 -3
func(g)

## la fonction lambda permet simplement d'�crire
## plus rapidement une fonction qui est limit�e
## � une seule expression. En effet, dans une fonction
## lambda, on ne peut pas mettre d'instructions comme
## des if ou des for. 

# 4 minutes

## Un usage classique des fonctions lambda en Python est
## de les utiliser avec les fonctions built-in map() et
## filter().

## Je vous rappelle qu'en Python les it�rateurs sont au coeur
## de la programmation et qu'avec les boucles for,
## on peut de mani�re simple et efficace exploiter la
## puissance des it�rateurs. Il existe cependant d'autres
## moyen d'exploiter les it�rateurs en Python comme les
## fonctions map et filter que nous allons voir maintenant. 

## La fonction map prend comme argument une fonction et
## un objet it�rable, et retourne une liste de la fonction
## appliqu�e � chaque �l�ment de l'objet it�rable. 

print map(g, range(10))

## les fonctions lambda permette d'avoir un code
## plus compact et plus rapide � �crire. Ce code
## est aussi plus facile � lire pour ceux habitu�s
## � la syntaxe des fonctions lambda, mais plus difficile
## � lire pour les d�butants. On s'habitue cependant vite
## aux fonctions lambda. 

print map(lambda x: x**2 -3, range(10))

## regardons maintenant la fonction filter. Comme la fonction
## map, la fonction filter prend comme argument une
## fonction et un objet it�rable, mais elle retourne une
## liste des �l�ments de l'objet it�rable pour les lequels
## la fonction retourne True. Je vous rappelle qu'en Python
## 0, None, les types de base vides et False sont faux, tout le
## reste est vrai.

## regardons un exemple de fonction filter, je veux
## obtenir tous les �l�ments d'une s�quence qui sont pairs.

print filter(lambda x: x % 2 == 0, range(10))

## ou divisible par 3
print filter(lambda x: x % 3 == 0, range(10))


# 6 minutes 30 seconces
