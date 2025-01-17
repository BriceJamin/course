---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  encoding: '# -*- coding: utf-8 -*-'
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
notebookname: Organiser les sources
version: '3.0'
---

# Comment organiser les sources de votre projet Python

+++

Où on va voir que :
* c'est bien de grouper son code dans un package
* mais à première vue ça casse tout, cependant pas de panique !
* il ne **FAUT PAS** tripoter la variable **`PYTHONPATH`**
* il faut au contraire créer un `setup.py`, et ensuite lancer une fois
  `pip install -e .`
  pour pouvoir utiliser le code en mode développeur

+++

## Complément - niveau intermédiaire

+++

Vous venez d'écrire un super algorithme qui simule le climat de l'an 2100, et vous voulez le publier ? Nous allons voir ici comment organiser les sources de votre projet, pour que ce soit à la fois

* pratique pour vous de tester votre travail pendant le développement
* facile de publier le code pour que d'autres puissent l'installer et l'utiliser
* et éventuellement facile pour d'autres de contribuer à votre projet.

+++

## Les infrastructures

+++

En 2020 on ne travaille plus tout seul dans son coin ; il est à la portée de tous d'utiliser et de tirer profit d'infrastructures, ouvertes et gratuites (pour les usages de base au moins) :

Pour ce qui nous concerne ici, voici celles qui vont nous être utiles :

