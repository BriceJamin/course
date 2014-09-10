# -*- coding: iso-8859-15 -*-

## Supposons que l'on veuille compter le nombre d'instances
## cr��es par une classe. On peut facilement maintenir un
## compteur du nombre de r�f�rence dans contructeur de la
## classe, mais l'acc�s � ce compteur n'est pas trivial.
## Regardons cela...


class C:
    nb_i = 0
    def __init__(self):
        C.nb_i  = C.nb_i + 1


C()
C()
## je peux �videmment acc�der � l'attribut de la
## classe directement. 
print C.nb_i

## Je peux aussi faire une fonction dans mon module

def num():
    return C.nb_i


print num()

## Mais cela complique la maintenance d'avoir une fonction
## travaillant sur une classe en dehors de la classe.

## Par contre, je ne peux pas faire une m�thode d'instance
## dans ma classe puisqu'il me faut une instance pour acc�der
## au compteur, et que cette instance va changer le compteur
## � sa cr�ation.

## La solution ici est d'avoir une m�thode statique.
## une m�thode statique s'�crit comme une fonction,
## mais doit �tre d�clar�e comme statique avec la
## fonction staticmethod. 

class C:
    nb_i = 0
    def __init__(self):
        C.nb_i  = C.nb_i + 1
    def num():
        return C.nb_i
    num = staticmethod(num)

C()
C()
print C.num()

## notons qu'une m�thode statique peut aussi �tre appel�e sur
## une instance, mais que l'instance n'est pas pass�e � la
## m�thode

print C().num()

## Une sous classe h�rite des m�thodes statiques, par
## contre, si la sous classe surcharge la m�thode
## statique, elle doit �tre de nouveau d�clar�e
## comme statique dans la sous classe. 

## je ne red�finis pas la m�thode statique
class SousC(C):
    pass

print SousC.num()

## je red�finis la m�thode statique
class SousC(C):
    def num():
        return 'de sousC {}'.format(C.num())
    num = staticmethod(num)

## L'inconv�nient ici est que il y a un seul compteur
## pour les instances de C et SousC

SousC()
SousC.num()

## il existe en Python un autre type de methode pour
## les classes, ce sont les m�thodes de classe.
## Lorsqu'une m�thode de classe est appel�e sur une
## classe C, elle re�oit comme premier argument une r�f�rence
## sur C. C'est tr�s int�ressant
## lorsque qu'une m�thode de classe est d�fini dans une classe
## et h�rit� dans plusieurs sous classe. Il sera ainsi
## possible de faire un traitement diff�rent en fonction
## de la sous classe. 

## On d�finit une method de class avec la fonction
## built-in classmethod()
## Si l'on revient � notre exemple, on peut avoir un
## compteur d'instance distinct pour chaque sous classe.

class C:
    nb_i = 0
    def __init__(self):
        self.count()
    ## affiche le nombre d'instances de la classe cls
    def num(cls):
        return cls.nb_i
    ## compte de nombre d'instances de la classe cls
    def count(cls):
        cls.nb_i = cls.nb_i + 1
    num = classmethod(num)
    count = classmethod(count)

class SousC(C):
    nb_i = 0

C()
C()
print C.num(), SousC.num()

