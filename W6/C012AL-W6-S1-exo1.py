# -*- coding: iso-8859-15 -*-

## Commen�ons par cr�er une fonction classique

def f():
    return 10

print f()

## notre fonction retourne 10

## cr�eons maintenant une fonction g�n�ratrice,
## il suffit pour cela de remplacer l'instruction
## return par yield

def f():
    yield 10

print f()

## on voit que cette fois la fonction ne retourne
## 10, mais un objet generator. Que faire alors avec
## cet objet ? En fait, cet objet est un it�rateur
## que l'on peut utiliser comme n'importe quel it�rateur
## dans une boucle for, avec les fonction map ou filter
## et dans une compr�hension de liste

it = f()
print it
print iter(it) is it

print it.next()
#it.next()

for i in f():
    print i

## �videmment, une fonction g�n�rateur est plus utile
## lorsqu'elle contient une boucle, soit avec for,
## soit avec while

def f(x):
    for i in range(x):
        yield 3*i**2 - 2*i + 35

for i in f(10):
    print i,

print 
print [i for i in f(100) if i%17 == 0]
