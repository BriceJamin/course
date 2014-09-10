# -*- coding: iso-8859-15 -*-

## Commen�ons par cr�er une classe. Une utilise l'instruction
## class suivi du nom de la classe, puis d'un bloc d'instructions.
## Comme pour une fonction, le nom de la classe est une variable
## qui pointe vers l'objet classe qui est cr��. 


class C:
    x = 1

print C

## Cr�ons maintenant une instance de la classe C
I = C()

print I

## En Python, chaque classe et chaque instance a son propre
## espace de nommage.
## on acc�de � l'espace de nommage des objets avec la variable
## __dict__, l'espace de nommage est repr�sent� comme un
## dictionnaire

print C.__dict__, I.__dict__

## Notons que toutes les variables commen�ant et finissant
## par des double tirets bas sont des variables d�finies par
## le langage. On ne doit donc jamais cr�er de nouvelles
## variables utilisant cette notion, par contre, comme
## on le verra bient�t, on peut surcharger ces variables.

## La relation d'h�ritage permet � un
## objet d'acc�der � l'espace de nommage de l'objet dont
## il h�rite. Une instance h�rite toujours de la classe qui
## l'a cr��e, donc une instance peut toujours acc�der � l'espace
## de nommage de sa classe. Comme toujours, on acc�de � une
## variable dans l'espace de nommage d'un objet avec la
## notation objet.variable

print C.x, I.x

## Pourquoi I1.x retourne 1 alors que cette variable n'existe
## pas dans l'espace de nommage de I1. Comme on vient de le dire
## I1 h�rite de C, alors lorsqu'une variable n'est pas trouv�
## dans l'espace de nommage d'une instance, elle est automatiquement
## cherch�e dans l'espace de nommage de la classe qui l'a cr��e.

## La classe qui a cr�� une instance est r�f�renc�e par la variable
## __class__ sur l'instance 

print I.__class__, type(I.__class__)

## l'espace de nommage des instances est toujours vide
## a sa cr�ation. Mais comme les classes et les instance sont
## des objets mutables, on peut modifier leur espace de nommage.

C.x = 2

print C.x, I.x

## Non seulement la variable x dans C est chang�e, mais l'instance
## voit aussi ce changement. En effet la recherche d'une variable
## est faite dynamiquement en fonction de l'�tat de chaque objet
## au moment de la recherche. Si je cr�e une nouvelle variable dans C
## elle sera �galement vue par l'instance.

C.y = 10

## regardons les espaces de nommage
print C.__dict__, I.__dict__

## y est trouv� dans C lorsqu'on la recherche par I1, m�me si I1
## a �t� instanci�e avant l'existance de y dans la classe C. 
print I.y

## �videmment, si  y est d�finie dans l'espace de nommage de I1,
## c'est elle qui sera retourn�e

I.y = 'a'

## regardons les espaces de nommage
print C.__dict__, I.__dict__

print C.y, I.y

## Comme les modules, les classes peuvent contenir des fonctions
## que l'on appelle habituellement m�thodes. 
## Le m�thodes des classes sont des fonctions un peu particuli�res,
## elles doivent obligatoirement avoir comme premier argument
## une instance. Cela permet aux m�thodes de travailler sur les
## variables de l'instance puisque la m�thode a un r�f�rence vers
## l'instance. Regardons un exemple

class C:
    x = 1
    def f(self, a):  #self n'est qu'un nom de variable, c'est pas un mot clef
        print self.x
        self.x = a

## cr�ons une instance de C
I = C()

## Lorsque j'appelle la fonction sur l'instance, l'interpr�teur
## passe automatiquement une r�f�rence de l'instance � la fonction
I.f(5)

## python fait automatiquement cette conversion
C.f(I, 5)

print C.x, I.x




