import class_vehicule

class Game :

    def __init__(self,nb_col,vehicules=[]) :
        """Class permettant de gerer la classe game, qui permet de gerer le plateau

        Args:
            nb_col (int): Nombre de colonnes du plateau
            vehicules(list) : Véhicule à ajouter dans le plateau.
        """
        self.plateau = [[' ' for _ in range(nb_col)] for _ in range(nb_col)]
        self.taille = len(self.plateau)
        # Liste des véhicules dans le tab (pour modifier/ selectionner)
        self.vehicules = []
        for element in vehicules :
            self.pose_vehicule(element)     
    
    def verif_pose(self,vehicule):
        if vehicule.direction == 'V' and ((vehicule.coord_y + vehicule.taille) <= len(self.plateau)):
            for i in range(vehicule.taille) :
                if self.plateau[vehicule.coord_y+i][vehicule.coord_x] != ' ' :
                    return False
        elif vehicule.direction == 'H' and ((vehicule.coord_x + vehicule.taille) <= len(self.plateau)):
            for i in range(vehicule.taille) :
                if self.plateau[vehicule.coord_y][vehicule.coord_x+i] != ' ' :
                    return False
        else :
            return False
        return True
    
    def pose_vehicule(self,vehicule) :
        if self.verif_pose(vehicule) :#== True :
            # Ajout du vehicule dans le tableau
            self.vehicules.append(vehicule)
            if vehicule.direction == 'V' :
                for i in range(vehicule.taille) :
                    self.plateau[vehicule.coord_y+i][vehicule.coord_x] = vehicule.nom
            else :
                for i in range(vehicule.taille) :
                    self.plateau[vehicule.coord_y][vehicule.coord_x+i] = vehicule.nom    
        else :
            print('Attention pose du véhicule, ',vehicule,' impossible')        
        
    def mouv_vehicule(self,vehicule):
        solution = []
        if vehicule.direction == 'H' :
            # Mouv droite :
            if (vehicule.coord_x+1+vehicule.taille < self.taille) and (self.plateau[vehicule.coord_y][vehicule.coord_x+vehicule.taille] == ' '):
                vehicules2 = []
                for element in self.vehicules :
                    if element.nom != vehicule.nom :
                        vehicules2.append(element)
                v2 = class_vehicule.Vehicule(vehicule.type_v,vehicule.direction,vehicule.coord_x+1,vehicule.coord_y,vehicule.nom)
                vehicules2.append(v2)
                solution.append((Game(self.taille,vehicules2),v2.nom + ' droite'))
            # Mouv gauche :
            if (vehicule.coord_x-1 >= 0) and (self.plateau[vehicule.coord_y][vehicule.coord_x-1] == ' '):
                vehicules2 = []
                for element in self.vehicules :
                    if element.nom != vehicule.nom :
                        vehicules2.append(element)
                v2 = class_vehicule.Vehicule(vehicule.type_v,vehicule.direction,vehicule.coord_x-1,vehicule.coord_y,vehicule.nom)
                vehicules2.append(v2)
                solution.append((Game(self.taille,vehicules2),v2.nom + ' gauche'))
        else :
            # Mouv bas :
            if (vehicule.coord_y+1+vehicule.taille < self.taille) and (self.plateau[vehicule.coord_y+vehicule.taille][vehicule.coord_x] == ' '):
                vehicules2 = []
                for element in self.vehicules :
                    if element.nom != vehicule.nom :
                        vehicules2.append(element)
                v2 = class_vehicule.Vehicule(vehicule.type_v,vehicule.direction,vehicule.coord_x,vehicule.coord_y+1,vehicule.nom)
                vehicules2.append(v2)
                solution.append((Game(self.taille,vehicules2),v2.nom + ' haut'))
            
            # Mouv haut : 
            if (vehicule.coord_y-1 >= 0) and (self.plateau[vehicule.coord_y-1][vehicule.coord_x] == ' '):
                vehicules2 = []
                for element in self.vehicules :
                    if element.nom != vehicule.nom :
                        vehicules2.append(element)
                v2 = class_vehicule.Vehicule(vehicule.type_v,vehicule.direction,vehicule.coord_x,vehicule.coord_y-1,vehicule.nom)
                vehicules2.append(v2)
                solution.append((Game(self.taille,vehicules2), v2.nom + ' bas'))
        return solution


    def __repr__(self):
        s = ''
        for ligne in self.plateau :
            s+= '|'
            for colonne in ligne :
                s+=' '+colonne+ ' |'
            s+= '\n'
        return s
    
    def __str__(self):
        '''Permet de donner une représentation en type str de la classe game'''
        s = ''
        for ligne in self.plateau :
            s+= '|'
            for colonne in ligne :
                s+=' '+colonne+ ' |'
            s+= '\n'
        return s

if __name__ == '__main__' :
    g = Game(6)
    v = class_vehicule.Vehicule('Camion','H',0,0,'J')
    v2 = class_vehicule.Vehicule('Camion','H',0,1,'R')
    print(g)
    print(g.pose_vehicule(v))
    print(g)
    print(g.pose_vehicule(v2))
    print(g)
    for i in g.vehicules :
        print(g.mouv_vehicule(i))
    print(str(g)+' ense')