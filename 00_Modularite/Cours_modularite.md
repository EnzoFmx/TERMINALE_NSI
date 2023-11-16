# Modularité

------

## **1. Introduction**

Lorsque l'on programme du code, il arrive souvent (quasi tout le temps) d'avoir des erreurs de code, des bugs. Ces freins à une bonne programmation sont normal. Mais il est possible d'éviter tout ces problèmes il faut prendre des bonnes habitudes de programmation.

Dans ce cours nous allons voir 3 critères importants pour gagner en visibilité.

## **2. Structurer son programme**

En informatique, les projets sont réalisés par plusieurs personnes et il n'est pas rare qu'un fichier soit édité par plusieurs développeurs.

C'est pourquoi, il est important lorsque l'on programme d'être clair et précis tant dans la structuration du programme que dans les explications (documentation).

Tout au long de l'année il va falloir être rigoureux sur la disposition du code :

Voici un exemple d'un fichier *python* (nous n'allons pas nous intéresser à son contenu mais à sa disposition) :

```python
## les importations
from math import *
import doctest

## mes variables
VALEUR = 25

## mes fonctions
def racine(val):
    """
    
    Renvoie la racine carré d'un nombre.

    :param val: (int) un entier
    :return: (float) la racine carré
    :CU: type(val) == int && val >= 0

    example:
    >>> racine(VALEUR)
    5.0
    """
    return sqrt(val)

## mon programme principal
print(racine(VALEUR))

if __name__=="__main__":
    doctest.testmod(verbose=True)
```

Chaque bloc est caractérisé par un titre mis en commentaire par *##*. Avec une nomenclature sous cette forme, on gagne en visibilité et nous permet de gagner du temps lors de la recherche d'un élément particulier.

## **3. Programmation modulaire**

Lorsque l'on programme sous python, nous éditons des fichiers sous un format *.py*. Chaque fichier python est appelé **module**.

Pour gagner en visibilité dans un programme, la nomenclature ne suffit pas à elle seule. Une autre manière de gagner du temps, c'est de faire des modules qui ont une tache spécifique.

Intéressons nous au programme vu précédemment :

```python
## les importations
from math import *
import doctest
```

Au début du programme, nous avons une partie *import* où l'on ajoute toute les lignes d'importations. Ces dernières permettent de dire à python que l'on ajoute a notre programme des élément du module **math** et du module **doctest**.

Chacun de ces modules à ses propres variables, fonctions et autres éléments. Le module *math* va permet de réaliser des opérations mathématiques comme la racine carré avec la fonction **sqrt** et le module *doctest* va s'occuper de réaliser des tests unitaire (que nous verrons un peu plus tard).

Dans un TP/Projet, il va être important de faire plusieurs modules, ceci aura plusieurs avantages :

- des fichiers assez court ;
- répartition du travail en groupe plus simple ;
- plus de visibilité lors d'une recherche d'un bug.

## **4. La documentation**

Un dernier point très important, c'est la documentation avec ses jeux de tests.

### **4. 1. Documentation simple**

Lorsque l'on utilise un module connu comme **math**, **random** ou encore **tkinter**, il est possible de trouver sa documentation en ligne afin de trouver les informations nous permettant de s'en servir correctement.

Il existe aussi une documentation que l'on peut récupérer via les modules grace à la fonction *help* :

```python
import random

help(random)
```

La documentation dans le module ne sert pas de décoration mais permet à celui ou celle ou bien à vous même lorsque vous reprenez le programme un temps plus tard de comprendre ses spécifications.

Voyons un exemple d'une **documentation** d'une fonction :

```python
def somme(n):
    """
    Renvoie la somme des nombres entre 0 à n

    :param n: (int) un nombre entier positif
    :return: (int) la somme de 0 à n
    :CU:
        type(n) == int
        n >= 0
    """
    return sum([i for i in range(n+1)])
```

La documentation se trouve toujours au début de la fonction, avant la première ligne de son bloc d'instructions et on y retrouve plusieurs informations :

- Une phrase qui explique son comportement
- Explication des paramètres et leur type
- Explication de la valeur de retour et son type
- Les contraintes d'utilisation

### **4. 2. Le module Doctest**

Le module doctest permet à python de réaliser des tests de façon à ce que le programme voit seul s'il y a un problème.

Pour réaliser ces tests unitaires, nous allons avoir besoin du module **doctest**.

Reprenons notre exemple et ajoutons y notre test :

```python
import doctest

def somme(n):
    """
    Renvoie la somme des nombres entre 0 à n

    :param n: (int) un nombre entier positif
    :return: (int) la somme de 0 à n
    :CU:
        type(n) == int
        n >= 0

    Exemple:
    >>> somme(5)
    15
    >>> somme(-1)
    AssertionError: erreur
    """
    assert type(n)==int, "erreur"
    assert n >= 0, "erreur"
    return sum([i for i in range(n+1)])

    if __name__=="__main__":
    doctest.testmod(verbose=True)
```

Lors de l'exécution du programme principal, la fonction *testmod* du module **doctest** va parcourir toute les documentations à la recherche de ligne commençant par ```>>>```.

Une fois les lignes trouvées, testmod va exécuter la ligne en question puis va comparer son résultat avec ce qui a été mis en dessous.

L'attribut *verbose* de la fonction testmod nous permet de dire à ce dernier de nous parler et de donner le détail des test, par défaut l'attribut est mis à False.