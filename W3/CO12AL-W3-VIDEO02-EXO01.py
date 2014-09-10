# -*- coding: iso-8859-15 -*-

## Il existe deux mani�res de cr�er un dictionnaire, la
## plus simple lorsque l'on cr�e un dictionnaire � la main
## est d'utiliser les accolades

d = {}

d = {'marc':35, 'alice':30, 'eric':38}

## la deuxi�me mani�re est tr�s utile lorsque les couples
## clefs-valeurs sont obtenues par une op�ration, dans
## ce cas on peut automatiquement cr�er un dictionnaire
## � partir d'une liste de tuples clef,valeur

a = [('marc', 35), ('alice', 30), ('eric', 38)]
d = dict(a)

# xxx je ferais remarquer qu'il s'agit d'un cas particulier de conversion
# comme on en a d�j� vu pour les types num�riques e.g. float(12)

## je rappelle qu'il n'y a pas d'ordre dans un dictionnaire
## donc le dictionnaire n'affiche pas n�c�ssairement
## les valeurs dans l'ordre dans lequel on les a entr�es

print d

## il existe de tr�s nombreuse op�rations et fonctions
## sur les dictionnaires, nous allons voir les principales
## commen�ons par les deux suivantes

print len(d)
print 'marc' in d
print 'marc' not in d

## m�me si les dictionnaires ne sont pas des s�quences,
## dans un soucis d'uniformit� et de simplification,
## la fonction len et l'op�rateur in ont �t� impl�ment�s
## sur les dictionnaires.

## on peut acc�der et modifier la valeur d'une clef de la
## mani�re suivante

print d['marc']
d['marc'] = 40

## on peut effacer la clef et sa valeur dans le dictionnaire
## avec l'instruction del

del d['marc']

d.copy() # shallow copie du dictionnaire
print 

## et on a des m�thodes pour r�cup�rer sous forme de liste:
## les clefs, les valeurs, et les tuples (clefs, valeur)

print d.keys()
print d.values()
print d.items()


# xxx on a a ce stade tout le bagage pour montrer ceci
#for k,v in d.items():
#    print "cle={} -> valeur={}".format(k,v)

# qui est tout de meme un truc majeur a montrer
# pour les dicts je pense
