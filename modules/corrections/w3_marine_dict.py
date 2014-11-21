# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

# @BEG@ 3 2 index
def index(bateaux):
    """
    Calcule sous la forme d'un dictionnaire index� par les ids
    un index de tous les bateaux pr�sents dans la liste en argument
    Comme les donn�es �tendues et abr�g�es ont toutes leur id 
    en premi�re position on peut en fait utiliser ce code
    avec les deux types de donn�es
    """
    # c'est une simple compr�hension de dictionnaire
    return { bateau[0]: bateau for bateau in bateaux}
# @END@

# @BEG@ 3 2 index
def index2(bateaux):
    """
    La m�me chose mais ne mani�re it�rative
    """
    # si on veut d�cortiquer
    resultat = {}
    for bateau in bateaux:
        resultat [bateau[0]] = bateau
    return resultat
# @END@

class ExerciceIndex(Exercice):

    # on surcharge correction pour capturer les arguments
    def correction(self, student_index, bateaux):
        self.datasets = [((bateaux, ), {})]
        return Exercice.correction(self, student_index)

    # une fonction pour exposer le resultat attendu
    def resultat(self, bateaux):
        return self.solution(bateaux)

exo_index = ExerciceIndex(index, "inputs_gets_overridden")
    

# @BEG@ 3 2 merge
def merge(extended, abbreviated):
    """
    Consolide des donn�es �tendues et des donn�es abr�g�es
    comme d�crit dans l'�nonc�
    Le co�t de cette fonction est lin�aire dans la taille 
    des donn�es (longueur des listes)
    """
    # on initialise le r�sultat avec un dictionnaire vide
    result = {}
    # pour les donn�es �tendues
    for ship in extended:
        # on affecte les 6 premiers champs
        # et on ignore les champs de rang 6 et au del�
        id, latitude, longitude, timestamp, name, country = ship[:6]
        # on cr�e une entr�e dans le r�sultat, 
        # avec la mesure correspondant aux donn�es �tendues
        result[id] = [name, country, (latitude, longitude, timestamp)]
    # maintenant on peut compl�ter le r�sultat avec les donn�es abr�g�es
    for id, latitude, longitude, timestamp in abbreviated:
        # et avec les hypoth�ses on sait que le bateau a d�j� �t� 
        # inscrit dans le r�sultat, donc on peut se contenter d'ajouter 
        # la mesure abr�g�e correspondant au bateau
        result[id].append((latitude, longitude, timestamp))
    # et retourner le r�sultat
    return result
# @END@

# @BEG@ 3 2 merge
def merge2(extended, abbreviated):
    """
    Une deuxi�me version
    """
    # on initialise le r�sultat avec un dictionnaire vide
    result = {}
    # on remplit d'abord � partir des donn�es �tendues
    for ship in extended:
        id = ship[0]
        # on cr�e la liste avec le nom et le pays
        result[id] = ship[4:6]
        # on ajoute un tuple correspondant � la position
        result[id].append(tuple(ship[1:4]))
    # pareil que pour la premi�re solution,
    # on sait d'apr�s les hypoth�ses
    # que les id trouv�es dans abbreviated
    # sont d�ja pr�sentes dans le resultat
    for ship in abbreviated:
        id = ship[0]
        # on ajoute un tuple correspondant � la position
        result[id].append(tuple(ship[1:4]))
    return result
# @END@

# @BEG@ 3 2 merge
def merge3(extended, abbreviated):
    """
    Une troisi�me solution
    """
    # ici on va tirer profit du fait que les id sont
    # en premi�re position dans les deux tableaux
    # aussi si on les trie on va mettre les deux tableaux 'en phase'
    #
    # c'est une technique qui marche dans ce cas pr�cis
    # parce qu'on sait que les deux tableaux contiennent des donn�es
    # pour exactement le m�me ensemble de bateaux
    # 
    # ici on a deux choix, selon qu'on peut se permettre ou non de
    # modifier les donn�es en entr�e. Supposons que oui:
    extended.sort()
    abbreviated.sort()
    # si �a n'avait pas �t� le cas on aurait fait plut�t
    # extended = extended.sorted() et idem pour l'autre
    #
    # il ne reste plus qu'� assembler le r�sultat
    # en d�coupant des tranches et en les transformant en tuples
    # lorsque c'est ce qui est demand�
    return {
        e[0] : e[4:6] + [ tuple(e[1:4]), tuple(a[1:4]) ]
        for (e,a) in zip (extended, abbreviated)
        }
# @END@

class ExerciceMerge(Exercice):

    # on surcharge correction pour capturer les arguments
    def correction(self, student_merge, extended, abbreviated):
        self.datasets = [((extended, abbreviated), {})]
        return Exercice.correction(self, student_merge)

    # une fonction pour exposer le resultat attendu
    def resultat(self, extended, abbreviated):
        return self.solution(extended, abbreviated)

exo_merge = ExerciceMerge(merge, "inputs_gets_overridden")
    
