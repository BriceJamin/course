# -*- coding: iso-8859-15 -*-

## cr�ons une classe C et une sous classe sousC heritant de C

class C:
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

## sousC h�rite de C et surcharge la m�thode get_x, c'est-�-dire
## red�fini une m�thode d�j� d�finie dans une super classe. 
class sousC(C):
    def get_x(self):
        print 'x est :', self.x


c = sousC()
sc = C()

## on peut remonter tout l'arbre d'h�ritage avec la variable
##  __class__ que l'on a d�j� vu et __bases__ qui
## sur un classe retourne un tuple de ses super-classes. 

print c.__class__, c.__class__.__bases__
print sc.__class__, sc.__class__.__bases__

## On voit que donc que c et sc n'ont pas le m�me arbre d'h�ritage.
## get_x sera celle de sousC pour c et celle de C pour sc

c.set_x(10) # set_x de C
sc.set_x(20) # set_x de C

c.get_x() #get_x de sousC
sc.get_x() #get_x de sousC

## finissons par regarder les diff�rents espaces de nommage
print c.__dict__, C.__dict__, sousC.__dict__ #noter les addresses differentes
                                             # de get_x dans C et sousC

## En Python tout est un objet, et les classes sont mutables,
## on peut donc ajouter une fonction a une classe apr�s sa cr�ation

def f(self):
    print 'depuis C, x est:', self.x

## je red�finis simplement la variable get_x dans l'espace de nommage
## de C pour r�f�rencer l'objet fonction r�f�renc� par f
C.get_x = f

## et sc vois la nouvelle fonction dans C
sc.get_x()
                                            
