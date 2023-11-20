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
        
    def hauteur(self):
        """Permet de renvoyer la hauteur de l'arbre
        Returns:
            int: Hauteur de l'arbre
        """
        if self.fils_droit == None and self.fils_gauche == None :
            return 1
        elif self.fils_droit == None :
            return 1 + self.fils_gauche.hauteur()
        elif self.fils_gauche == None :
            return 1 + self.fils_droit.hauteur()
        else :
            return 1 + max(self.fils_gauche.hauteur(),self.fils_droit.hauteur())
        
    def profondeur(self):
        """Permet de renvoyer la profondeur de l'arbre
        Returns:
            int: profondeur de l'arbre
        """
        return self.hauteur()-1
    
    def est_dans_larbre(self,v):
        """Permet de savoir si une valeur v est dans l'arbre
        Args:
            v (int): valeur a retrouver dans l'arbre

        Returns:
            bool: True si dans l'arbre, False sinon
        """
        if self.fils_droit == None and self.fils_gauche == None :
            return self.valeur == v
        elif self.fils_droit == None :
            return self.valeur == v or self.fils_gauche.est_dans_larbre(v)
        elif self.fils_gauche == None :
            return self.valeur == v or self.fils_droite.est_dans_larbre(v)
        else :
            return self.valeur == v or self.fils_droite.est_dans_larbre(v) or self.fils_gauche.est_dans_larbre(v)
    

def arbre_peigne_droit(h):
    """Fonction permettant de créer un arbre dit "peigne droit" ("branche" ici)
    param h : (int) hauteur de l'arbre
    return : (Arbre) Arbre"""

    if h == 1:
        return Arbre(h,None,None)
    else :
        return Arbre(h,None,arbre_peigne_droit(h-1))
    
def est_arbre_peigne_droit(a):
    """Fonction permettant de vérifier si l'arbre est dit "peigne droit"
    param a : (Arbre) Arbre à tester
    return : (bool) True s'il est peigne droit, False sinon"""
    if a.fils_gauche != None :
        return False
    else :
        if a.fils_droit == None :
            return True
        else :
            return est_arbre_peigne_droit(a.fils_droit)
# Est peigne droit sans récursivité
def v2(a):
    for i in range(a.hauteur()):
        if a.fils_gauche != None :
            return False
        else :
            a = a.fils_droit
    return True


def arbre_parfait(h):
    """Renvoie un arbre de hauteur h parfait
    Args:
        h (int): hauteur de l'arbre
    Returns:
        Arbre: Arbre parfait de hauteur h
    """
    if h == 1:
        return Arbre(h,None,None)
    else :
        return Arbre(h,arbre_parfait(h-1),arbre_parfait(h-1))

def est_parfait(a):
    """Permet de savoir si un arbre est parfait
    Args:
        a (Arbre): Arbre à tester
    Returns:
        bool: True si parfait, False sinon
    """
    if a.fils_droit == None and a.fils_gauche == None :
        return True
    elif a.fils_droit != None and a.fils_gauche == None :
        return False
    elif a.fils_gauche != None and a.fils_droit == None :
        return False
    else :
        return a.fils_droit.hauteur() == a.fils_gauche.hauteur() and \
            est_parfait(a.fils_droit) and est_parfait(a.fils_gauche) 
        
a = Arbre(12,Arbre(12,None,None),Arbre(12,None,Arbre(12,None,None)))
print('Taille de l\'arbre a',a.taille())
print('Hauteur de l\'arbre a',a.hauteur())
print('12 est dans l\'arbre ?',est_dans_arbre(a,12))
print('123 est dans l\'arbre ?',est_dans_arbre(a,123))

b = peigne_droit(6)
print('l\'arbre b est peigne droit ?',est_peigne_droit(b))

c = arbre_parfait(6)
print('l\'arbre b est parfait ?',est_parfait(c))
