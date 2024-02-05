import class_vehicule
class Game :

    def __init__(self,nb_col,vehicules = []) :
        """Class permettant de gerer la classe game, qui permet de gerer le plateau

        Args:
            nb_col (_type_): _description_
        """
        self.plateau = [[' ' for _ in range(nb_col)] for _ in range(nb_col)]
        self.taille = len(self.plateau)
        # Liste des véhicules dans le tab (pour modifier/ selectionner)
        self.vehicules = vehicules
    
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
    
 

        
        



if __name__ == '__main__' :
    g = Game(6)
    v = class_vehicule.Vehicule('Camion','H',0,0,'J')
    v2 = class_vehicule.Vehicule('Camion','H',0,0,'R')
    print(g.plateau)
    print(g.pose_vehicule(v))
    print(g.plateau)
    print(g.pose_vehicule(v2))
    print(g.plateau)