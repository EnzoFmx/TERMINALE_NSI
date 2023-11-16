class Etudiant : 
    def __init__(self,nom_etu,prenom_etu,spe1_etu,age_etu) :
        self.nom = nom_etu
        self.prenom = prenom_etu
        self.spe1 = spe1_etu
        self.age = age_etu
        self.nom_complet = nom_etu + ' ' + prenom_etu
        if self.age < 18 :
            self.peut_avoir_son_permis = False
        else :
            self.peut_avoir_son_permis = True
    
    def change_spe(self,nouvelle_spe) :
        self.spe = nouvelle_spe
    
    def anniversaire(self) :
        self.age = self.age + 1
        if self.age == 18 :
            self.peut_avoir_son_permis = True
    
    def nouvelle_spe(self,new_spe):
        self.spe2 = new_spe
        
    def __eq__(self,obj2):
        return self.spe1 == obj2.spe1
    
    def __repr__(self):
        return self.nom + ' ' + self.prenom
    
    def get_nom(self):
        return self.__nom

    def set_nom(self,nouveau_nom):
        self.__nom =  nouveau_nom
    

    