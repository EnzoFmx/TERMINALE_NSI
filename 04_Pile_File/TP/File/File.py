import Module_liste.Liste_chainee as Liste

# File non récursive
class File1 :
    
    def __init__(self) :
        """
        Méthode d'initialisation
        param liste : (List) Liste d'élément à enfiler dès l'initialisation
        """
        self.file = []
        
    def enfile(self,x) :
        """
        Méthode qui enfile un élément x
        param x : () Elément x à enfiler
        """
        self.file.append(x)

    def defile(self) :
        """
        Méthode qui defile un élément de la file
        return : (bool/ ) False si impossible de retirer l'élément / Elément sinon
        """
        if not self.est_vide() :
            tmp = self.file[0]
            self.file = self.file[1:]
            return tmp
        
    def est_vide(self):
        """
        Méthode testant la longueur de la file
        return : (bool) True si la file est vide, False sinon
        """
        return self.file == []
    
    def taille(self):
        """
        Méthode retournant la taille de la file
        return : (int) taille de la file
        """
        return len(self.file)
<<<<<<< HEAD
    
    def __len__(self):
        return len(self.file)
    
=======
>>>>>>> 54a657adfdd7a5f0846c0d308d9d2d411e2f5d8d


    # EXERCICE 2
    
    def ajout_element(self,element):
        """
        Fonction qui ajoute un élément, si la taille le permet.
        return (bool): Renvoie True si l'ajout de l'élément a eu lieu, False sinon
        """
        if file.taille() < 5 :
            file.enfile(fichier)
            return True
        else :
            return False
    
    def vide_file(self):
        """
        Fonction qui vide une file et affiche ces éléments
        """
        while file.est_vide() == False :
            e = file.defile()
            print(e)
            
#File récursive
class File2 :
    
    def __init__(self) :
        """
        Méthode d'initialisation
        param liste : (List) Liste d'élément à enfiler dès l'initialisation
        """
        self.file = Liste.Liste()
        
    def enfile(self,x) :
        """
        Méthode qui enfile un élément x
        param x : () Elément x à enfiler
        """
        if self.file.est_vide() :
            self.file.element = x
        else :
            self.file.ajouter_element_queue(x)

    def defile(self) :
        """
        Méthode qui defile un élément de la file
        return : (bool/ ) False si impossible de retirer l'élément / Elément sinon
        """
        if not self.est_vide() :
            tmp = self.file.tete
            self.file = self.file.queue
            return tmp
        
    def est_vide(self):
        """
        Méthode testant la longueur de la file
        return : (bool) True si la file est vide, False sinon
        """
        return self.file.est_vide()

    def taille(self):
        """
        Méthode retournant la taille de la file
        return : (int) taille de la file
        """
        return len(self.file)
    