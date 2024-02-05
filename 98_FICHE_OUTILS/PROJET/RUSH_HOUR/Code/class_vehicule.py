class Vehicule :

    def __init__(self,type_v,direction,coord_x,coord_y,nom) :
        self.type_v = type_v
        if self.type_v == 'Camion' :
            self.taille = 3
        else :
            self.taille = 2
        self.direction = direction
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.nom = nom

    def __repr__(self) :
        return "{} {} ({},{}) {}".format(self.type_v,self.nom,self.coord_x,self.coord_y,self.direction)
    
if __name__ == '__main__' :
    v = Vehicule('Camion','H',0,0,'J')
    print(v)

