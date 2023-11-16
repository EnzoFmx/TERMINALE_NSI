# TD Récursivité :

------

## 1. Application du cours 

### 1. 1. Fonction somme :

Combien d'appel de fonction sont nécessaire pour somme(0), somme(5) et somme(n) ? 

> Il faut 1 appels pour somme(0), 6 pour somme(5), n+1 pour somme(n)

### 1. 2. Fonction factorielle  :

1) 

```python
def factorielle(n) :
	if n == 0 :
		return 1
	else :
		return n * factorielle(n-1)
```

2) 

> Il y aura factorielle(4), factorielle(3), factorielle(2), factorielle(1), factorielle(0) 

### 2. 1. Fonction mystère :

1. Que fait la fonction mystère ci-dessous : 

> La fonction mystère affiche les entiers entre i et k

### 2. 2. Nombre de chiffre d'un nombre :

Ecrire une fonction nb_chiffre(n) permettant d'obtenir le nombre de chiffre d'un nombre :

```python
def nb_chiffre(n) :
	if n <= 9 :
        return 1 
    else : 
        return 1 + nb_chiffre(n//10)
```

### 2. 3. Maximum d'un tableau :

```python
def maximum(t):
    if len(t) == 0:
        return -1
    elif len(t) == 1 :
        return t[0]
    else :
        return max(t[0], maximum(t[1:]))
```

## 3. Bonus : 

### 3. 1. Suite de Syracuse :

```python
def syracuse(u):
    print(u)
    if u > 1 :
        if u%2 == 0 :
            return syracuse(u//2)
        else :
            return syracuse(u*3 + 1)
```

### 3. 2. Dentiste

```python
def dentiste(texte) :
    voyelles = ["a","e","i","o","u","y"]
    if len(texte) == 1 :
        if texte[0] in voyelles :
            return texte[0]
    else :
        if texte[0] in voyelles :
            return texte[0] + dentiste(texte[1:])
        else :
            return dentiste(texte[1:])
```

### 3. 3. Combine deux tableaux :

```python
def combine(t,t2):
    if len(t) > 0 and len(t2)> 0 :
        if t[0] < t2[0] :
            return [t[0]] + combine(t[1:],t2)
        else :
            return [t2[0]] + combine(t,t2[1:])
    elif len(t)>0:
        return t
    elif len(t2)>0 :
        return t2
    else :
        return []
```

