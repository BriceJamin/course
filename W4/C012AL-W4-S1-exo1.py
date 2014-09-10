# -*- coding: iso-8859-15 -*-

## Pour ouvrir un fichier on utilise la fonction built-in open.
## Attention, le nom de cette fonction peut-�tre trompeur.
## La fonction open ne permet pas seulement d'ouvrir un
## fichier qui existe d�j�, mais elle permet aussi de cr�er
## un nouveau fichier. En fait, le r�le exact de la fonction
## open est d�termin� par ce que l'on appel le mode d'ouverture.

## Regardons, maintenant comment cr�er un fichier, �crire
## dedans sur chaque ligne un nombre et son carr�

f = open('C:\Temp\spam.txt', 'w')

## le mode w ouvre le fichier en �criture et efface le
## contenu pr�c�dent. Attention w est une cha�ne de caract�res

## on ne peut �crire dans un fichier que des cha�nes de
## caract�res, en d'autres termes write s'attend a recevoir un string
## on utilise donc format; remarquez bien la fin de ligne qui s'�crit "\n"
for i in range(100):
    line = "{} {}\n".format(i,i**2)
    f.write(line)

f.close()
