# -*- coding: iso-8859-15 -*-

## commen�ons avec quelque chose de simple
## la fonction built-in type() retourne
## ce que l'on appelle le type d'un objet
## c'est �galement �quivallent � appeler
## l'argument __class__ sur l'objet.
## Donc le type d'un objet c'est la classe
## qui a instanci� cet objet. Notons que
## cette classe est aussi un objet

print type('a')
print 'a'.__class__

## les classes new style ont �t� introduites
## pour r�pondre � deux probl�mes majeurs
## avec les classes classiques qui �taient les
## seuls � exister.
## 1) il n'est pas possible
## avec les classes classiques d'h�riter d'un
## type built-in. C'est tr�s ennuyeux parce
## que l'on peut imaginer beaucoup de cas o� l'on
## veut simplement l�g�rement modifier le comportement
## d'un type built-in. En effet, les types built-in
## sont tr�s puissant et constituent une bonne base
## de d�part pour de nouvelles classes.
## 2) le type d'une instance d'un type built-in
## est le type built-in. Mais le type d'une intance
## d'une classe classique, n'est pas la classe,
## mais un objet instance. Donc toutes les instances
## des classes classiques sont du type instance.
## c'est inconsistant avec les types built-in, en effet
## on aurait pr�f�r� que le type des instances soit
## la classe qui a cr�� l'instance.

class C:
    pass

class D:
    pass

c = C()
d = D()
## c et d on le m�me type instance
print type(c)
print type(d)

i = 1
s = 'a'
## mais le type des types built-in est bien celui
## de la classe qui l'a cr��
print type(i)
print type(s)

## les classes new-style corrigent ces deux probl�mes
## et introduisent d'autres am�liorations comme
## la notion de propri�t� ou comme un nouvel
## algorithme pour parcourir les arbres d'h�ritage
## en cas d'h�ritage multiple.
## Ces classes new-style repr�sentent une modification profonde
## du fonctionnement des classes classiques en Python. Cependant,
## dans les versions actuelles de Python 2, les 
##  classes classiques et new-style cohabitent. La principale
## raison est de ne pas casser la compatibilit� avec du code
## ancien. Il faut noter que les classes classiques sont les
## classes par d�faut en Python 2.

## Heureusement, les diff�rences entre classes classiques
## et new-style sont sur des applications avanc�es, donc
## le fait que les classes classiques soient les classes
## par d�faut pose rarement un probl�me. De plus, d�s que
## l'on est dans un cas qui � n�cessite des classes new-style
## comme l'h�ritage d'un type built-in ou d'une classe new-style
## la classe sera automatiquement new-style.

## Cependant, c'est une bonne
## habitude de toujours d�marrer un nouveau projet avec les
## classes new-style et de ne r�server les classes classiques
## que pour les projets existants utilisant d�j� des classes
## classiques. 

## regardons maintenant comment cr�er une classe new style.
## Il faut soit h�riter d'un type built-in, soit d'une classe
## new-style, soit de object. 

class C(object):
    pass

## le type de l'instance est bien la classe C
c = C()
print type(c)
print type (C)

class D(list):
    pass

## le type de l'instance est bien la classe C
d = D()
print type(d)



