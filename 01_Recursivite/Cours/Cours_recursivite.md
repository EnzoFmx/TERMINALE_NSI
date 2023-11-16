# Récursivité :

------

La récursivité est un style de programmation permettant de coder sans utiliser de boucle. Cela peut présenter un avantage lorsque l'on veut résumer le programme avec des problèmes simples.

**La fonction récursive s'appelle elle même dans sa définition.**

## 1. Mauvais exemple

Voici une fonction récursive :

```python
def fct_recursive() :
    print("Je fais un appel de la fonction")
    fct_recursive()
```

Cette fonction s'appelle elle même, mais elle présente un problème.<br> Si nous l'appelons, le résultat sera celui-ci : 

```python
>>> fct_recursive()
"Je fais un appel de la fonction"
"Je fais un appel de la fonction"
"Je fais un appel de la fonction"
"Je fais un appel de la fonction"
"Je fais un appel de la fonction"
"Je fais un appel de la fonction"
"Je fais un appel de la fonction"
...
```

Tout comme les boucles, il faut créer une instruction permettant d'arrêter l'exécution du code, en récursif nous l'appelons **le cas d'arrêt**. Il permettra d'éviter les appels **infinis**

## 2. Le cas d'arrêt 

Afin de stopper l'exécution du code il est donc essentiel de créer une instruction n'appelant pas notre fonction.

Par exemple : 

Voici la fonction somme(n) se définissant comme :

$$`somme(n) = \left\{ \begin{array}{ll}     0 {~si~} n = 0\\     n + somme(n -1){~sinon.} \end{array}\right.`$$

```python
def somme(n) :
    if n == 0 :
        return 0
    else :
        return n + somme(n-1)
```

Cette fonction s'appelle donc elle même jusqu'à avoir n égal à 0. 

Mais quel sera le résultat de *somme(3)* ? 

Pour obtenir cette réponse nous allons dérouler *à la main* le code : 

```
somme(3) = 3 + somme(2)
somme(2) = 2 + somme(1)
somme(1) = 1 + somme(0)
somme(0) = 0
```

Voici les différents appels de fonctions pour somme(3). Mais là, le résultat n'est pas encore obtenu.

Pour cela il faut pour cela reprendre les appels de fonctions pour revenir jusqu'à somme(3)

```
somme(0) = 0
somme(1) = 1 + 0 = 1 
somme(2) = 2 + 1 = 3
somme(3) = 3 + 3 = 6
```

Ici nous observons donc 4 appels de fonctions pour résoudre somme(3).

## 3. Appel de fonction en python 

En python il existe une limite au nombre d'appel de fonction que l'on peut faire pour une fonction récursive.

En effet, avec notre exemple nous voyons que pour obtenir somme(3) nous faisons 4 appels de fonction.

Ces appels de fonction **s'empilent** en espace mémoire, python peut stocker autour de 1000 appels.

Si cette limite est dépassée alors l'erreur **RecursionError** apparaîtra.

```python
>>> somme(1001)
...
RecursionError: maximum recursion depth exceeded in comparison
```

 ## 4. Autre type de récursivité  

Il existe divers types de récursivité : 

- La récursivité multiple
- La récursivité double
- La récursivité imbriquée
- etc ...

Ces différents types de récursivité sont quelques peu différents de ce que l'on vient de voir. Mais nous pourrions les rencontrer dans la suite du programme. 

### 4. 1. Récursivité double 

En effet à la différence de la récursivité dites *simple* il y aura ici plusieurs appels de fonctions dans une même instruction. 

<u>Suite de Fibonacci :</u>

$$`fibonacci(n) = \left\{ \begin{array}{ll}     0 {~si~} n = 0\\ 1 ~si~ n = 1 \\    fibonnaci(n-1) + fibonacci(n-2){~sinon.} \end{array}\right.`$$

```python
# En python

def fibonacci(n):
	if n == 0 : 
        return 0
    elif n == 1 :
        return 1
    else : 
        return fibonacci(n-1) + fibonacci(n-2)
```
