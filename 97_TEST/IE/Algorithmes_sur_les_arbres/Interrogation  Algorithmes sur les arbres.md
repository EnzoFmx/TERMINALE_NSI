# Interrogation : Algorithmes sur les arbres

Voici deux arbres :

1. Appliquer le parcours en largeur et en profondeur sur ces arbres. (2pts)

<u>Implémentation :</u>

2. Nous utilisons une file pour l'implémentation d'un des deux parcours, le quel ? Et pourquoi? (1pt)

Bonus. Le	quel des deux parcours permet de retrouver une valeur proche en premier? Pourquoi?

<u>Voici un algorithme :</u> 

```
#Algo 1 :
def mystere(arbre):
    print(arbre.valeur)
    if arbre.fils_gauche.valeur != None :
        mystere(arbre.fils_gauche)
    if arbre.fils_droit.valeur != None :
        mystere(arbre.fils_droit)
#Algo 2 :
def ajoute_element(element,arbre) :
    if ................ :
        if .................... != None :
            ajoute_element(element,....................)
        else :
            .................... = Arbre(element,Arbre(),Arbre())
    else :
        if .................... != None :
            ajoute_element(element,....................)
        else :
            .................... = Arbre(element,Arbre(),Arbre())
```

3. Que fait l'algorithme 1 ? Quel nom pourrait on lui donner ? (1pt) 
4. Ecrire la documentation de l'algorithme mystère (1pt)
5. Ecrire sur votre feuilles les lignes manquantes de l'algorithme 2. (3pts)
6. Expliquez le principe de la recherche d'un élément dans un ABR. (2pts)