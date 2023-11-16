class Pile :
    def __init__(self):
        self.elements = []
    def empile(self,el):
        self.elements.append(el)
        # self.elements = [el] + self.elements
    def depile(self):
        s = self.elements[:len(self.elements)-1]
        
        
    def est_vide(self):
        return len(self.elements)==0