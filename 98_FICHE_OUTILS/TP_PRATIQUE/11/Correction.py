# exo 1
def nombre_de_mot(mot):
    tab = mot.split(" ")
    for i in range(len(tab)) :
        if tab[i] == "!" or tab[i] == "?" or tab[i] == "." :
            del(tab[i])
    return len(tab)

def nombre_de_mot2(mot):
    res = 0
    for i in mot :
        if i == ' ':
            res += 1
        elif i == '.':
            res += 1
    return res
            
        
# exo 2
class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.insere(cle)
            else:
                self.gauche = Noeud(cle) 
        else:
            if self.droit != None :
                self.droit.insere(cle)
            else:
                self.droit = Noeud(cle)