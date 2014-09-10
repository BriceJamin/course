# -*- coding: iso-8859-15 -*-

## L'instruction while �value un test qui peut s'�crire
## exactement comme un test dans un if. Ce test peut-�tre
## par exemple le r�sultat d'une comparaison, d'un retour
## fonction, d'un op�rateur de test bool�en (and, or, not)
## ou directement un type built-in qui vaut faux lorsque
## c'est 0, None, ou un objet vide (liste vide, set vide)
## et True dans tous les autres cas. 


## Tant que le test est vrai, le while r�p�te le
## bloc d'instruction sous le while, lorsque le
## test est faux, on sort du while. 

L = range(10)

while L.pop():
    print L

## Notons que le while, comme la boucle for, accepte
## les instructions break, pour sortir du while, et
## continue, pour remonter directement � l'�valuation
## du test. 

## Un usage fr�quent du while est le suivant. On fait
## une boucle infinie avec un while True et on sort
## de cette boucle avec un break sous une certaine
## condition. C'est un usage fr�quent lorsque l'on a
## un programme qui r�pond � des entr�es utilisateur. 
    
while True:
    s = raw_input('Quelle est votre question ?\n')
    if 'aucune' in s:
        break
    #answer(s) # fonction pour le traitement de la reponse
