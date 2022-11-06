class Liste :
    def __init__(self, element,queue = None):
        '''Classe permettant de manipuler les listes chaînées
        param element : (..) Element de la liste
        param queue : (Liste) Queue de la liste'''
        self.element = element
        self.queue = queue
    
    def est_vide(self):
        """
        Renvoie Vrai si la liste est vide.
        :return: (bool) Vrai si la liste est vide, Faux sinon.
        Exemple:
        >>> l1 = Liste()
        >>> l1.est_vide()
        True
        >>> l2 = Liste([1,2,3])
        >>> l2.est_vide()
        False
        """
        if self.queue == None :
            return self.element == None
        else :
            return self.element == None and self.queue.est_vide()

    def ajouter_element_queue(self,element):
        '''Methode ajoutant un élement à la queue de la liste chaînée
        param element: ( ) Element à ajouter'''
        if self.queue == None :
            self.queue = Liste(element)
        else :
            self.queue.ajoute_element_queue(element)
    
    def __len__(self):
        '''Renvoie la longueur de la liste'''
        if self.queue == None :
            return 1
        else :
            return 1 + self.queue.__len__()
    
    def extrait_element(self,ind):
        '''Renvoie l'élément à la position i
        param ind : (int) Indice de la liste
        return : ( ) Element de la liste
        CU : ind > self.len()'''
        if ind == 0 :
            return self.element
        else :
            return self.queue.extrait_element(ind-1)
    def cherche_element(self,element):
        '''Cherche un element dans la liste
        param element : ( ) Element à chercher
        return : (int) Indice de l'élément, si élément non présent renvoie la longueur de la liste'''
        if element== self.element :
            return 0
        else :
            if self.queue == None :
                return 1
            else :
                return 1 + self.queue.cherche_element
        
    def __repr__(self):
        '''Permet de representer la liste'''
        s = '[' + str(self.element)
        suivant = self.queue
        while suivant != None:
            s += ','+str(self.element)
            suivant = self.queue
        return s+'['
    
    #Méthode sans copie profonde
    def add(self,other):
        '''Permet d'ajouter une liste à une autre
        param other : (Liste) Liste à ajouter à self'''
        if self.queue = None :
            self.queue = other
        else :
            self.queue.__add__(other)
    
    # Méthode avec réecriture de other
     def __add__(self,other):
        '''Permet d'ajouter une liste à une autre
        param other : (Liste) Liste à ajouter à self'''
        if self.queue = None :
            self.queue = Liste(other.element)
            if other.queue != None :
                self.queue.__add__(other.queue)
        else :
            self.queue.__add__(other)