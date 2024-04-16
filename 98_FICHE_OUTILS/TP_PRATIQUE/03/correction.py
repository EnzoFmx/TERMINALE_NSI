def maxi(t):
    max_val = t[0]
    for i in range(len(t)-1) :
        if t[i]>max_val:
            max_val = t[i]
    return max_val

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []
    def est_vide(self):
        return self.contenu == []
    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)
    def depiler(self):
        assert not self.est_vide()
        return self.contenu.pop()
def bon_parenthesage(ch):
    p = Pile()
    for c in ch:
        if c == '(':
            p.empiler(c)
        elif c == ')':
            if p.est_vide():
                return False 
            else:
                p.depiler()
    return p.est_vide()