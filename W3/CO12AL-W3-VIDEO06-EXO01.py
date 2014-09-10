# -*- coding: iso-8859-15 -*-

## On peut �crire des listes, tuples, set et dictionnaires
## sur plusieurs lignes. Lorsque les �l�ments sont s�par�s
## par des virgules, on a l'habitude le mettre une virgule
## en fin de ligne plut�t qu'en d�but. On aligne chaque
## premier �l�ment de la ligne pour la lisibilit�, les espaces
## ne sont pas pris en compte. 

print [1,
       2]

print (1,
       2) 

print {1,
       2}

print {'a': 1,
       'b': 2}

print (1 + 2 + 3 +
       4)

## par contre pour les cha�nes de caract�res, on doit
## mettre un backslash en fin de ligne et tous les caract�res
## ajout�s en d�but de ligne seront pris en compte dans
## la cha�ne. 

print 'une grande\
 phrase'

# xxx comme la fois pr�c�dente, perso je ne mettrais pas l'exemple des strings
# 1. les strings multilignes sont beaucoup mieux avec des """
# 2. c'est plus utile je pense de montrer un appel de fonction - il n'y en a pas ci-dessus

    monobjet.mamethode (le_premier_argument,
                        on_doit_appeler_une_fonction (x,y,z),
                        le_dernier_argument)
