# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

# @BEG@ 3 5 decode_zen
# le module this est impl�ment� comme une petite �nigme 
# comme le laissent entrevoir les indices, on y trouve
# (*) dans l'attribut 's' une version encod�e du manifeste
# (*) dans l'attribut 'd' le code � utiliser pour d�coder
# 
# ce qui veut dire qu'en premi�re approximation on pourrait 
# obtenir une liste des caract�res du manifeste en faisant
# 
# [ this.d [c] for c in this.s ]
# 
# mais ce serait le cas seulement si le code agissait sur 
# tous les caract�res

def decode_zen(this_module):
    # la version encod�e du manifeste
    encoded = this_module.s
    # le 'code' 
    code = this_module.d
    # si un caract�re est dans le code, on applique le code
    # sinon on garde le caract�re tel quel
    # aussi, on appelle 'join' pour refaire une cha�ne � partir
    # de la liste des caract�res d�cod�s
    return ''.join([code[c] if c in code else c for c in encoded])

# une autre version qui marche aussi, en utilisant 
# dict.get(key, default)
def decode_zen_bis(this_module):
    return "".join([this_module.d.get(c, c) for c in this_module.s])
# @END@

class ExerciceDecodeZen(Exercice):
    # on surcharge correction pour capturer les arguments
    def correction(self, student_decode_zen, this):
        self.datasets = [((this,), {})]
        return Exercice.correction(self, student_decode_zen)
    
    def resultat(self, this):
        return self.solution(this)

# cannot copy not deepcopy a module
exo_decode_zen = ExerciceDecodeZen(decode_zen, "inputs_gets_overridden", copy_mode='none')
