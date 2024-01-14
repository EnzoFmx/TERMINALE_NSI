# TP Diviser pour régner

------

## Tri fusion

### 1. 1. Première approche

Une fonction de tri s'applique à un tableau, ce tableau contient des éléments comparables entre eux. Le but est donc de les ranger par ordre croissant. Nous connaissons déjà le tri par insertion et le tri par sélection. Cependant en utilisant le principe de "diviser pour régner" il est possible de concevoir un tri plus efficace. Il est appelé "tri fusion".

Le tri fusion se décompose comme suit :

Le tri sépare le tableau en 2 moitiés égale (à un élément près pour les longueurs impaire) puis on trie avec le tri fusion et cela de manière récursive. Puis on trie les éléments des deux tableau triés, c'est la fusion.

1. Lorsque l'on découpe le tableau en deux parties, comment garantir que l'on arrivera à un tableau trié ?

2. Une fois ces tableaux triés obtenus, expliquer comment pouvons nous faire pour assembler ces tableaux et obtenir un nouveau tableau trié. (sans faire de code)

   ```
   Par exemple :
   Si l'on a [2,6,78] et [4,5,98] le résultat doit être [2,4,5,6,78,98]
   ```

3. Dessiner l'arbre de décomposition et de fusion du tableau [7,89,15,2,65,10,8,11,1]

### 1. 2. Implémentation

L'algorithme est composé de deux fonction :

- une fonction nommée *fusion( )* prenant en paramètre deux tableau trié et faisant la fusion des deux.
- une fonction nommée *tri_fusion( )* prenant en paramètre un tableau et le décompose en deux tableaux auxquels on appliquera tri_fusion
  - Les deux tableaux sont ensuite fusionnés grâce à *fusion( )* 

1. Ecrire dans un premier temps la fonction *fusion( )* prenant en paramètre deux tableaux triés et effectuant la fusion des deux tableaux.

   ```python
   >>> fusion([2,6,78],[4,5,98])
   [2,4,5,6,78,98]
   ```

   > Cette fonction ne doit pas être récursive. (=> Boucles)

2. Ecrire la fonction *tri_fusion( )* prenant en paramètre un tableau et effectue le tri fusion. La valeur renvoyée est le tableau trié
   - Décomposition en 2 tableaux
   - Tri fusion sur ces deux tableaux
   - Fusion des deux tableaux triés

### 1. 3. Complexité 

La complexité du tri fusion est intéressante à étudier. 

1. Pour cela, récupérez le fichier nommé *complexité.py* 
2. Expliquez les lignes 25 à 54
3. Exécutez le code
   1. Expliquez à quoi correspondent les courbes (c'est normal si elles ne sont pas lisses)
   2. Bonus : Pourquoi les courbes ne sont pas lisses ? 
4. Le tri fusion est-il plus efficace que les autres tris ? 
