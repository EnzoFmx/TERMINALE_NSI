#PARTIE 
class File1 :
    
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
    
    def get_file(self):
        """
        Méthode retournant la file sous forme de liste pour en avoir un aperçu
        return : (list) file sous forme de list
        """
        return self.file
    
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

# PARTIE 3 :

class File2 :

    def __init__(self,tete = None,queue = None):
        """
        Méthode d'initialisation
        param tete : () Element a mettre en tete de file
        param queue : (File) queue de la file (élements suivants)
        """
        self.tete = tete
        self.queue = queue
    
    def enfile(self,x) :
        """
        Méthode qui enfile un élément x
        param x : () Elément x à enfiler
        """
        self.queue = File2(self.tete,self.queue)
        self.tete = x
       
    def defile(self) :
        """
        Méthode qui defile un élément de la file
        return : (bool/ ) False si impossible de retirer l'élément / Elément sinon
        """
        if self.est_vide() :
            return False
        if self.queue == None  :
            val = self.tete
            self.tete = None
            return val
        elif self.queue.queue == None :
            val = self.queue.tete 
            self.queue = None
            return val
        else :
            return self.queue.defile()
    
    def est_vide(self) :
        """
        Méthode testant la longueur de la file
        return : (bool) True si la file est vide, False sinon
        """
        return self.queue == None and self.tete == None
    
    def top(self):
        if self.suivant != None :
            return self.suivant.top()
        else:
            return self.element
    
    def taille(self):
        """
        Méthode retournant la taille de la file
        return : (int) taille de la file
        """
        if self.queue == None :
            return 1
        else :
            return 1 + self.queue.taille()
    
    def get_file(self):
        """
        Méthode retournant la file sous forme de liste pour en avoir un aperçu
        return : (list) file sous forme de list
        """
        if self.queue != None :
            return [self.tete] + self.queue.get_file()
        else :
            return [self.tete]
        

    
    
    