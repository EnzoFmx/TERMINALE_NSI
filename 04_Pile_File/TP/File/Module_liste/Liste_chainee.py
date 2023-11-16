class Liste :
    def __init__(self, element=None,queue = None):
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
        
    def extrait_element(self,i):
        if i == 0 :
            return self.element
        else :
            return self.queue.extrait_element(i-1)
        
    def __repr__(self):
        s='['
        if self.element != None :
            s += str(self.element)
        else:
            s+= ' '
        if self.queue != None: 
            stock = self.queue
            while self.queue != None :
                if stock.element != None :
                    s += ','+str(stock.element)
                else:
                    s+= ' '
                stock = stock.queue
        return s+']'
        
        
        
        
        
        
        
        
        
    
