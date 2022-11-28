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
        """Méthode renvoyant la taille de l'arbre
        return : (int) taille de l'arbre"""
        if self.valeur == None :
            return 0
        else :
            return 1 + self.fils_droit.taille() + self.fils_gauche.taille()
    def hauteur(self):
        if self.valeur == None :
            return 0
        else :
            return max(1+self.fils_gauche.taille(),1+self.fils_droit.taille())

    def profondeur(self):
        return self.hauteur()-1
    def est_feuille(self):
        return self.fils_droit is None and self.fils_gauche is None


a = Arbre(12,Arbre(12,Arbre(None,None,None),Arbre(None,None,None)),Arbre(12,Arbre(None,None,None),Arbre(12,Arbre(None,None,None),Arbre(None,None,None))))
