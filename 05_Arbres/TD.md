# Arbres binaires

------

## 1. Arbres et définitions

Soit les 4 arbres binaires suivant :

<div style="display: flex; justify-content: space-around;">
<img src="./images/img2.PNG" alt="Méthodes_natives" style="zoom: 80%;" />

<img src="./images/img3.PNG" alt="Méthodes_natives" style="zoom: 80%;" />
</div>

<div style="display: flex; justify-content: space-around;">
<img src="./images/img4.PNG" alt="Méthodes_natives" style="zoom: 80%;" />

<img src="./images/img5.PNG" alt="Méthodes_natives" style="zoom: 80%;" />
</div>

1. Compléter le tableau :

| arbres  | taille | hauteur | Profondeur |
| :-----: | :----: | :-----: | :--------: |
| Arbre 1 |        |         |            |
| Arbre 2 |        |         |            |
| Arbre 3 |        |         |            |
| Arbre 4 |        |         |            |

2. En utilisant la classe **BinnaryTree** du module ```arbres_binary_tree```, donner la définition :

- en plusieurs affectations (plusieurs lignes) de l'arbre ayant pour racine le nœud **4** ;
- en une seule affectation (une ligne) de l'arbre ayant pour racine le nœud **1**.

![arbre binaire](./images/img6.PNG)

3. Dessiner les arbres de ces définitions :

```python
vide = BinaryTree()

# Premier arbre : F
A = BinaryTree("A", vide, vide)
E = BinaryTree("E", vide, vide)
I = BinaryTree("I", vide, vide)

B = BinaryTree("B", A, vide)
D = BinaryTree("D", vide, E)
H = BinaryTree("H", vide, I)

C = BinaryTree("C", B, D)
G = BinaryTree("G", vide, H)

F = BinaryTree("F", C, G)

# Deuxième arbre : J
J = BinaryTree("A", BinaryTree("B", vide, BinaryTree("F", vide, vide)), BinaryTree("D", BinaryTree("E", vide, vide), BinaryTree("C", vide, vide)))
```

## 2. Arbre binaire de recherche :

1. Parmi les 5 arbres binaires ci-dessous, lesquels sont des ABR ?

![ABR?](./images/img7.PNG)