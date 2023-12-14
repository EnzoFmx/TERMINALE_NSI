class Pile :

    def __init__(self) :
        """Méthode constructeur"""
        self.pile = []   
    def empile(self,x) :
        """
        Méthode qui enpile un élément
        param x : () Elément x à enpiler
        """
        self.pile.append(x)

    def depile(self) :
        """
        Méthode qui defile un élément de la pile
        return : (bool/ ) False si impossible de retirer l'élément / Elément sinon
        """
        if self.est_vide() :
            return False
        else :
            return self.pile.pop()
    def est_vide(self):
        """Méthode calculant la longueur de la pile"""
        return self.pile == []
    def top(self):
        """Méthode renvoyant l'élément au dessus de la pile"""
        return self.pile[-1]
    """def __repr__(self):
        long = len(self.pile)-1
        s = ''
        while long >= 0 :
            s+=str(self.pile[long])+'\n'
            long= long-1
        return s"""
    def __repr__(self):
        s = '['
        for i in self.pile:
            s += i + ' '
        return s+']'
    def taille(self):
        """Méthode permettant de connaître la taille de la pile"""
        return len(self.pile)
    
#PARTIE 
class File :
    def __init__(self,liste = []) :
        """
        Méthode d'initialisation
        param liste : (List) Liste d'élément à enfiler dès l'initialisation
        """
        self.file = liste
    def enfile(self,x) :
        """
        Méthode qui enfile un élément x
        param x : () Elément x à enfiler
        """
        self.file = [x] + self.file
    def defile(self) :
        """
        Méthode qui defile un élément de la file
        return : (bool/ ) False si impossible de retirer l'élément / Elément sinon
        """
        if not self.est_vide() :
            return self.file.pop()
        else :
            return False
    def est_vide(self):
        """
        Méthode testant la longueur de la file
        return : (bool) True si la file est vide, False sinon
        """
        return len(self.file) == 0
    def taille(self):
        """
        Méthode retournant la taille de la file
        return : (int) taille de la file
        """
        return len(self.file)
    def __repr__(self):
        s = '['
        for i in self.file:
            s += i + ' '
        return s+']'