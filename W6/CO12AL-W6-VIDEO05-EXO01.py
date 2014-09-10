# -*- coding: iso-8859-15 -*-


## Actuellement, parmi les types de base,
## seul les fichiers ont un context manager.

## with est suivi d'un objet qui a deux m�thodes
## __enter__ et __exit__. La m�thode __enter__ doit
## retourner un objet que va r�f�rencer la variable f
## __enter__ est ex�cut� avant la premi�re ligne du bloc
## d'instruction, puis on ex�cute le bloc d'instruction,
## et finalement on ex�cute __exit__(), m�me s'il y a
## une exception non captur�e. Pour les fichiers, __exit__()
## ferme simplement le fichier. 

with open(r'c:\Temp\spam.txt', 'w') as f:
    for i in range(10):
        f.write(str(i) + '\n')


## On peut �videment impl�menter un context manager
## pour nos propres objets. Regardons un exemple


class C():
    ## la m�thode __enter__ retourne en g�n�ral l'objet
    ## lui m�me
    def __enter__(self):
        print 'dans enter'
        return self

    ## la m�thode __exit__ doit retourner un bool�een
    ## Si elle retourne False, en cas d'exception,
    ## l'exception sera relanc�e, c'est le cas classique
    ## Si elle retourne True, l'exception sera captur�e

    def __exit__(self, *args):
        print 'dans exit'
        ## args contient les d�tails de l'exception
        print args
        return False

    def div(self, a, b):
        print a/b

#with C() as c:
#    c.div(1, 0)

## Si la valeur de retour de __exit__ est True, l'exception
## est captur�e.

class C():
    ## la m�thode __enter__ retourne en g�n�ral l'objet
    ## lui m�me
    def __enter__(self):
        print 'dans enter'
        return self

    ## la m�thode __exit__ doit retourner un bool�een
    ## Si elle retourne False, en cas d'exception,
    ## l'exception sera relanc�e, c'est le cas classique
    ## Si elle retourne True, l'exception sera captur�e

    def __exit__(self, *args):
        print 'dans exit'
        ## args contient les d�tails de l'exception
        print args
        return True

    def div(self, a, b):
        print a/b

#with C() as c:
#    c.div(1, 0)

