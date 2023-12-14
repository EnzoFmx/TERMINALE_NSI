# Cours : Algorithmes liés aux graphes :

## 1. Rappel :

Les graphes sont composés de **sommets**, tous liés (ou non) entre eux par **des arêtes** ou **des arcs** (selon si le graphe est non orienté ou orienté). Ils ont différentes représentation : 

- Liste d'adjacence
- Matrice d'adjacence
- Dictionnaire d'adjacence

## 2. Parcours d'un graphe :

Un graphe peut être parcouru **en largeur et en profondeur** (tout comme les arbres) mais quelques différences sont notables :

1. **Cycle :** Un graphe peut contenir des cycles, tandis qu'un arbre n'en a pas.
2. **Connectivité :** Un graphe peut avoir plusieurs composantes connexes, alors qu'un arbre est toujours connexe.
   - On appelle connexe une structure pour la quelle chaque sommet `u` et `v` peuvent être reliés par une chaîne permettant de les relier.

### 2. 1. Parcours en largeur :

Le parcours en largeur se décrit comme suit :

```
Choix d'un noeud de départ
Enfile le noeud de départ

Tant que la file n'est pas vide :
	On defile un noeud appelé n
	On l'affiche
	On met chaque nœud voisin de n dans la file (si on ne les a pas encore visité)
```

Il faut gérer ici, les possibles cycles des graphes.

### 2. 2. Parcours en longueur :

Le parcours en longueur se décrit comme suit :

```
Choix d'un noeud de départ

Si le noeud de départ n'as pas été visité :
	On affiche le noeud de départ
	Pour chaque voisin à ce noeud :
			Parcours en profondeur du noeud voisin
```

Il faut gérer ici, les possibles cycles des graphes.

## 3. Présence d'un cycle :

A la différence d'un arbre, un graphe peut avoir des cycles. On parle d'un cycle lorsque lors d'un parcours du graphe, un sommet est visité au moins deux fois.

```
Lors du parcours d'un graphe :
	- Si le noeud à visiter est dans les noeuds déjà visités :
		Retourner Vrai
Retourner Faux	
```

## 4. Calcul du plus court chemin entre deux sommets :

Afin de déterminer le plus court chemin entre deux sommets nous allons utiliser le parcours en largeur. Ce parcours permet de parcours tous les sommets situés à 1 de distance par rapport au départ, puis ceux situé à 2 de distance, etc.. Il permet donc d'avoir le chemin entre deux sommets de manière optimale.

Pour cela :

```
Même raisonnement que le parcours en largeur sauf :
 - Lorsqu'on ajoute un noeuds dans la file, on l'ajoute sous forme de tuple :
 	- Le tuple est sous la forme (Noeud, [Chemin vers noeud])
 	- Le chemin vers le noeud vaut le chemin actuel + le noeud à visiter.
 	
- Dans la boucle principale :
	- Si on rencontre la destination (noeud final)
		- On renvoie le chemin
		
- Si on sort de la boucle, c'est que le chemin n'existe pas.
```

