# -*- coding: iso-8859-15 -*-

## Lorsque l'on importe un module on utilise l'instruction
## import suivi du nom du module. Ce nom a deux r�les,
## Le premier est de donner le nom du fichier devant
## �tre import� pour cr�er l'objet module. Le deuxi�me
## est de donner le nom de la variable qui pointera vers
## l'objet module import�. Prenons l'exemple du module os. 

import os

## os est une variable qui pointe vers l'objet module os
print os

## mais c'est �galement un nom de fichier, le fichier os.py
## vous pouvez voir que le fichier de l'objet module
## s'appelle os.pyc, nous allons revenir dessus. 

## Revenons sur le processus d'importation. Ce processus
## se d�roule en trois �tapes.

## La premi�re �tape consiste � trouver le fichier module
## sur le disque dur. L'interpr�teur va chercher le module
## � importer dans le r�pertoire courant, c'est-�-dire,
## dans le repertoire duquel vous avez lancer Python. Si vous
## avez lanc� Python depuis un raccourci, le r�pertoire
## courant sera celui d'installation de Python sur votre
## syst�me. Si l'interpr�teur Python ne trouve pas le fichier
## il va chercher dans les r�pertoires contenus dans la
## variable d'environement syst�me PYTHONPATH.

## utilisons os.environ qui est un dictionnaire qui contient
## toutes les variables d'environement dans le syst�me.

print os.environ.get('PYTHONPATH', '') ## PYHTONPATH n'est pas
                                       ## n�cessairement sur le
                                       ## syst�me

## Si le fichier n'est toujours pas trouv�, il sera cherch�
## dans le r�pertoire des librairies standards.

## Tous les chemins suivis par l'interpr�teur sont dans
## la variable  sys.path
import sys
print sys.path


## Comme il s'agit d'une liste il est possible de la modifier
## en cours d'ex�cution du programme.

## La deuxi�me �tape consiste � compiler le fichier module
## en byte code. Attention, il ne s'agit pas de code machine
## mais de code pr�par� � �tre ex�cut� directement sur une
## machine virtuelle. Le fichier compil� finit par un .pyc
## Comme cette op�ration prend du temps, elle n'est ex�cut�e
## que si le fichier .pyc n'existe pas encore ou si le
## fichier source .py a chang� depuis la derniere compilation.

## Pour finir, l'interpr�teur Python va ex�cuter le fichier
## module (en fait, il va ex�cuter le byte code) pour cr�er
## l'objet module est tous les objets qu'il contient. 
## L'interpr�teur va ex�cuter le code sequentiellement en
## cr�ant chaque objet au fur et � mesure. Les fonctions
## sont un cas un peu particulier. L'objet fonction est bien
## cr�� � l'import s�quentiel du module. Par contre, le code
## contenu dans le corps de la fonction ne sera ex�cut�
## qu'a l'appel de la fonction.

## Ouvrons un �diteur IDLE pour comprendre cette ex�cution
## s�quentielle

#f()
#def f():
#    print 'dans f()'
#    g()

## l'objet fonction f() est maintenant cr��

#f()
#def g():
#    print 'dans g()'

## l'objet fonction g() est maintenant cr��

#f()
