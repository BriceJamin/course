# -*- coding: iso-8859-15 -*-

## Je vais cr�er une variable globale et une fonction
L = 10

def f():
    L = 11

print L
f()
print L

## La variable locale L est diff�rente de la
## variable gobale L

## Par contre, si l'on rajoute l'instruction global, alors
## �a veut dire que la variable L assign�e dans la fonction
## est bien la variable globale. L'instruction global permet
## de changer le scope d'une variable assign�e localement
## dans une fonction. 

def f():
    global L
    L = 11

print L
f()
print L

## global est une intruction un peu particuli�re en Python
## �a n'est pas une instruction interpr�t�e comme toutes les
## autres instruction, c'est une directive au compilateur
## qui g�n�re le byte code avant l'ex�cution. Donc, une
## variable d�finie comme �tant globale le sera pour tout le
## scope dans lequel l'instruction global est pr�sente,
## quelque soit la position de global dans ce scope.

def f():
    L = 12
    global L
f()
print L

## L est globale pour toute la fonction h(), m�me si global
## est d�finie apr�s l'assignation 'L = 12'. Attention,
## dans les nouvelles versions de Python, il sera interdit
## de mettre la directive global apr�s la variable que l'on
## veut rendre globale. Il faut donc prendre l'habitude
## de mettre global au tout d�but des fonctions. 

# 2 minutes 30

## Pour finir, comme la directive global nuit � la claret�
## du code en rendant les modifications
## aux variable globales implicite, on doit �viter de
## l'utiliser.

## En effet, il faut toujours
## privil�gier les modifications explicites par retour
## de fonction. Regardons ces deux exemples

x = 100
def f():
    global x
    x = x + 10
f()
print x

## Regardons maintenant une autre mani�re d'�crire
## le m�me code

x = 100
def f():
    return x + 10
x = f()
print x

## Maintenant, la modification de la variable globale x
## est explicite, mais on peut faire mieux en rendant aussi
## explicite l'acc�s � la variable globale x dans la
## fonction f. 

x = 100
def f(x):
    return x + 10
x = f(x)
print x

## dans le premier cas la modification de x est implicite,
## mais dans le deuxi�me cas  c'est explicite avec
## l'assignation du resultat de f() � la variable x. Il faut
## toujours privil�gier ce deuxi�me cas. 

## 4 minutes. 
