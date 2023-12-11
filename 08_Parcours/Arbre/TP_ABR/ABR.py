class Arbre :
    """Classe Arbre, permettant de créer des arbres binaire"""
    def __init__(self,valeur=None,fils_gauche=None,fils_droit=None):
        """
        Méthode constructeur permettant de créer un arbre
        param valeur : (int/str) Valeur du noeud
        fils_gauche/fils_droit : (Arbre/None) Fils gauche/droit de l'arbre
        """
        self.valeur = valeur
        self.fils_droit = fils_droit
        self.fils_gauche = fils_gauche



    def __repr__(self):
       """Return a string which when eval'ed will rebuild tree"""

       return '{}({}, {}, {})'.format(
                 self.__class__.__name__,
                 repr(self.valeur),
                 repr(self.fils_gauche) if self.fils_gauche else None,
                 repr(self.fils_droit) if self.fils_droit else None) \
                      .replace(', None, None)', ')') \
                      .replace(', None)', ')')




# Algorithme en pseudo-code :
def ajout_element_dans_abr(element,arbre) :
    """Fonction permettant d'ajouter un élément dans un Arbre en respectant
    la définition d'un ABR"""
    if element <= arbre.valeur :
        if arbre.fils_gauche != None :
            ajout_element_dans_abr(element,arbre.fils_gauche)
        else :
            arbre.fils_gauche = Arbre(element)
    else :
        if arbre.fils_droit != None :
            ajout_element_dans_abr(element,arbre.fils_droit)
        else :
            arbre.fils_droit = Arbre(element)

def recherche_element_dans_ABR(element,arbre):
    """Fonction de recherche d'élément dans un ABR"""
    if element == arbre.valeur :
        return True
    elif element < arbre.valeur :
        if arbre.fils_gauche != None :
            return recherche_element_dans_ABR(element,arbre.fils_gauche)
    elif element > arbre.valeur :
        if arbre.fils_droit != None :
            return recherche_element_dans_ABR(element,arbre.fils_droit)
    return False

a = Arbre(5,None,None)
ajout_element_dans_abr(6,a)
ajout_element_dans_abr(6,a)
print(a)
print(recherche_element_dans_ABR(6,a))
print(recherche_element_dans_ABR(0,a))

