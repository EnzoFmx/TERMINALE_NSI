# Diviser pour régner

------

Parfois la résolution d'un problème peut être très longue et répétitive. Il s'agit d'appliquer une méthode encore et encore jusqu'à obtenir une solution.
Par exemple lorsque l'on recherche un élément dans un tableau, on regarde le premier élément, puis le second ainsi de suite. Lors d'un tri selection, on cherche un minimum dans un tableau puis on le place dans la partie triée, ainsi de suite. 
La complexité de ces algorithmes peuvent être très élevée. 

Il existe bien évidemment des méthodes pour réduire cette complexité, afin d'avoir des algorithmes plus performants.

La méthode **diviser pour régner** permet de **décomposer** un problème en sous-problèmes. Une fois les sous-problèmes crées on les **résout** puis on **combine** les résultats de ces sous problème pour trouver le résultat final.

Le tout se fait de manière récursive. 

Récapitulons :

- **Décomposition** du problème en sous problèmes
- **Résolution** des sous problèmes
- **Combinaison** des résultats

Nous allons ici parler de la recherche dichotomique afin d'illustrer notre propos. Ce n'est pas le meilleur exemple, mais c'est le plus trivial. Nous profiterons de la partie TP pour voir d'autres applications de cette méthode.

## 1. Recherche dichotomique

### 1. 1. Principe 

La recherche dichotomique est une recherche d'un élément dans un tableau trié. Il s'agit de la recherche optimale pour ce type de situation.

<u>Recherche dans un tableau :</u>

Tant que l'indice de début est inférieur à l'indice de fin :

- Sélectionner la valeur au milieu du tableau

  - Si la valeur du milieu est supérieur à la valeur recherchée
    - Rechercher dans la partie gauche du tableau

  - Si la valeur du milieu est inférieur à la valeur recherchée
    - Rechercher dans la partie droite du tableau
  - Sinon
    - Renvoyer la valeur recherchée

### 1. 2. Diviser pour régner sur la recherche dichotomique

<u>**Décomposition du problème en sous problèmes :**</u>

Afin d'appliquer la méthode, il faut dans un premier temps diviser le problème en sous problèmes. 

C'est pourquoi l'exemple de la recherche dichotomique n'est pas le meilleur, car il décompose le problème en 1 seul sous problème et pas en plusieurs.

Mais peut importe, la décomposition à lieu lorsqu'on recherche soit dans la partie de droite ou de gauche.

<u>**Résolution des sous problèmes :**</u>

La résolution du sous problèmes ici se fait lorsque l'on à 1 seul élément, soit il s'agit de l'élément recherché, soit ça ne l'est pas. 

**<u>Combinaison des résultats :</u>**

Une fois le résultat trouvé de ce sous problème, il est renvoyé (ici pas de combinaison, il n'y a qu'un sous problème)

### 1. 3. Code de la fonction 

```python
def recherche(t,v,d,f):
	"""Fonction récursive de recherche
	param t (tableau) : tableau dans lequel on recherche l'élément
	param v ( ) : valeur à rechercher
	param d (int) : indice de début de recherche dans le tableau
	param f (int) : indice de fin de recherche dans le tableau
	return (None/ ) : None si pas trouvé, position de v dans t sinon"""
    if d > f :
        return None
    milieu = (d+f)//2
    if t[milieu] < v :
        return recherche(t,v,milieu+1,f)
    elif t[milieu] > v :
        return recherche(t,v,d,milieu-1)
    else :
        return milieu
    
def recherche_dichotomique(t,v):
    """Algo de recherche dichotomique, renvoie None si pas trouvé, position de v dans t sinon,
    le tableau t est trié, v est la valeur à rechercher dans le tableau"""
    return recherche(t,v,0,len(t)-1)
```
