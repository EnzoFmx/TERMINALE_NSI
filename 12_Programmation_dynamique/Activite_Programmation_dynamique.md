# Activité programmation dynamique :

------

## 1. Objectif :

Réaliser l'un des deux cas décrit ci dessous.

Pour chacun des cas :

1. Comprendre le problème décris, et trouver une solution pour le résoudre de manière naïve (ou gloutonne).
2. Ecrire l'algorithme en version naïve (Sans utiliser la programmation dynamique)
3. Réfléchir aux sous problèmes possibles. Et à l'implémentation possible de l'algorithme en programmation dynamique. (Ascendante, descendante)
4. Ecrire cet algorithme.

## 2. Cas d'applications :

### 2. 1. Pyramide de nombres :

<u>Pyramide de nombres :</u> Retrouver la somme maximale en parcourant les nombres de la pyramide.

![image-20240404005435648](./Images/pyramide.png)

Ici les nombres peuvent être représentés sous forme de tableau : 

```python
pyramide = [[3], [7,4], [2,4,6], [8,5,9,3]]
```

### 2. 2. Rendue de monnaie :

<u>Problème du rendu de monnaie :</u> Comment à partir d'une somme et d'un ensemble de pièces/billets rendre le moins de pièces possibles. Les systèmes monétaires possibles peuvent être l'euro [50, 20, 10, 5, 2, 1] ou l'ancien système impérial britannique [30, 24, 12, 6, 3, 1]
