# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

# @BEG@ 3 2 merge
def merge (extended, abbreviated):
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
        id, latitude, longitude, timestamp, name, country = ship [:6]
        # on cr�e une entr�e dans le r�sultat, 
        # avec la mesure correspondant aux donn�es �tendues
        result[id] = [ name, country, (latitude, longitude, timestamp) ]
    # maintenant on peut compl�ter le r�sultat avec les donn�es abr�g�es
    for id, latitude, longitude, timestamp in abbreviated:
        # et avec les hypoth�ses on sait que le bateau a d�j� �t� 
        # inscrit dans le r�sultat, donc on peut se contenter d'ajouter 
        # la mesure abr�g�e correspondant au bateau
        result [id] . append ( (latitude, longitude, timestamp) )
    # et retourner le r�sultat
    return result
# @END@

def merge2 (extended_data, abbreviated_data):
    result = {}
    for ship in extended_data:
        result [ship[0]] = ship[4:6]
        result [ship[0]] .append ( tuple (ship[1:4]))
    for ship in abbreviated_data:
        result [ship[0]] .append( tuple (ship[1:4]))
    return result

class ExerciceMerge (Exercice):

    # on surcharge correction pour capturer les arguments
    def correction (self, student_merge, extended, abbreviated):
        self.datasets = [ ((extended, abbreviated), {}) ]
        return Exercice.correction (self, student_merge)

    # une fonction pour exposer le resultat attendu
    def resultat (self, extended, abbreviated):
        return self.solution (extended, abbreviated)

exo_merge = ExerciceMerge (merge, "inputs_gets_overridden")
    
