# -*- coding: iso-8859-15 -*-

## prenons un probl�me simple, je veux afficher la liste des entiers
## de 1 � 10 et de leur carr�.
print 1, 1**2
print 2, 2**2
print 3, 3**2

## on se rend vite compte que l'on fait 10 fois la m�me tache avec
## une petite variation, la valeur de x. Les boucles for existe justement
## pour factoriser ce type de taches. Regardons comme on �crit une boucle for

for x in range(1,11):
    print x, x**2
print "on est sorti de la boucle"
## La boucle for utilise (comment souvent en Python), une notation
## simple et intuitive. On commence une boucle for par l'instruction
## for puis, on sp�cifie une variable (x dans notre cas), l'instruction
## in, et une s�quence. On fini la ligne avec un : ce qui veut
## dire que l'on va avoir un nouveau bloc d'instruction d�cal�
## de 4 caract�res vers la droite par rapport au for.
## La boucle for va r�p�ter le bloc d'instruction autant fois qu'il
## y a d'�l�ments dans la s�quence. � la premiere ex�cution du bloc
## d'instruction, la variable x r�f�rence le premier �l�ment de la s�quence
## et � chaque nouvelle r�p�tition du bloc d'instruction x r�f�rencera
## l'�l�ment suivant dans la s�quence jusq'au dernier �l�ment de la s�quence. 
## Lorsqu'il n'y a plus d'�l�ment dans la s�quence on sort de la boucle
## for, c'est-� dire que l'on continu avec le bloc de code align� avec
## la boucle for.

## comme un boucle for fonctionne sur toutes les s�quences, on peut
## faire une boucle for sur un cha�ne de caract�res par exemple
for i in 'spam':
    print i + ' ',
    
print
## ou sur une liste d'�l�ments quelconques.
L = [1, 'spam', 3.2, True]
for i in L:
    print i

#2 minutes 50 secondes

## regardons maintenant un autre probl�me. Je veux a diff�rents moments
## de mon programme faire une op�ration, par exemple, afficher
## sur la sortie standard tous les �l�ments d'une liste et leur carr�.

L1 = [1, 4, 6, 7, 10, 11, 30, 50]
for x in L1:
    print x, x**2

L2 = [3.4, 11, 22, 150.435, 18]
for x in L2:
    print x, x**2

## on voit que grace � la boucle for, je peux factoriser mon code, mais
## que malgr� tout je r�p�te deux fois exactement la m�me boucle for.
## Un moyen de factoriser encore plus ce code est d'utiliser ce que l'on
## appelle une fonction. Regardons comment on �crit une fonction

def f(L):
    for x in L:
        print x, x**2

## une fonction commence avec l'instruction def, on donne ensuite un nom
## � la fonction (f ici). puis en met entre paranth�ses l'argument de la
## fonction (L dans notre cas) et on finit une fois encore par un :
## qui signal un nouveau bloc d'instruction qui doit �tre indent� de 4
## caract�re vers la droite par rapport au premier caractere du la
## permi�re ligne de la fonction, donc le d du def. On appelle de bloc
## d'instructions le corps de la fonction. 
## Le principe d'une fonction est que le bloc d'instruction dans la fonction
## (c'est-�-dire indent� de 4 caract�res vers la droite) est ex�cut�
## � chaque appel de la fonction avec l'argument pass� au moment de la
## fonction. C'est tr�s facile d'appeler une fonction et de lui passer un
## argument, il suffit de taper le nom de la fonction suivi de l'argument
## entre parenth�ses.

f(L1)
f(L2)

# 6 minutes ##

## Une caract�ristique importante des fonctions est sa valeur de retour.
## En effet, une fonction retourne toujours un objet. Par d�faut
## elle retourne l'objet None qui est un objet vide, sans valeur,
## mais on peut d�finir un autre objet retourn� avec l'instruction
## return.

## la valeur de retour d'une fonction peut-�tre affect� � une variable
## de la mani�re suivante

r = f(L1) ## c'est None qui est retourn�.
print r

def f(L):
    for x in L:
        print x, x**2
    return 'fin du calcul'

##

r = f(L1)
print s

# 7 mintes 10 secondes
