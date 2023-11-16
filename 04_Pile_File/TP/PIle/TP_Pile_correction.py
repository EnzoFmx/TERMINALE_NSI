class Pile :
    
    def __init__(self) :
        """
        Méthode constructeur
        """
        self.pile = []
        
    def empile(self,x) :
        """
        Méthode qui enpile un élément
        param x : () Elément x à enpiler
        """
        self.pile.append(x)

    def depile(self) :
        """
        Méthode qui defile un élément de la pile
        return : (bool/ ) False si impossible de retirer l'élément / Elément sinon
        """
        if self.est_vide() :
            return False
        else :
            return self.pile.pop()
            
        
    def est_vide(self):
        """Méthode calculant la longueur de la pile"""
        return self.pile == []
    
    def top(self):
        """Méthode renvoyant l'élément au dessus de la pile"""
        return self.pile[-1]
    
    def __repr__(self):
        long = len(self.pile)-1
        s = ''
        while long >= 0 :
            s+=str(self.pile[long])+'\n'
            long= long-1
        return s
        
    def taille(self):
        """Méthode permettant de connaître la taille de la pile"""
        return len(self.pile)
    
    # TRI D UNE PILE AVEC 2 PILES
    def sort_stack(self):
        """Méthode qui renvoie la pile trié"""
        pile_tmp = Pile()
        while not self.est_vide() :
            val_tmp = self.depile()
            while pile_tmp.est_vide() == False and pile_tmp.top() < val_tmp:
                self.empile(pile_tmp.depile())
            pile_tmp.empile(val_tmp)
        p.pile = pile_tmp.pile
        return p
    
    
    
    
    
    
# TRI AVEC 3 PILE :   
def tri_pile(pile):
    pile_trie = Pile()
    pile_tmp = Pile()
    # s = pile.depile()
    # pile_triee.empile(s)
    pile_trie.empile(pile.depile())
    while pile.est_vide() == False :
        if pile.top() > pile_trie.top() :
            while pile_trie.est_vide() == False and pile.top() > pile_trie.top():
                pile_tmp.empile(pile_trie.depile())
            pile_trie.empile(pile.depile())
            while pile_tmp.est_vide() != False :
                pile_trie.empile(pile_tmp.depile())
        else :
            pile_trie.empile(pile.depile())
    while pile_trie.est_vide()==False:
        pile_tmp.empile(pile_trie.depile())
    while pile_tmp.est_vide() == False :
        pile.empile(pile_tmp.depile())
    

# BIEN PARENTHESE :
def bien_parenth(chaine) :
    p = Pile()
    for i in chaine :
        #Ouvrante
        if i == '(' or i == '[' :
            p.empile(i)
        #Fermante
        elif i == ')' or i == ']':
            dernier = p.depile()
            if dernier == False :
                return False
            else :
                if i ==')' :
                    if dernier != '(' :
                        return False
                else :
                    if dernier != '[' :
                        return False
        # Autre :
        else :
            pass
    return p.est_vide()
    
# CALCULATRICE POLONAISE INVERSE
def calculatrice(calcul):
    pile = Pile()
    i = 0
    while i <= len(calcul)-1 :
        if calcul[i] in '0123456789' :
            var  = ''
            while calcul[i] != ' ' :
                var += calcul[i]
                i += 1
            pile.empile(var)
        elif calcul[i] == '+' or calcul[i] =='-' or calcul[i] =='*':
            nb1 = pile.depile()
            nb2 = pile.depile()
            if calcul[i] == '+' :
                res = int(nb1) + int(nb2)
            if calcul[i] == '*' :
                res = int(nb1) * int(nb2)
            if calcul[i] == '-' :
                res = int(nb1) - int(nb2)
            pile.empile(res)
        else :
            pass
        i += 1
    return pile.depile()






p = Pile()
p.empile(7)
p.empile(1)
p.empile(3)
p.empile(9)
print(p)
tri_pile(p)
print(p)
    