# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

# @BEG@ 3 3 diff
def diff (extended, abbreviated):
    """Calcule comme demand� dans l'exercice, et sous formes d'ensembles
(*) les noms des bateaux seulement dans extended
(*) les noms des bateaux pr�sents dans les deux listes
(*) les ids des bateaux seulement dans abbreviated
    """
    # on n'utilise que des ensembles dans tous l'exercice
    # les ids de tous les bateaux dans extended
    # en utilisant une compr�hension d'ensemble
    extended_ids =         { ship[0] for ship in extended }
    # les ids de tous les bateaux dans abbreviated
    # en utilisant une compr�hension d'ensemble
    abbreviated_ids =      { ship[0] for ship in abbreviated }
    # les ids des bateaux seulement dans abbreviated
    # en utilisant la difference des ensembles
    abbreviated_only_ids = abbreviated_ids - extended_ids
    # les ids des bateaux dans les deux listes
    # en utilisant l'intersection des ensembles
    both_ids =             abbreviated_ids & extended_ids
    # les ids des bateaux seulement dans extended
    # en utilisant la difference des ensembles
    extended_only_ids =    extended_ids - abbreviated_ids
    # on recalcule les noms pour les deux cat�gories o� c'est possible
    # par une compr�hension d'ensemble
    both_names = \
          { ship[4] for ship in extended if ship[0] in both_ids }
    extended_only_names = \
          { ship[4] for ship in extended if ship[0] in extended_only_ids }
    # enfin on retourne les 3 ensembles sous forme d'un tuple
    return extended_only_names, both_names, abbreviated_only_ids
# @END@

# xxx celui-ci serait + �l�gant mais ne marche pas et je ne comprends pas pourquoi...
def diff2 (extended, abbreviated):
    extended_ids =     { ship[0] for ship in extended }
    abbreviated_only = { ship[0] for ship in abbreviated if ship[0] not in extended_ids }
    extended_only =    { ship[4] for ship in extended    if ship[0] not in abbreviated_only }
    both =             { ship[4] for ship in extended    if ship[0] in abbreviated_only }
    return extended_only, both, abbreviated_only

import copy

class ExerciceDiff (Exercice):
    def correction (self, student_diff, extended, abbreviated):
        # start with the full dataset
        self.datasets = [ ((extended, abbreviated), {}) ]
        # make up a samples by taking only <sample> entries in each
        for sample in [ 10, 20, 40]:
            extended_sample = copy.deepcopy (extended[:sample])
            abbreviated_sample = copy.deepcopy (abbreviated[:sample])
            self.datasets.append ( ((extended_sample, abbreviated_sample), {}) )
        return Exercice.correction (self,student_diff)

    def resultat (self, extended, abbreviated):
        return self.solution (extended, abbreviated)

exo_diff = ExerciceDiff (diff, "inputs_gets_overridden")
    
