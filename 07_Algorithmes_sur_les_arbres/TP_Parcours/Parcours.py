from Arbre import *
from Pile_File import *

def parcours_largeur(arbre):
    """Parcours en largeur de l'arbre
    Ne renvoie rien,affiche juste les noeuds visités"""
    f = File()
    f.enfile(arbre)
    while f.est_vide() == False :
        n = f.defile()
        if n.fils_gauche.valeur != None :
            f.enfile(n.fils_gauche)
        if n.fils_droit.valeur != None :
            f.enfile(n.fils_droit)
        print(n.valeur)
            
def parcours_profondeur(arbre):
    print(arbre.valeur)
    if arbre.fils_gauche.valeur != None :
        parcours_profondeur(arbre.fils_gauche)
    if arbre.fils_droit.valeur != None :
        parcours_profondeur(arbre.fils_droit)