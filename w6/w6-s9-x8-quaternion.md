---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
notebookname: classe Quaternion
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

## exercice - niveau avancé

+++

Le [corps des quaternions](https://fr.wikipedia.org/wiki/Quaternion) est une extension non commutative du corps des complexes; la construction mathématique est totalement hors sujet pour nous, on va se contenter de ces quelques bribes :

* les quaternions peuvent être vus comme un espace vectoriel 
  sur $\mathbb{R}$, un peu comme les complexes mais de dimension 4
* un quaternion s'écrit donc $q = a + bi + cj + dk$  
  avec $(a, b, c, d) \in \mathbb{R}^4$  
  (les deux premiers éléments $1$ et $i$ de cette base canonique sont ceux des nombres complexes)
* les trois éléments $i, j, k$ sont tels que  
  $$i^2 = j^2 = k^2 = ijk = -1$$

+++

**attention** : l'addition est bien commutative,  
mais à nouveau **la multiplication n'est pas commutative**  
ainsi par exemple $ij = k$ mais $ji = -k$

les règles indiquées ci-dessus impliquent (on vous laisse vous en assurer) que la table de multiplication est la suivante

![](media/quaternion-table.png)

+++

On se propose ici d'écrire une classe pour représenter les quaternions.

**Notes importantes**

* il est malheureux que Python ait retenu la notation `j` pour représenter ce qu'on appelle $i$ dans le corps des complexes, surtout dans ce contexte des quaternions où il y a un autre nombre qui s'appelle justement $j$...

* le système de correction automatique a besoin également que votre classe définisse son comportement vis-à-vis de `repr()` ; regardez les exemples pour voir la représentation choisie, et inspirez-vous de la fonction `number_str` comme suit :

```{code-cell} ipython3
def number_str(x):
    """
    la fonction utilisée dans Quaternion.__repr__ 
    pour la mise en forme des nombres
    """
    if isinstance(x, int):
        return f"{x}"
    elif isinstance(x, float):
        return f"{x:.1f}"
```

```{code-cell} ipython3
from corrections.cls_quaternion import exo_quaternion
exo_quaternion.example()
```

*****

```{code-cell} ipython3
# votre code

class Quaternion:
    
    def __init__(self, a, b, c, d):
        ...        
```

```{code-cell} ipython3
# correction
exo_quaternion.correction(Quaternion)
```

*****

```{code-cell} ipython3
# peut-être utile pour debugger ?
I = Quaternion(0, 1, 0, 0)
J = Quaternion(0, 0, 1, 0)
K = Quaternion(0, 0, 0, 1)
```

```{code-cell} ipython3
I*J == K
```

```{code-cell} ipython3
J*K == I
```

```{code-cell} ipython3
K*I == J
```

```{code-cell} ipython3
I*I == J*J == K*K == -1
```

```{code-cell} ipython3
J*K == 1j
```

```{code-cell} ipython3
K*J == -1j
```
