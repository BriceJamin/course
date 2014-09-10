# -*- coding: iso-8859-15 -*-

## Nous avons d�j� vu la d�claration d'arguments ordonn�es

def agenda(nom, prenom, tel):
    return {'nom' : nom , 'prenom' : prenom,
            'tel' : tel}

## et l'appel de fonction avec le passage d'arguments
## ordonn�s.

d = agenda('durant', 'marc', '0720202020')
print d

## Il y a cependant un probl�me avec cet appel : on doit
## conna�tre l'ordre des arguments. Lorsqu'il y a beaucoup
## d'arguments et que le nom des arguments est bien choisi
## il est plus facile de se souvenir du nom des arguments
## que de leur ordre. C'est pourquoi, il est possible
## d'appeler une fonction en pla�ant les arguemnts dans
## un ordre quelconque du moments qu'on les nomme

d = agenda(tel='0720202020', nom='durant', prenom='marc')

## M�me s'il est possible de m�langer des arguments ordonn�s
## et des arguments nomm�s lors de l'appel, �a n'a
## pas de sens de le faire. En effet, soit on connait l'ordre
## des arguments et dans ce cas on utilise des arguments
## ordonn�s lors de l'appel. Soit on ne connait pas l'ordre
## alors on utilise des arguments nomm�s. Si on les m�langes
## cela peut conduire � des erreurs subtiles que nous
## d�taillerons dans les compl�ments. 

## Si l'on revient � notre d�claration de fonction,
## on pourrait vouloir cr�er une entr�e dans l'agenda
## sans donner un t�l�phone. On pourrait donc appeler
## notre fonction avec un cha�ne vide au lieu du num�ro
## ou avec un point d'int�rogation. Mais si notre programme
## a un comportement sp�cifique lorsqu'il n'y a pas de num�ro
## il est important que ce champ num�ro soit toujours le
## m�me lorsqu'il n'est pas fourni lors de l'appel.
## Le moyen le plus simple est d'utiliser les arguments
## par d�faut. Regardons un exemple

def agenda(nom, prenom, tel='na'):
    return {'nom' : nom , 'prenom' : prenom,
            'tel' : tel}

## si on ne founit pas l'argument lors de l'appel, c'est
## l'argument par d�faut qui est utilis�.
print agenda('durant', 'marc')

##sinon c'est l'argument que l'on passe. 
print agenda('durant', 'marc', '0720202020')

## lorsque dans la d�claration de notre fonction on a des
## arguments ordonn�s et des arguments par d�faut,
## il faut toujours mettre les arguments ordonn�s en premier
## et les arguments par d�faut apr�s. On ne peut pas les
## m�langer. 

## Nous avons donc vu deux mani�res de d�clarer les arguments
## d'une fonction : arguments ordonn�s et arguments par d�faut.
## Nous avons dit qu'il y avait 4 mani�res en tout, il nous
## en reste donc deux � voir.

## regardons maintenant la forme *. C'est un nom �trange
## pour quelque chose de tr�s simple. Regardons un exemple

def f(*t):
    print t

## le nom Targs est juste un nom de variable, on peut prendre
## n'importe quel nom seul l'�toile est importante. Avec
## cette maniere de d�clarer les arguments, on peut passer
## une liste quelconque qui sera mise dans un tuple
## r�f�renc� par la variable Targs. 

f(1, 2, 3, 'a')

## il nous reste une derni�re forme � voir, la forme **.
## Ici encore c'est un nom �trange pour quelque chose
## de simple, regardons alors un exemple...

def f(**d):
    print d

## Ici aussi, Dargs est juste un nom de variable, seule
## la double * est importante. Avec cette d�claration
## d'arguments, on pourra appeler notre fonction avec
## des arguments nomm�s et ces arguments seront mis
## dans un dictionnaire avec pour clef le nom de l'argument
## et pour valeur l'argument pass�.

f(nom='durant', prenom='marc', tel='0720202020')

## On peut combiner les 4 d�clarations d'arguments, mais
## toujours dans l'ordre suivant arguments ordonn�s,
## arguments par d�faut, forme *, forme **. Cependant,
## il ne faut pas que �a nuise � la compr�hension, c'est
## pourquoi on recommande d'�viter de m�langer plus
## de deux mani�res. 

# 7 minutes

## Pour finir, il nous reste encore � voir deux mani�re
## d'appeler une fonction. Regardons un exemple

def f(a, b):
    print a, b

## Ma fonction prend deux arguments, mais supposons
## que j'ai mes arguments � passer � la fonction dans une liste
L = [1, 2]

## je peux passer L[0] comme premier argument et L[1]
## comme deuxi�me, mais je peux aussi utiliser une forme
## * qui permet de passer les �l�ments d'une s�quence
## comme arguments d'une fonction

f(*L)

## Supposons, maintenant que j'ai mes arguments dans un
## dictionnaire
d = {'a' : 1, 'b' : 2}

## je peux utiliser ce dictionnaire pour passer des arguments
## nomm�s � ma fonction avec une forme **, il faut �videment
## que chaque clef du dictionnaire corresponde au nom d'un
## argument de la fonction

f(**d)

## comme pour la d�claration des arguments, on peut combiner
## les diff�rents appels, mais il faut ici aussi �viter de le
## faire d'autant plus que cela peut conduire � des erreurs
## subtiles que nous verrons dans les compl�ments. C'est
## donc une bonne pratique de se limiter � une seule mani�re
## d'appeler une fonction.

# 8 minutes 40 secondes
