class Auteur :
    def __init__(self,nom,naissance,deces = False):
        """
        Méthode constructeur de Auteur.
        param nom : (str) Nom de l'auteur
        param naissance : (int) année de naissance de l'auteur
        param deces : (int/bool) année de décès / False si toujours en vie"""
        self.nom = nom
        self.annee_naissance = naissance
        self.deces = deces

class Livre :
    def __init__(self,titre,genre,auteur):
        """Méthode constructeur de Livre
        param titre : (str) Titre du livre
        param genre : (str) Genre du livre
        param auteur: (Auteur) Auteur du livre"""
        self.titre = titre
        self.genre = genre
        self.auteur = auteur
  
    def __repr__(self):
        return self.titre

class Bibliotheque :
    def __init__(self,rayon):
        """Méthode constructeur de bibliothèque. L'ensemble des livres est vide
        lors de l'initialisation
        param rayon : (str) Type de livre que la biblio peut recevoir"""
        self.rayon = rayon
        self.ens_livre = []
        
    def add_livre(self,livre):
        """ Méthode permettant d'ajouter un livre.
        param livre (Livre): Livre à ajouter
        return : (str) précise si le livre est ajouté ou non"""
        if livre.genre == self.rayon :
            self.ens_livre.append(livre)
            return "Livre ajouté"
        else :
            return "Impossible d'ajouter le livre"
    
    
    
    
    
    
    def disponible(self,nom_livre) :
        for i in self.ens_livre :
            if nom_livre == i.titre :
                return True
        return False
    
    
    def est_dispo(self,nom_livre):
        """Méthode parcourant l'ensemble des livres de la biblio pour savoir si
        un livre est disponible
        param nom_livre : (str) Nom du livre à rechercher
        return : (int) Indice du livre si dispo, -1 sinon"""
        i = 0
        while i < len(self.ens_livre) :
                if self.ens_livre[i].titre == nom_livre :
                    return i
                i+=1
        return -1
    
    def prete_livre(self,nom_livre):
        """Méthode permettant de preter un livre s'il est dispo.
        param nom_livre : (str) nom du livre à emprunter
        return : (Livre/bool) Livre si emprunt possible, False sinon"""
        val = self.est_dispo(nom_livre)
        if  val != -1 :
            livre =  self.ens_livre[val]
            # Utilisation des slices pour supprimer le livre (Tester d'autres exemples
            # si pas compris)
            self.ens_livre = self.ens_livre[:val] + self.ens_livre[val+1:]
            return livre
        else :
            return False







    def prete_livre2(self,livre):
        """
        méthode permettant de préter un livre si celui-ci est dispo dans la bibliothèque
        param : self (Bibliothèque)
        param : livre (Livre)
        """
        if livre.genre == self.rayon :
            if self.disponible(livre.titre) == True :
                num_element = 0
                trouver = False
                while num_element < len(self.ens_livre) and trouver == False :                   
                    if livre.titre == self.ens_livre[num_element].titre :
                        l = self.ens_livre.pop(num_element)
                        trouver = True
                    num_element+=1
                if trouver == True :
                    return l
        return False
                    
                    









#Initialisation des valeurs :
a1 = Auteur('Bob',1990)
a2 = Auteur('Alice', 1998,2009)
l1 = Livre('Livre NSI terminale','Cours','Bob')
l2 = Livre('Livre NSI premiere','Cours',a2)
l3 = Livre('Les animaux de compagnies','Animaux',a1)
l4 = Livre('Les animaux sauvages','Animaux',a2)
b1 = Bibliotheque('Cours')
b2 = Bibliotheque('Animaux')


    





# Ajout des livres dans biblio :
b1.add_livre(l1)
b1.add_livre(l2)
"""
b1.add_livre(l3) #Impossible d'ajouter le livre

b2.add_livre(l3)
b2.add_livre(l4)
"""
#Pret d'un livre
print(b1.ens_livre)
b1.prete_livre('Livre NSI terminale')
print(b1.ens_livre)


#Dispo d'un livre
b2.est_dispo('Les animaux de compagnies')
b1.est_dispo('Livre NSI terminale') # Pas dispo
