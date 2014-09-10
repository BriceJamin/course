# -*- coding: iso-8859-15 -*-

## Je rappelle que l'on d�finit une fonction avec le mot clef
## def suivi du nom de la fonction, d'une liste quelconque
## d'arguments entre parenth�ses, s�par�s par des virgules
## suivi de : et d'un bloc d'instruction indent� de 4 caract�res
## vers la droite.

def f(a, b, c):
    print a, b, c

f(1,2,3)

## En Python tout est un objet. Une fonction est donc un objet
## et le nom de la fonction n'est qu'une variable r�f�ren�ant
## l'objet fonction. On peut donc renomer une fonction simplement
## en affectant l'objet � une nouvelle variable

g = f
g(1,2,3)

## Comme en Python tout est un objet, on a un surco�t m�moire
## pour tout en Python. Il faut donc minimiser les cr�ations
## d'objets et Python est tr�s efficace pour cela. En particulier,
## en Python, on ne duplique jamais les objets (sauf �
## faire explicitement une copie). Les arguments que l'on
## passe � une fonction sont donc toujours des r�f�rences
## vers les objets (et jamais une copie d'objet). Les passages
## d'arguments aux fonctions cr�ent donc des r�f�rences
## partag�es vers les objets. On a vu que lorsque l'objet est
## immuable, les r�f�rences partag�es ne pose aucun probl�me,
## mais lorsque l'objet est mutable, il faut faire attention
## aux effets de bord.

L = []

def h(a):
    a.append(1)

print L
h(L)
print L

## On peut donner une valeur de retour � notre fonction
## avec l'instruction return. Cette valeur de retour
## peut �tre assign�e � une variable lors de l'appel
## de la fonction. S'il n'y a pas de return, la fonction
## retourne None.

print h(L)

def h(a):
    a.append(1)
    return a

x = h(L)
print x

## Return peut appa�tre n'importe ou dans une fonction et
## il peut m�me y avoir plusieurs return. Cependant, le
## premier return rencontr� lors de l'ex�cution du code de
## la fonction sortira imm�diatement de la fonction.

def f(a, b, c):
    if b < 10:
        return a
    else:
        return c

print f(1, 11, 2)

# 4 minutes 20

## il y a un autre point important que je voudrais aborder
## dans cette introduction g�n�rale des fonctions. Lorsque
## le code d'une fonction est �valu�, c'est-�-dire lorsque
## l'on tape un retour chariot au prompt interactif apr�s la
## d�finition d'une fonction, ou
## lorsque l'on ex�cute un fichier .py contenant une fonction
## l'objet fonction est cr��, mais le code dans le corps de
## la fonction n'est pas evalu�. Ce code ne sera �valu� qu'�
## l'appel de la fonction. Cela permet � une fonction
## d'utiliser du code non encore impl�ment� au moment de
## la d�finition de la fonction, mais impl�ment� plus tard.
## regardons un exemple.

def f(a):
    func(a)

print f # on a bien un objet fonction
#f(1)   # mais on a une exception lors de l'appel puisque func
        # n'existe pas encore. 

def func(a):
    print a

f(1)

# 5 minutes 30

## Pour finir, je vais vous parler de polymorphisme. J'ai
## horreur de ce mot p�dant qui m'a effray� lorsque j'ai
## d�couvert la programmation objet, alors qu'il
## repr�sente un concept tout simple.

## Une fonction est polymorphe lorsqu'elle accepte en argument
## des objets de n'importe quel type. En Python, le typage est
## dynamique, donc toutes les fonctions sont naturellement
## polymorphes. Regardons un exemple

def my_add(a, b):
    print "j'ajoute", a, "et", b
    return a + b

my_add(1,2)
my_add(1.5,2.3)
my_add('spam', 'good')
my_add([1], [2])


