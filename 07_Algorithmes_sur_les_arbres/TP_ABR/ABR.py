from Arbre import *

# Algorithme en pseudo-code :
def ajout_element_dans_abr(element,arbre) :
    """Fonction permettant d'ajouter un élément dans un Arbre en respectant
    la définition d'un ABR"""
    if element <= arbre.valeur :
        if arbre.fils_gauche.valeur != None :
            ajout_element_dans_abr(element,arbre.fils_gauche)
        else :
            arbre.fils_gauche = Arbre(element,Arbre(),Arbre())
    else :
        if arbre.fils_droit.valeur != None :
            ajout_element_dans_abr(element,arbre.fils_droit)
        else :
            arbre.fils_droit = Arbre(element,Arbre(),Arbre())