* [PyPI](https://pypi.org) - (prononcer "paille - pis - ail") pour **Py**thon **P**ackage **I**ndex, est l'endroit où chacun peut publier ses librairies
* [github](https://github.com) - ainsi que ses concurrents [gitlab](https://gitlab.com) et [bitbucket](https://bitbucket.org) - sont bien sûr des endroits où l'on peut déposer ses sources pour partage, sous la forme de  dépôt `git`

Optionnellement, sachez qu'il existe également des infrastructures pour les deux grandes tâches que sont la documentation et le test, souvent considérées - à tort - comme annexes :

* [readthedocs](https://readthedocs.io) est une infra qui permet d'exposer la documentation
* [travis](https://travis-ci.com) est - parmi plein d'autres - une infrastructure permettant d'exécuter une suite de tests

S'agissant de ces deux derniers points : souvent on s'arrange pour que tout soit **automatique** ; quand tout est en place, il **suffit de pousser un nouveau commit** auprès de github (par exemple) pour que

* tous les **tests** soient **repassés** (d'où le terme de **CI** = *Continuous Integration*) ; du coup on sait en permanence si tel ou tel commit a cassé ou non l'intégrité du code ;
* la **documentation** soit **mise à jour**, exposée à tout le monde, et navigable par numéro de version.

+++

Alors bon bien sûr ça c'est le monde idéal ; on ne passe pas d'un seul coup, d'un bout de code qui tient dans un seul module `bidule.py`, à un projet qui utilise tout ceci ; on n'a **pas forcément besoin** non plus d'utiliser **toutes** ces ressources (et bien entendu, aucun de ces trucs n'est obligatoire).

Aussi nous allons commencer par le commencement.

+++

## Le commencement : créer un package

+++

Le commencement, ça consiste à se **préparer à coexister** avec d'autres librairies.

Si votre code expose disons une classe `Machine` dans le fichier/module `machine.py`, la première chose consiste à  trouver un nom unique ; rien ne vous permet de penser qu'il n'y a pas une autre bibliothèque qui expose un module qui s'appelle aussi `machine` (il y a même fort à parier qu'il y en a plein !).
Aussi ce qu'on va commencer par faire c'est d'installer tout notre code **dans un package**.

Concrètement ça va signifier se mettre dans un sous-dossier, mais surtout d'un point de vue des utilisateurs potentiels de la classe, ça veut dire qu'au lieu de faire juste :

```python
from machine import Machine
```

on va décider qu'à partir de maintenant il faut toujours faire

```python
from bidule.machine import Machine
```

et de cette façon tous les noms qui sont propres à notre code ne sont accessibles que via l'espace de noms `bidule`, et on évite les conflits avec d'autres bibliothèques.

+++

### Choisir le nom du package

+++

Bien sûr ceci ne fonctionne que si je peux **être sûr que `bidule` est à moi**, de sorte que **personne** demain ne publie une librairie qui utilise **le même nom**.

C'est pourquoi je **recommande**, à ce stade, de s'assurer de prendre un nom qui n'est **pas déjà pris** ; en toute rigueur c'est optionnel, tant que vous ne prévoyez pas de publier votre appli sur pypi (car bien sûr c'est optionnel de publier sur pypi), mais ça coûte moins cher de le faire très tôt, ça évite des renommages fastidieux plus tard.

+++

Donc pour s'assurer de cela, on va tout simplement demander à `pypi`, qui va jouer le rôle de *registrar*, et nous garantir l'exclusivité de ce nom. Je vous invite à chercher votre nom [directement dans le site pypi](https://pypi.org/search/?q=bidule) pour vous en assurer (à noter que `pip search bidule` n'est plus disponible depuis la ligne de commande)

+++

Le nom est libre, pour toute la suite **je choisis `bidule` comme mon nom de package**.
Vous trouverez dans ce dépôt git <https://github.com/flotpython/bidule> un microscopique petit projet qui illustre notre propos.

+++

### Adapter son code

+++

Une fois que j'ai choisi mon nom de package, donc ici `bidule`, je dois :

1. mettre tout mon code dans un répertoire qui s'appelle `bidule`,
1. et modifier mes importations ; maintenant j'importe tout au travers du seul package `bidule`.

+++

Donc je remplace les importations partout ; ce qui avant aurait été simplement

```python
from machine import Machine
```

devient

```python
from bidule.machine import Machine
```

+++

#### Remarque : imports relatifs

Lorsqu'un fichier a besoin d'en importer **dans le même package**, on a le choix ; par exemple ici, `machine.py` a besoin d'importer la fonction `helper` du fichier `helpers.py`, il peut faire

```python
from bidule.helpers import helper
```

mais aussi plus simplement avec un **import relatif** :

```python
from .helpers import helper
```

remarquez le `.` dans `.helpers`, qui signifie *dans le même package que moi*.

+++

Je recommande toutefois de ne pas se précipiter avec ces imports relatifs, et notamment de **ne pas les utiliser dans un point d'entrée** (le fichier qu'on passe à l'interpréteur Python) car ça ne fonctionne pas dans ce cas.

+++

### C'est tout cassé

+++

À ce stade précisément, vous constatez... que **plus rien ne marche** !

En effet, comme on l'a vu dans le complément sur le chargement des modules, Python recherche vos modules dans l'ordre

* le dossier du point d'entrée
* la variable d'environnement `PYTHONPATH`
* les dossiers système

Et donc si vous m'avez suivi, vous devez avoir quelque chose comme

```
mon-depot-git/
             bidule/
                    main.py
                    machine.py
                    helpers.py
```

mais alors quand vous faites 

```
$ python bidule/main.py
Traceback (most recent call last):
  File "bidule/main.py", line 1, in <module>
    from bidule.machine import Machine
ModuleNotFoundError: No module named 'bidule'
```

on va chercher du coup un module `bidule` à partir du répertoire du point d'entrée qui est le dossier `bidule/`, donc on ne trouve pas.

+++

### Le mauvais réflexe

Du coup naturellement, on se dit, ça n'est pas grave, je vais tirer profit de la variable `PYTHONPATH`.
Alors disons-le tout net : **Ce n'est pas une bonne idée**, ce n'est pas du tout pour ce genre de cas qu'elle a été prévue.

Le fait de modifier une variable d'environnement est un processus tarabiscoté, même sans parler de Windows, et cette approche est une bonne façon de se tirer une balle dans le pied ; un jour ou l'autre la variable ne sera pas positionnée comme il faut, c'est sûr.

Bref, il ne **faut pas faire comme ça !!**

+++

## Le bon réflexe : `setup.py`

Non, le bon reflexe ici c'est d'écrire un fichier `setup.py`, et de l'utiliser pour faire ce qu'on pourrait appeler une *installation en mode développeur*. Voyons cela :

Je commence donc par créer un fichier `setup.py` à la racine de mon dépôt git, dans lequel je mets, pour commencer, le minimum :

```python
# minimal setup.py to install in develop mode

from setuptools import setup, find_packages

setup(
    name="bidule",
    packages=find_packages(),
)
```

+++

**Attention** : nous sommes en 2020 et il faut utiliser le package `setuptools`, qui ne fait pas partie de la librairie standard (**et non pas** le module `distutils` qui, lui, en fait pourtant partie) ; donc comme d'habitude si c'est nécessaire, faites dans le terminal :

    pip install setuptools

+++

### Installation en mode developpeur : `pip install -e .`

Avec ce fichier en place, et toujours à la racine de mon dépôt, je peux maintenant faire la formule magique (toujours dans le terminal)

```
$ pip install -e .
Obtaining file:///Users/tparment/git/flotpython-course/w6/mon-depot-git
Installing collected packages: bidule
  Attempting uninstall: bidule
    Found existing installation: bidule 0.0.0
    Uninstalling bidule-0.0.0:
      Successfully uninstalled bidule-0.0.0
  Running setup.py develop for bidule
Successfully installed bidule
```

L'effet de cette commande est de modifier mon environnement pour que le répertoire courant (le `.` dans `pip install -e .`) soit utilisé pour la recherche des modules.
Ça signifie que je peux maintenant lancer mon programme sans souci :

  ```
  $ python bidule/main.py
  ... déroulement normal
  ```

Et je peux modifier mon code dans le répertoire courant, ce sera bien ce code-là qui sera utilisé ; cette précision pour ceux qui penseraient que, comme on fait une installation, cela pourrait être fait par copie, mais ce n'est pas le cas, donc sauf gros changement dans le contenu, on n'a **plus besoin de refaire** le `pip install -e .`

+++

### Un `setup.py` plus raisonnable

+++

Au delà de cette première utilité, `setup.py` sert à configurer plein d'aspects de votre application ; lorsque votre projet va gagner en maturité, il sera exécuté lorsque vous préparez le packaging, lorsque vous uploadez le package, et au moment d'installer (comme on vient de le voir).

+++

Du coup en pratique, les besoins s'accumulent au fur et à mesure de l'avancement du projet, et on met de plus en plus d'informations dans le `setup.py`; voici quelques ajouts très fréquents que j'essaie de mettre dans l'ordre chronologique [reportez-vous à la doc pour une liste complète](https://setuptools.readthedocs.io/en/latest/setuptools.html#developer-s-guide) :

* `name` est le nom sous lequel votre projet sera rangé dans PyPI

* `packages` est une liste de noms de packages ; tel qu'on l'a écrit, cela sera calculé à partir du contenu de votre dépôt ; dans notre cas on aurait pu aussi bien écrire en dur `['bidule']`;
  dans les cas les plus simples on a `packages == [ name ]`


* `version` est bien entendu important dès que vous commencez à publier sur PyPI (et même avant) pour que PyPI puisse servir la version la plus récente, et/ou satisfaire des exigences précises (les applis qui vous utilisent peuvent par exemple préciser une version minimale, etc...)
  Cette chaine devrait être [compatible avec semver (semantic versioning)](https://semver.org/)
  i.e. qu'un numéro de version usuel contient 3 parties (major, minor, patch), comme par ex. "2.1.3"
  le terme `semantic` signifie ici que **toute rupture de compatibilité** doit se traduire par une incrémentation du numéro majeur (sauf s'il vaut `0`, on a le droit de tâtonner avec une 0.x; d'où l'importance de la version 1.0)

* `install_requires` : si votre package a besoin d'une librairie non-standard, disons par exemple `numpy`, il est **très utile** de le préciser ici ; de cette façon, lorsqu'un de vos utilisateurs installera votre appli avec `pip install bidule`, `pip` pourra **gérer les dépendances** et s'assurer que `numpy` est installé également ;
  bien sûr on n'en est pas là, mais je vous recommande de maintenir **dès le début** la liste de vos dépendances ici



* informatifs : `author`, `author_email`, `description`, `keywords`, `url`, `license`,  pour affichage sur PyPI ;
  une mention spéciale à propos de `description_long`, qu'en général on veut afficher à partir de `README.md`, d'où l'idiome fréquent :

  ```python
  setup(
     ...
     long_description=open('README.md').read(),
     long_description_content_type = "text/markdown",
     ...
  )
  ```

* etc… beaucoup d'autres réglages et subtilités autour de `setup.py` ; je conseille de prendre les choses comme elles viennent : commencez avec la liste qui est ici, et n'ajoutez d'autres trucs que lorsque ça correspond à un besoin pour vous !

+++

### Packager un point d'entrée

+++

Assez fréquemment on package des **librairies** ; dans ce cas on se soucie d'installer uniquement des modules Python.


Mais imaginez maintenant que votre package contient aussi un **point d'entrée** - c'est-à-dire en fin de compte une **commande** que vos utilisateurs vont vouloir lancer **depuis le terminal**. Ce cas de figure change un peu la donne; il faut maintenant installer des choses à d'autres endroits du système (pensez par exemple, sur linux/macos, à quelque chose comme `/usr/bin`).

Dans ce cas **surtout n'essayez pas de le faire vous-même**, c'est beaucoup trop compliqué à faire correctement !

Pour illustrer la bonne façon de faire dans ce cas, je vous renvoie pour les détails à un exemple réel, mais pour l'essentiel :

* je vous conseille d'écrire tout le code en question dans une classe habituelle, que vous rangez normalement avec les autres ;
* cette classe expose typiquement une méthode `main()`, qui retourne, pour suivre les conventions usuelles :
  * `0` si tout s'est bien passé
  * `1` sinon
* vous créez un module `__main__.py` qui se contente de créer une instance et de lui envoyer la méthode `main` - voir l'exemple
* vous déclarez cela dans `setup.py` qui se chargera de tout :-)

Voici tout ceci illustré sur un exemple réel.
Dans  cet exemple, le package (PyPI) s'appelle `apssh`, la commande qu'on veut exposer s'appelle `apssh`, du coup on a
 * un dossier `apssh` pour matérialiser le package
 * un module `apssh/apssh.py`, qui définit
 * une classe `Apssh`, qui expose une méthode `main()`

Voici les différents codes; le détail de la classe elle-même n'est pas pertinent (c'est très long), c'est pour vous montrer un système de nommage, disons habituel :

* [la définition de `entry_points` dans `setup.py`](https://github.com/parmentelat/apssh/blob/a97cccd8eb6286a81c68b3c6953fce8a643fe8e9/setup.py#L52-L55)
  ici après installation avec `pip`, nos utilisateurs pourront utiliser la commande `apssh`,
  qui est de cette façon associée au module `__main__.py`
  (les termes `entry_points` et `console_scripts` ne doivent pas être modifiés);

* [ le module `__main__.py`](https://github.com/parmentelat/apssh/blob/a97cccd8eb6286a81c68b3c6953fce8a643fe8e9/apssh/__main__.py);

* la classe `Apssh` qui fait le travail se trouve [ dans un module usuel, ici `apssh.py`](https://github.com/parmentelat/apssh/blob/a97cccd8eb6286a81c68b3c6953fce8a643fe8e9/apssh/apssh.py).

+++

## Publier sur PyPI

+++

Pour publier votre application sur PyPI, rien de plus simple :

* il faut naturellement obtenir un login/password
* avant de pouvoir utiliser le nom `bidule`, il faut l'enregistrer :
  `python setup.py register`
* aussi il vous faudra installer `twine`
  `pip install twine`

Ensuite à chaque version, une fois que les tests sont passés et tout :

* préparer le packaging
  `python setup.py sdist bdist_wheel`
* pousser sur PyPI
  `twine upload dist/*`

Signalons enfin qu'il existe une infra PyPI "de test" sur `https://test.pypi.org` utile quand on ne veut pas polluer l'index officiel.

+++

## Utiliser `pip` pour installer

+++

Ensuite une fois que c'est fait, le monde entier peut profiter de votre magnifique contribution en faisant bien sûr
`pip install bidule`

Remarquez que l'on conseille parfois, pour éviter d'éventuels soucis de divergence entre les commandes `python`/`python3` et `pip`/`pip3`,
* de remplacer tous les appels à `pip`
* par plutôt `python -m pip`, qui permet d'être sûr qu'on installe dans le bon environnement.

D'autres formes utiles de `pip` :

* `pip show bidule` : pour avoir des détails sur un module précis
* `pip freeze` : pour une liste complète des modules installés dans l'environnement, avec leur numéro de version
* `pip list` : sans grand intérêt, si ce n'est dans sa forme
  `pip list -o` qui permet de lister les modules qui pourraient être mis à jour
* `pip install -r requirements.txt` : pour installer les modules dont la liste est dans le fichier `requirements.txt`

+++

## Packages et `__init__.py`

+++

Historiquement avant la version 3.3 pour qu'un dossier se comporte comme un package il était **obligatoire** d'y créer un fichier de nom `__init__.py` - même vide au besoin.

Ce n'est plus le cas depuis cette version. Toutefois, il peut s'avérer utile de créer ce fichier, et si vous lisez du code vous le trouverez très fréquemment.

L'intérêt de ce fichier est de pouvoir agir sur :
* le contenu du package lui-même, c'est-à-dire les attributs attachés à l'objet module associé à ce dossier,
* et accessoirement d'exécuter du code supplémentaire.

Un usage particulièrement fréquent consiste à "remonter" au niveau du package les symboles définis dans les sous-modules. Voyons ça sur un exemple.

+++

Dans notre dépôt de démonstration, nous avons une classe `Machine` définie dans le module `bidule.machine`. Donc de l'extérieur pour me servir de cette classe je dois faire

```python
from bidule.machine import Machine
```

C'est très bien, mais dès que le contenu va grossir, je vais couper mon code en de plus en plus de modules. Ce n'est pas tellement aux utilisateur de devoir suivre ce genre de détails. Donc si je veux pouvoir changer mon découpage interne sans impacter les utilisateurs, je vais vouloir qu'on puisse faire plutôt, simplement

```python
from bidule import Machine
```

pour y arriver il me suffit d'ajouter cette ligne dans le `__init__.py` du package `bidule` :

```python
import Machine from .machine
```

qui du coup va définir le symbole `Machine` directement dans l'objet package.

+++

## Environnements virtuels

+++

Terminons ce tour d'horizon pour dire un mot des environnements virtuels.

Par le passé, on installait python une seule fois dans le système ; en 2020, c'est une approche qui n'a que des inconvénients :

* quand on travaille sur plusieurs projets, on peut avoir besoin de Python-3.6 sur l'un et Python-3.8 sur un autre ;
* ou alors on peut avoir un projet qui a besoin de `Django==2.2` et un autre qui ne marche qu'avec `Django>=3.0` ;
* en plus par-dessus le marché, dans certains cas il faut être super utilisateur pour modifier l'installation ; typiquement on passe son temps à faire `sudo pip` au lieu de `pip`…

et le seul avantage, c'est que tous les utilisateurs de l'ordi peuvent partager l'installation ; sauf que, plus de 99 fois sur 100, il n'y a qu'un utilisateur pour un ordi ! Bref, c'est une pratique totalement dépassée.

+++

La création et la gestion d'environnements virtuels sont **très faciles** aujourd'hui. Aussi c'est une **pratique recommandée** de se créer **un virtualenv par projet**. C'est tellement pratique qu'on n'hésite pas une seconde à repartir d'un environnement vide à la moindre occasion, par exemple lorsqu'on a un doute sur les dépendances.

Le seul point sur lequel il faut être attentif, c'est de trouver un moyen de **savoir en permanence** dans quel environnement on se trouve. Notamment :

* une pratique très répandue consiste à s'arranger pour que **le prompt dans le terminal** indique cela,
* dans vs-code, dans la bannière inférieure, on nous montre toujours l'environnement courant.

+++ {"cell_style": "center"}

![](media/venv-terminal.png)

**figure :** le prompt dans le terminal nous montre le venv courant

+++ {"cell_style": "center"}

![](media/venv-vscode.png)

**figure :** vs-code nous montre le venv courant et nous permet de le changer

+++

### Les outils

+++

Par contre il reste le choix entre plusieurs outils, que j'essaie de lister ici :

* [`venv`](https://docs.python.org/3/library/venv.html) un module de la librairie standard

* [`virtualenv`](https://virtualenv.pypa.io/en/latest/) un module externe, qui préexistait à `venv` et qui a fourni la base des fonctionnalités de `venv`

* [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) un sous-produit de anaconda

+++

Actuellement j'utilise quant à moi `miniconda`.
Voici à titre indicatif une session sous MacOS en guise de rapide introduction.
Vous remarquerez comme le *prompt* reflète **l'environnement dans lequel on se trouve**, ça semble relativement impératif si on ne veut pas s'emmêler les pinceaux.

+++

##### La liste de mes environnements
```
[base] ~ $ conda env list
# conda environments:
#
base                  *  /Users/tparment/miniconda3
<snip ...>
```

+++

##### j'en crée un nouveau avec Python-3.8

```
[base] ~ $ conda create -n demo-py38 python=3.8
Collecting package metadata (current_repodata.json): done
Solving environment: done
<snip ...>
```

+++

##### on le voit
```
[base] ~ $ conda env list
# conda environments:
#
base                  *  /Users/tparment/miniconda3
demo-py38                /Users/tparment/miniconda3/envs/demo-py38
<snip...>
```

+++

##### pour entrer dans le nouvel environnement

```
[base] ~ $ conda activate demo-py38
[demo-py38] ~ $
```

+++

##### les packages installés

très peu de choses

```
[demo-py38] ~ $ pip list
Package    Version
---------- -------------------
certifi    2020.4.5.1
pip        20.0.2
setuptools 46.2.0.post20200511
wheel      0.34.2
```

+++

##### on y installe ce qu'on veut
```
[demo-py38] ~ $ pip install numpy==1.15.3
```

+++

##### la version de python
```
[demo-py38] ~ $ python --version
Python 3.8.2
```

+++

##### sortir
```
[demo-py38] ~ $ conda deactivate
[base] ~ $
```

+++

##### la version de python
```
[base] ~ $ python --version
Python 3.7.6
```

+++

##### on n'a pas perturbé l'environnement de départ
```
[base] ~ $ pip show numpy
Name: numpy
Version: 1.18.1
```

+++

##### pour détruire l'environnement en question
```
[base] ~ $ conda env remove -n demo-py38

Remove all packages in environment /Users/tparment/miniconda3/envs/demo-py38:
```
