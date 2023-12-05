# Implémentation des parcours : 

------

Considérons cette classe d'arbre :

```python
class Arbre :
    """Classe Arbre, permettant de créer des arbres binaire"""
    def __init__(self,valeur=None,fils_gauche=None,fils_droit=None):
        """
        Méthode constructeur permettant de créer un arbre
        param valeur : (int/str) Valeur du noeud
        fils_gauche/fils_droit : (Arbre/None) Fils gauche/droit de l'arbre
        """
        self.valeur = valeur
        self.fils_droit = fils_droit
        self.fils_gauche = fils_gauche
```

Le but du TP est d'implémenter les parcours des arbres. Des fichiers (arbres et pile_file) sont disponibles pour récupérer les classes.

Il faut écrire les parcours dans un nouveau fichier et importer les fichiers disponibles.

## 1. Parcours en largeur

L'implémentation du parcours en largeur se fait en itératif. Afin de savoir quel sommet est à parcourir on utilise une **file**.

Explication brève du parcours :

- On met chaque nœud dans la file.
- Si la file est vide, on arrête l'algorithme
- On ajoute à la file, le fils gauche et fils droit de chaque nœud (s'il existe)

On affiche chaque nœud défilé.

**Ecrire l'algorithme en Python de ce parcours**

## 2. Parcours en profondeur

 L'implémentation du parcours en profondeur se fait en récursif !! Aucune structure n'est utilisée (Sauf l'arbre)

**Ecrire les algorithmes en Python de ce parcours (Préfixe,Infixe,Postfixe)**

Il y a 3 types de parcours pour le parcours en profondeur, d'abord le **préfixe**, on affiche le nœud, puis le fils gauche et le fils droit. 
Il existe aussi des parcours dis **infixe** où l'on affiche le fils gauche, la racine et le fils droit
Il existe aussi un dernier parcours dis **postfixe** ou l'on affiche d'abord le fils gauche, puis le fils droit, et la racine.

## 3. Utilisation de l'algorithme

Créer des arbres permettant d'utiliser vos algorithmes et d'afficher :

- A B C D E F pour un parcours en profondeur
- A B C D E F H pour un parcours en largeur.
