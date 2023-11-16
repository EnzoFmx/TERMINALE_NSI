from File import *
import random
   
VAL_CARTE = ['2','3','4','5','6','7','8','9','10','V','D','R','AS']
COL_CARTE = ['P','T','C','H']

def in_file(x,f):
    """
    Fonction qui revoie True si x est dans la file f
    param x (): element present ou non dans f
    param f (File1/File2) : File contenant ou non x
    return (bool) : Renvoie True si x est dans f, False sinon
    """
    if type(f) == File1 :
        if x in f.file :
            return True
        else :
            return False
    elif type(f) == File2 :
        if f.tete == x :
            return True
        elif f.queue != None :
            return in_file(x,f.queue)
        else :
            return False
    else :
        return False
        
def comp(c1,c2) :
    """
    Fonction de comparaison entre deux cartes
    param c1 : (tuple) Carte 1
    param c2 : (tuple) Carte 2
    return : Renvoie
                    -1 si => c1 < c2
                    1  si => c1 > <2
                    0  si => c1 == c2
    
    """
    if VAL_CARTE.index(c1[0]) < VAL_CARTE.index(c2[0]) :
        return -1
    elif VAL_CARTE.index(c1[0]) > VAL_CARTE.index(c2[0]) :
        return 1
    else :
        return 0
                    
def creer_jeu():
    """
    Fonction qui crée un jeu aléatoire
    return a,b (File) Deux files contenant 26 cartes chacunes
    """
    i = 0
    val_carte = ['2','3','4','5','6','7','8','9','10','V','D','R','AS']
    col_carte = ['P','T','C','H']
    f1 = File1()
    f2 = File1()
    while i < 52 :
        val = random.randint(0,len(val_carte)-1)
        col = random.randint(0,len(col_carte)-1)
        carte = (val_carte[val],col_carte[col])
        if in_file(carte,f1) == False and in_file(carte,f2) == False  :
            if i%2 == 0 :
                f1.enfile(carte)
            else :
                f2.enfile(carte)
            i+=1
    return f1,f2
            
def tour(f1,f2) :
    """
    Foncton qui simule un tour de bataille
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    """
    i = f1.defile()
    j = f2.defile()
    res = comp(i,j)
    if res == 1 :
        f1.enfile(i)
        f1.enfile(j)
    elif res == -1 :
        f2.enfile(i)
        f2.enfile(j)
    else :
        print('bataille')
        if bataille_possible() :
            bataille(i,j,f1,f2)
            
def bataille(c1,c2,f1,f2) :
    """
    Fonction simulant un tour de bataille
    param c1 : (tuple) Carte n°1 égale a c2
    param c2 : (tuple) Carte n°1 égale a c1
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2    
    """
    bataille_tab= []
    bataille_tab.append(c1)
    bataille_tab.append(c2)
    while comp(c1,c2) == 0 and bataille_possible() :
        """
        bataille_tab += [f1.defile()]"""
        bataille_tab.append(f1.defile())
        bataille_tab.append(f2.defile())
        c1 = f1.defile()
        c2 = f2.defile()
        bataille_tab += [c1,c2]
    if comp(c1,c2) == 1 :
        """
        for i in range(len(bataille_tab)) :
            f1.enfile(bataille_tab[i])"""
        for i in bataille_tab :
            f1.enfile(i) 
    elif comp(c1,c2) == -1 :
        for i in bataille_tab :
            f2.enfile(i)
        
        
        
def est_fini(f1,f2):
    """
    Fonction qui détermine si le jeu est fini
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    return (bool): renvoie True si le jeu est fini, False sinon.
    """
    if f1.taille() == 0 :
        print("J1 a perdu")
        return True
    elif f2.taille() == 0 :
        print("J2 a perdu")
        return True
    else :
        return False
    
def bataille_possible(f1,f2):
    """
    Fonction permettant de faire finir le jeu
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    """
    res = True
    if f2.taille() < 2 :
        while f2.est_vide() == False :
            f2.defile()
            res = False
    elif f1.taille() < 2  :
        while f1.est_vide() == False :
            f1.defile()
            res = False
    return res
    
    
def game(f1,f2):
    """
    Fonction simulant le jeu de la bataille
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    """
    while not est_fini(f1,f2) :
        tour(f1,f2)