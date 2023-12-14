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
        
    def taille(self):
        """Permet de renvoyer la taille de l'arbre
        Returns:
            int: Taille de l'arbre
        """
        if self.fils_droit == None and self.fils_gauche == None :
            return 1
        elif self.fils_droit == None :
            return 1 + self.fils_gauche.taille()
        elif self.fils_gauche == None :
            return 1 + self.fils_droit.taille()
        else :
            return 1 + self.fils_gauche.taille()+self.fils_droit.taille()
    
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
