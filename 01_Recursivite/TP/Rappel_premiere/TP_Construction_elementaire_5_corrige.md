# TP 5 Corrigé :

<h2><u> Exercice 1 :</h2></u> 

### Question 1 :
Un carré est dessiné

### Question 2 :

- reset() : Permet de reinitialiser le dessin
- home() : Permet de revenir au point (0,0)
- up() : Lève le stylo
- down() : Baisse le stylo
- goto(x,y) : Place le curseur au point x,y
- forward(x) : Avance le stylo d'une distance x
- left(x) : Tourne à gauche de x degrés
- right(x) : Tourne à droite de x degrés

### Question 3 : 

```python
def carre(cote):
    """
    Dessine un carre de longueur cote
    param cote : (int) longueur du cote du carre
    """
    #Facultatif
    turtle.up()
    turtle.goto(-50,-50)
    turtle.down()
    #Obligatoire
    turtle.forward(cote)
    turtle.left(90)
    turtle.forward(cote)
    turtle.left(90)
    turtle.forward(cote)
    turtle.left(90)
    turtle.forward(cote)
```
<br><br><br><br><br><br><br><br><br><br>
<h2><u> Exercice 2 :</h2></u> 

```python
def triangle_equilateral(cote):
    """
    Dessine un triangle equilateral de longueur cote
    param cote : (int) longueur du cote du triangle equilateral
    """
    turtle.forward(cote)
    turtle.left(120)
    turtle.forward(cote)
    turtle.left(120)
    turtle.forward(cote)
```
<h2><u> Exercice 3 :</h2></u> 

### Question 1 :

```python
def hexagone(cote):
    """
    Dessine un hexagone de longueur cote
    param cote : (int) longueur du cote de l'hexagone
    """
    turtle.forward(cote)
    turtle.left(60)
    turtle.forward(cote)
    turtle.left(60)
    turtle.forward(cote)
    turtle.left(60)
    turtle.forward(cote)
    turtle.left(60)
    turtle.forward(cote)
    turtle.left(60)
    turtle.forward(cote)
    turtle.left(60)
```
<br><br><br><br><br><br><br><br><br>
### Question 2 :

```python
def rose(cote):
    """
    Dessine une rose d'hexagone
    param cote : (int) longueur du cote des l'hexagones de la rose
    """
    hexagone(cote)
    turtle.left(90)
    hexagone(cote)
    turtle.left(90)
    hexagone(cote)
    turtle.left(90)
    hexagone(cote)
```

<h2><u> Exercice 4 :</h2></u> 


```python

def rectangle(longueur,largeur) :
    """
    Fonction qui dessine un rectangle
    param longueur : (int) Longueur des cotés du rectangle
    param largeur : (int) Largeur des cotés du rectangle
    """
    turtle.forward(largeur)
    turtle.left(90)
    turtle.forward(longueur)
    turtle.left(90)
    turtle.forward(largeur)
    turtle.left(90)
    turtle.forward(longueur)
    turtle.left(90)

def drapeau(longueur,largeur,coul1,coul2,coul3) :
    """
    Fonction qui dessine un drapeau
    param longueur : (int) Longueur des cotés des rectangles
    param largeur : (int) Largeur des cotés des rectangles
    param coul1 : (str) Couleur numéro 1
    param coul2 : (str) Couleur numéro 2
    param coul3 : (str) Couleur numéro 3
    """
    #Rectangle1
    turtle.fillcolor(coul1)
    turtle.begin_fill()
    rectangle(longueur,largeur)
    turtle.end_fill()
    #On replace le stylo
    turtle.up()
    turtle.forward(largeur)
    turtle.down()
    #Rectangle2
    turtle.fillcolor(coul2)
    turtle.begin_fill()
    rectangle(longueur,largeur)
    turtle.end_fill()
    #On replace le stylo
    turtle.up()
    turtle.forward(largeur)
    turtle.down()
    #Rectangle3
    turtle.fillcolor(coul3)
    turtle.begin_fill()
    rectangle(longueur,largeur)
    turtle.end_fill()

#Exemple d'utilisation : drapeau(50,25,"blue","white","red")

```


<h2><u> Exercice 5 :</h2></u> 

```python

def triforce(longueur,coul1,coul2,coul3) :
    """
    Fonction qui dessine une triforce (3 triangles)
    param longueur : (int) Longueur des cotés des triangle equilateraux
    param coul1 : (str) Couleur numéro 1
    param coul2 : (str) Couleur numéro 2
    param coul3 : (str) Couleur numéro 3
    """
    #Triangle 1
    turtle.fillcolor(coul1)
    turtle.begin_fill()
    triangle_equilateral(longueur)
    turtle.end_fill()
    #On replace le stylo
    turtle.up()
    turtle.forward(longueur)
    turtle.left(120)
    turtle.down()
    #Triangle 2
    turtle.fillcolor(coul2)
    turtle.begin_fill()
    triangle_equilateral(longueur)
    turtle.end_fill()
    #On replace le stylo
    turtle.up()
    turtle.left(120)
    turtle.forward(longueur)
    turtle.down()
    #Triangle 2
    turtle.fillcolor(coul3)
    turtle.begin_fill()
    triangle_equilateral(longueur)
    turtle.end_fill()
```