# Fiche de révision : Exercices de 1ère

------

## Objectifs :

- Rappel de la syntaxe python
- Rappel de quelques fonction clés du cours de 1ère

## 1. Syntaxe python

1) Quel mot clé permet de définir une fonction?
2) Quels sont les deux types de boucles? Comment les différencier ?
3) Que permet le mot clé *return* ?
4) Que permet la fonction *print( )*

 ## 2. Rappel 1 ère :

### <u>2. 1. Plus grand que :</u>

Ecrire un prédicat *plus_grand_que(a,b)* qui prend en paramètre *a* et *b* et renvoie True si *a* est supérieur à *b*.

### <u>2. 2. Pythagore :</u>

Ecrire une fonction *Pythagore(cote1,cote2,hypothenuse)* qui renvoie un booléen si les trois côtés forment un triangle rectangle

### <u>2. 3. Tableaux :</u>

Ecrire une fonction *somme(t)* qui additionne tous les éléments d'un tableau et renvoie cette somme

### <u>2. 4. Fonction de tri :</u>

Expliquez le tri par sélection et le tri par insertion avec des exemples.

### <u>2. 5. Recherche dichotomique :</u>

1. Expliquez la recherche dichotomique

2. Quelle est la condition nécessaire pour faire cette recherche

3. Complétez le code ci-dessous :

   ```python
   def recherche_dichotomique(t, v):
       """
       Fonction qui applique la recherche dichotomique dans un tableau
       param tableau : Tableau où l'on va rechercher une valeur
       param valeur : valeur à retrouver
       return : Renvoie l'indice de la position de val, -1 si val n'est pas dans le tableau
       """
       debut = 0
       fin = ................
       while .............. :
           milieu = ............
           if t[milieu] > v :
               .....................
           elif t[milieu] < v :
               .....................
           elif t[milieu] == v :
               .....................
       return ..........
   ```


### <u>2. 6. Dentiste</u> :

Chez le dentiste, la bouche grande ouverte, lorsqu’on essaie de parler, il ne reste que les voyelles. Même les ponctuations sont supprimées.
Vous devez écrire une fonction `dentiste(texte)` qui renvoie un texte ne contenant que les voyelles de `texte`, dans l'ordre.
On ne considérera que des textes écrits en minuscules, sans accents. 
Voici des exemples d’appels de fonction :

```python
>>> dentiste("j'ai mal")
'aia'
>>> dentiste("il fait chaud")
'iaiau'
>>> dentiste("")
''
```

1. Quel est le type de la valeur de retour de cette fonction ?
2. Ecrire la fonction dentiste( )
3. Ecrire un appel de fonction permettant d’obtenir le résultat suivant :  ‘eeyae’