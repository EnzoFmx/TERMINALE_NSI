# TP Pile

------

## 1. Implémentation de la pile :

Afin d'implémenter la pile il nous faut utiliser une structure de données permettant de stocker des informations.

1. Trouver une structure de données adéquate permettant de réaliser les méthodes liées à la Pile

2. Implémenter la Pile (Constructeur et méthodes associées)

3. Implémenter la méthode *\_\_repr\_\_( )* permettant d'afficher la Pile crée

   ​	*Exemple :*

```python
>>> p = Pile()
>>> p 
[ ]
>>> p.empile(7)
>>> p.empile(9)
>>> p 
9
7
```

## 2. Exercices : 

### 2. 1. Bon parenthésage

1.  Ecrire une fonction *bien_parenthese*( ) vérifiant si une chaîne de caractère est bien parenthésée ou non. La valeur de retour sera un booléen. On vérifie les parenthèses '( )' ainsi que les crochets '[ ]'

   ```python
   >>> bien_parenthese("(oui)")
   True
   >>> bien_parenthese("(ou(i)")
   False
   >>> bien_parenthese("(o[u]i)")
   True
   >>> bien_parenthese("(ou][i)")
   False
   ```

    

## 2. 2. Calculatrice polonaise inverse 

La calculatrice polonaise inverse permet de faire des calculs simple mais pose l'opérateur après les deux opérandes. 

<u>Par exemple :</u>

5 + 8 + 9 => 5 8 + 9 + 

7 * 8 + 9 * 2 => 7 8 * 9 2 * + 

1. Ecrire une fonction calculatrice( ) prenant une chaîne de caractère en paramètre qui sera un calcul en polonais inverse et le résout.

```python
>>> calculatrice("5 8 + 9 + ")
22
>>> calculatrice("7 8 * 9 2 * + ")
74
>>> calculatrice("11 4 +")
15
```

> Ici il y a plusieurs points important.
> Il faut pouvoir découper la chaîne de caractères en plusieurs données. (split())
>
> Les éléments traités sont des chaînes de caractères => '11' '+' '4' ne veut rien dire
> De la même manière =>  '11' + '4' => '114'

## 2. 3. Tri d'une pile

Le but ici est de trier une pile. Pour cela nous utiliserons une autre pile temporaire permettant de stocker les éléments.

1.  Ecrire une fonction tri_pile( ) prennant en paramètre une pile et renvoyant la pile triée.

> L'idée ici est d'utiliser seulement deux piles. Afin de comprendre le fonctionnement il faut faire quelques essais à la main.

```python
>>> >>> p = Pile()
>>> p 
>>> p.empile(7)
>>> p.empile(1)
>>> p.empile(3)
>>> p.empile(9)
>>> p
9
3
1
7
>>> tri_pile(p)
1
3
7
9
```

