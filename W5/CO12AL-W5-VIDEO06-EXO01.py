# -*- coding: iso-8859-15 -*-

## Commen�ons avec l'op�rateur le plus courant que l'on
## appel le constructeur. C'est une m�thode qui est appel�e
## automatiquement � la cr�ation de chaque instance.
## Cette m�thode __init__ permet d'initialiser des variables
## d'instance � la contruction de l'instance. Regardons
## un exemple

class C:
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

I = C()

## si on appelle get_x avant de d'appeler set_x on
## va avoir une exception parce que la variable x
## n'a pas encore �t� cr��e dans l'espace de nommage
## de l'instance. On pourrait alors vouloir, d�s la
## cr�ation de l'instance, initialiser x � une valeur
## par d�faut, par exemple 0. On peut le faire avec
## le constructeur

#I.get_x()

class C:
    def __init__(self):
        print 'dans C'
        self.x = 0 
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

I = C()
I.get_x()

## On peut, comme pour toutes fonctions, passer des arguments
## � init

class C:
    def __init__(self, x):
        print 'dans C'
        self.x = x
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

I = C(10)
I.get_x()

## En cas d'h�ritage, le contructeur n'est appeler que sur
## la classe qui instancie l'objet et pas sur ces super-classes

class D(C):
    def __init__(self):
        print 'dans D'

I = D()

#I.get_x()

## pour appeler le contructeur de C lorsque l'on cr�e une
## instance de D, il faut le faire explicitement.

class D(C):
    def __init__(self):
        C.__init__(self, 100)
        print 'dans D'

I = D()
I.get_x()



## 5 minutes
## Pour voir les valeurs de x dans l'instance on appelle
## � chaque fois la m�thode get_x(), mais 
## on pourrait vouloir utiliser directement l'instruction
## print. C'est possible en surchargeant la m�thode __str__

class C:
    def __init__(self, x):
        print 'dans C'
        self.x = x
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x
    # doit retourner une cha�ne de caract�res
    def __str__(self):
        return str(self.x)

class D(C):
    def __init__(self):
        C.__init__(self, 100)
        print 'dans D'

## l'appel � la m�thode __str__ suit l'arbre d'h�ritage,
## donc si elle est d�finie dans la super classe, toutes
## les sous classes pourront utiliser la m�me m�thode
## lorsque print est appel�.
        
I = C(20)
J = D()
print I, J

