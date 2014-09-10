# -*- coding: iso-8859-15 -*-

## commen�ons par regarder la taille des types
## built-in

import sys
## en entier fait 12 bytes sur une machine 32 bits
## et 24 bytes sur une machine 64 bits

print '1', sys.getsizeof(1)

print '1L', sys.getsizeof(1L)

print 'grand entier', sys.getsizeof(23495873294572347598275973825833)

## une cha�ne de caract�re fait au minimum 22 bytes
## sur une machine 32 bits et 38 bytes sur une
## machine 64 bits
print 'a', sys.getsizeof('a')

## par contre chaque nouveau caract�re ne compte que
## pour un byte de plus dans la cha�ne
print 'ab', sys.getsizeof('ab')

print 'abc', sys.getsizeof('abc')

## None vaut 8 bytes sur une machine 32 bits
## et 16 bytes sur une machine 64 bits

print 'None', sys.getsizeof(None)

print '[]', sys.getsizeof([])
## la taille d'une liste est ind�pendante de la
## taille des objets dans une list. Elle ne garde
## que les r�f�rences
print '[1, 2]', sys.getsizeof([1, 2])
print '["sdafasd", {1, 2}]', sys.getsizeof(['sdafasd', {1, 2}])

## Donc Python utilise  beaucoup de m�moire pour chaque
## objet, heureusement les r�f�rences partag�es permettent de
## limiter le nombre d'objets en m�moire.

## Il est �galement important de comprendre qu'occuper
## de la m�moire quand on en a n'est pas un probl�me.
## Toutes les machines modernes ont plusieurs Gigabytes
## de m�moire. Les avantages de Python viennent
## au prix d'avoir des objets partout, donc une plus
## grande occupation m�moire. C'est presque toujours un
## petit prix � payer pour tant d'avantages.

## Dans les rares cas o� les types built-in consomment
## trop de m�moire pour votre usage, il est toujours
## possible d'impl�menter vos propres strucutures de
## donn�es en C et d'interfacer ces structures avec
## du code Python. Nous donnerons dans les compl�ments
## le lien de la documentation qui explique comment
## interfacer du code C et du code Python.

## regardons maintenant quelques r�sultats suprenants sur
## la performance de Python. On va utiliser pour cela
## la fonction timeit dans le module timeit. Cette fonction
## permet d'ex�cuter plusieurs fois un morceau code et retourne
## le temps d'ex�cution de ce code.

import timeit

## commen�ons par r�pondre � une question simple, � partir
## de quand vaut-il mieux utiliser les set que les listes
## dans les test d'appartance. 
print timeit.timeit(setup= "x = range(40)", stmt = '"a" in x', number = 6000000)
print timeit.timeit(setup= "x = set(range(40))", stmt = '"a" in x', number = 6000000)


print timeit.timeit(setup= "x = range(2)", stmt = '"a" in x', number = 6000000)
print timeit.timeit(setup= "x = set(range(2))", stmt = '"a" in x', number = 6000000)

print timeit.timeit(setup= "x = range(2)", stmt = '0 in x', number = 6000000)
print timeit.timeit(setup= "x = set(range(2))", stmt = '0 in x', number = 6000000)

## la liste est l�g�rement plus rapide que quand le test d'appertance
## est vrai d�s le premier �l�ment de la liste

## regardons maintenant un r�sultat tr�s surprenant pour les personnes
## habitu�es aux langages compil�s. Nous avons vu avec la surcharge
## d'op�rateur qu'il existait des m�thodes pour toutes les op�rations
## sur les built-in. Par exemple la m�thode __contains__ est appel�e
## lors du test d'appartenance avec in. Les personnes habitu�es
## aux langage compil� pourrait croire que l'appel direct � la fonction
## est plus rapide que d'utiliser l'op�rateur in. Regardons cela

print timeit.timeit(setup = "L = range(1000)", number = 30000000, stmt = "0 in L")

print timeit.timeit(setup = "L = range(1000)", number = 30000000, stmt = "L.__contains__(0)")

## L'interpr�teur Python est optimis� pour l'utilisation des op�rateurs.
## il faut donc toujours favoriser les op�rateurs sur les appels directs
## aux fonctions. 


## regardons maintenant la diff�rence de performance entre une boucle
## for et une compr�hension de liste

def f():
    L = []
    for i in xrange(1000):
        L.append(i**2)
    return L

def g():
    return [x**2 for x in xrange(1000)]

print timeit.timeit(number = 10000, stmt = f)
print timeit.timeit(number = 10000, stmt = g)

## on voir donc que la compr�hension de liste n'est pas une
## expression qui ex�cute en r�alit� une boucle for.
## Les compr�hensions sont ex�cut� plus efficacement
## que les boucles for par l'interpr�teur Python.


## nous aurions pu faire beaucoup d'autres tests, mais vous
## devez commencer � comprendre le principe. N'h�sitez
## pas � jouer avec timeit pour comprendre quels sont
## les meilleurs choix d'impl�mentation dans votre contexte. 
