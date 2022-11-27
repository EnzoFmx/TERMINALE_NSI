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
        return self.fils_droit.valeur == None and self.fils_gauche.valeur == None

def est_dans_arbre(arb,val):
    if arb.valeur == val :
        return True
    elif arb.valeur == None :
        return False
    else :
        return est_dans_arbre(arb.fils_gauche,val) or est_dans_arbre(arb.fils_droit,val)


arbre1 = Arbre(1,Arbre(12,None,None),Arbre(123,None,None))
arbre2 = Arbre("C",None,Arbre("A",None,Arbre("B",None,Arbre("E",None,None))))

def peigne_droit(h:int):
    """Fonction permettant de créer un arbre dit "peigne droit" ("branche" ici)
    param h : (int) hauteur de l'arbre
    return : (Arbre) Arbre"""
    assert(h!=0), 'Impossible de faire un arbre de hauteur 0'
    if h==1 :
        return Arbre(1,Arbre(None),Arbre(None))
    else :
        return Arbre(1,Arbre(None),peigne_droit(h-1))

def est_peigne_droit(a: Arbre):
    """Fonction permettant de vérifier si l'arbre est dit "peigne droit"
    param a : (Arbre) Arbre à tester
    return : (bool) True s'il est peigne droit, False sinon"""
    if a.fils_gauche.valeur != None :
        return False
    elif a.fils_droit.valeur == None :
        return True
    else :
        return True and est_peigne_droit(a.fils_droit)


# Test des fonctions

a = Arbre(12,Arbre(12,Arbre(None,None,None),Arbre(None,None,None)),Arbre(12,Arbre(None,None,None),Arbre(12,Arbre(None,None,None),Arbre(None,None,None))))
print('Taille de l\'arbre a',a.taille())
print('Hauteur de l\'arbre a',a.hauteur())
print('12 est dans l\'arbre ?',est_dans_arbre(a,12))
print('123 est dans l\'arbre ?',est_dans_arbre(a,123))

b = peigne_droit(6)
print('l\'arbre b est peigne droit ?',est_peigne_droit(b))

