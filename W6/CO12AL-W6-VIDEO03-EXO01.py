# -*- coding: iso-8859-15 -*-

def f(a, b):
    x = a / b

## si b est 0, il y aura une exception ZeroDivisionError
## On voit que l'exception a un nom sp�cifique et
## contient un message d'explication. C'est 
## le cas pour toutes les exceptions built-in

#f(1,0)

## Heureusement, il est possible de capturer une exception
## pour continuer le programme. 
## Les exceptions se capture avec l'instruction try/except

def f(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print "Division par 0"        
    print 'continuons...'

print f(10, 2)
print f(1,0)

## mais maintenant, comment afficher le r�sultat que s'il
## n'y a pas d'exception. On pourrait mettre un print juste
## apr�s x = a/b. S'il y a une exception le print n'est pas
## ex�cut�, et s'il n'y a pas de exception il est ex�cut�
## Cependant, l'instruction print pourrait elle m�me g�n�rer
## une exception et �tre capturer par erreur.

def f(a, b):
    try:
        x = a/b
        print b/a #au lieu de faire str(x)
    except ZeroDivisionError:
        print "Division par 0"        
    print 'continuons...'

f(0, 2)

## Une bonne pratique et de ne mettre entre le try/except
## que l'instruction ou l'ensemble d'instructions
## que l'on veut �valuer pour une exception donn�e.
## On peut alors mettre le code qui doit �tre ex�cut�
## que s'il n'y a pas d'exception dans une clause else

def f(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print "Division par 0"
    else:
        print x
    print 'continuons...'
    
f(2, 0)
f(10,2)

## Lorsqu'il y a une exception non captur�e le programme
## s'arr�te � la ligne de l'exception. Cependant, il y a des
## cas dans lequels on veut ex�cuter une derniere instruction
## m�me s'il y a une exception non captur�e. C'est
## par exemple le cas lorsque l'on travaille sur des fichiers.
## il faut toujours fermer les fichiers avant que le programme
## ne s'arr�te. Il existe
## pour cela la clause finally. La clause finally s'ex�cute
## toujours m�me en cas d'exception non captur�e.

def f(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print "Division par 0"
    else:
        print x
    finally:
        print 'dans finally'
    print 'continuons...'

#f(1, 'b')

## on peut �galement avoir plusieurs except pour un m�me try
def f(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print "Division par 0"
    except TypeError:
        print "Il faut des int !"
    else:
        print x
    finally:
        print 'dans finally'
    print 'continuons...'

f(1, 'b')

## Il est �galement possible de r�cup�rer l'instance de
## l'exception g�n�r�e pour en afficher son contenu.
## les informations de l'exceptions sont toujours
## stock�e dans le tuple args

def f(a, b):
    try:
        x = a/b
    except ZeroDivisionError as i:
        print "Division par 0", i.args
    except TypeError as i:
        print "Il faut des int !", i.args
    else:
        print x
    finally:
        print 'dans finally'
    print 'continuons...'

f(1, 'b')
f(1,0)

## 6 minutes 50 secondes
