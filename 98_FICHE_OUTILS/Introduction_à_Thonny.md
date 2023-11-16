 # Introduction à Thonny :

------

## 1. Présentation

Thonny est un logiciel permettant de programmer en python. 

Celui-ci est sous la forme suivante :

![Thonny](./Images/thonny.jpg)

On le voit sur l'image il y a une partie 1 et une partie 2, à quoi servent elles ?

### Partie 1 :

Cette partie appelée **console** permettra exécuter des instructions directement **sans mémoire**. Il est par exemple possible d'écrire des calculs et d'avoir la réponse en appuyant sur la touche entrée.

- Attention, une fois une ligne écrite on ne peut revenir dessus
- Il est recommandé d'écrire une ligne à la fois

### Partie 2 : 

La deuxième partie, appelée **édition de programme** est la partie ou nous allons écrire le programme. Il pourra lui être **enregistré**. 

## 2. Comment utiliser ce logiciel ?

En règle générale, on écrit notre code dans la partie **édition de programme (partie 2)**, puis la **console (partie 1)** permet de voir les tests de notre code *(mais pas que)*.

<u>Voici un exemple de code :</u> 

```python
import time
print('Bonjour, bienvenu en NSI')
print('Voici la date du jour ainsi que l\'heure: '+time.ctime())
a = 6
b = 7
c = 'Les résultats des calculs de a+b, a-b, a*b sont : '+ str(a+b) + ' ' + str(a-b) + ' ' + str(a*b)
print(c)
```

Afin d'utiliser ce code, il faut le copier et le coller dans l'édition de programme, puis on appuie sur la flèche verte situé au dessous du menu horizontal (celui qui contient : *Fichier, Edition, Affichage ...*).

Une fois appuyé il faut enregistrer notre fichier en lui donnant un nom. Et le résultats des instructions ci-dessus **affichera** quelque chose dans la console

<u>Autre exemple de code :</u>

```python
import random

def jeu():
    print('Bienvenue au jeu du pierre feuille ciseau')
    t = ["Pierre","Feuille","Ciseau"]
    m_gagnée = 0
    manches = 0
    while manches < 3 :
        choix = input('Choissisez entre "Pierre", "Feuille", "Ciseau"')
        while choix not in t :
            choix = input('Choissisez entre "Pierre", "Feuille", "Ciseau" (Sans fautes !!!)')
        choix2 = random.randint(0,2)
        if t.index(choix) == choix2 :
            print("Egalité, l'ordinateur a choisi "+t[choix2])
        elif t.index(choix) == (choix2-1) or (choix == 'Ciseau' and choix2 == 0) :
            print("Manche perdue, l'ordinateur a choisi "+t[choix2])
        else : 
            print("Manche gagnée, l'ordinateur a choisi "+t[choix2])
            m_gagnée = m_gagnée + 1
        manches = manches + 1
    if m_gagnée < 2 :
        print('Vous avez perdu')
    else : 
        print('Vous avez gagné')
```

Même démarche, copiez puis collez le code. Puis une fois exécuté écrivez dans la console **jeu()**

Puis, lorsqu'on vous demande de jouer, jouez.