# **Les listes chainées**

------

Le but de ce TP est de pouvoir définir la classe liste afin de définir la classe des listes chainées qui seront non cyclique et simplement chainée.

## 1. La classe Liste

Pour rappel, une liste est constitué de 2 attributs :

- Le contenu
- Le suivant

S'ajoute à cela la méthode permettant d'ajouter une autre liste.

Si il n'y a pas de suivant alors la classe pointera vers un objet ```None```

Exemple d'utilisation de la classe Liste pour faire une liste ```[1, 2, 3]```

```python
>>> m3 = Liste(3)
>>> m2 = Liste(2, m3)
>>> m1 = Liste(1, m2)
```

## 2. Première approche

0. Créer un module ```Liste.py```.

1. Définir la classe Liste avec sa documentation.

2. Utiliser la classe Liste pour créer une liste chainée de tous les nombres pair compris entre 0 et 6 inclus.

3. Quels sont les inconvénients de cette méthode pour un utilisateur lambda ?

4. Que faudrait-il faire pour faciliter l’utilisation des listes chaînées pour l’utilisateur. Dans ce cas que devra uniquement connaître l’utilisateur ?

## 3. Méthodes associées

5. Construire une méthode **est_vide(self)** qui retourne True si la liste est vide, False sinon.

```python
def est_vide(self):
    """
    Renvoie Vrai si la liste est vide.

    :return: (bool) Vrai si la liste est vide, Faux sinon.
    :CU: aucune

    Exemple:
    >>> l1 = Liste()
    >>> l1.est_vide()
    True
    >>> l2 = Liste([1,2,3])
    >>> l2.est_vide()
    False
    """
```

7. Construire une méthode **ajouter_element_queue(self,element)** qui ajoute une liste à la liste chaînée. Son paramètre valeur contiendra la valeur de la liste à ajouter. On distinguera les cas où la liste est vide ou non.

```python
>>> l = Liste()
>>> l.ajoute_element_queue(1)
```

8. Créer une méthode **\_\_len\_\_(self)** qui permet de calculer la taille de la liste avec l'utilisation de la fonction *len* de python. (De manière récursive)

9. Construire la méthode **extrait_element(self)** qui retourne le maillon de position d’indice *i* spécifié par l’utilisateur. Le programme doit s’arrêter en fournissant un message à l’utilisateur s’il spécifie un indice non valable (préconditions, mot clé *assert* en Python).

10. Ecrire la méthode **\_\_repr\_\_ (self)** permettant d'avoir un affichage de la Liste

    ```python
    >>> m3 = Liste(3)
    >>> m2 = Liste(2, m3)
    >>> m1 = Liste(1, m2)
    >>> m1
    [1,2,3]
    ```

11. Ecrire une méthode **\_\_add\_\_(self, other)** : retourne une nouvelle liste, concaténation de la liste avec la **liste** *other*.

Bonus. Construire les méthodes usuelles sur les listes chaînées suivantes : 

- ```ajouter_element_tete(self, val)``` : ajoute un maillon de valeur *val* à la tête de la liste ;
- ```supprimer_element_queue(self)``` : supprime le dernier maillon ;
- ```supprimer_element_tete(self)``` : supprime le premier maillon ;
- ```inserer_element(self, val, i)``` : insère un maillon de valeur *val* à la position d’indice *i* ;
- ```supprimer_element(self, i)``` : supprime le maillon de position d’indice *i* ;
- ```chercher_element(self, val)``` : retourne l’indice *i* du maillon recherché de valeur *val* ;
- ```renverser(self)``` : renverse la liste ;
- ```permuter_elements(self, i, j)``` : permute deux maillons de la liste d’indices *i* et *j* ;

