def plus_grand_que(a,b) :
    """
    Fonction permettant de savoir quelle valeur entre a et b est la plus grande
    param a : (int/float/str) element à comparer
    param b : (int/float/str) element à comparer
    CU : Les deux paramètres doivent être de même type
    return : (int/float/str) Element le plus grand
    """
    if a > b :
        return a
    elif a == b :
        return a
    else :
        return b

def pythagore(cote1,cote2,hypothenuse) :
    """
    Fonction qui determine sur un triangle de coté : cote1,cote2,hypothenuse est
    rectangle
    param cote1 : (int) cote 1 du triangle
    param cote2 : (int) cote 2 du triangle
    param hypothenuse : (int) cote le plus grand des 3
    return : (bool) renvoie True si le triangle est rectangle, False sinon
    """
    res = False
    if cote1**2 + cote2**2 == hypothenuse**2 :
        res = True
    return res

def somme(t):
    """Fonction qui fait la somme de tout les éléments du tableau
    param t : (tableau) Tableau contenant les éléments
    return (int/float) Somme de tous les éléments"""
    s = 0
    for i in t :
        s = s + i
    return s

def somme2(t):
    """Fonction qui fait la somme de tout les éléments du tableau
    param t : (tableau) Tableau contenant les éléments
    return (int/float) Somme de tous les éléments"""
    addition = 0
    for i in range(len(t)) :
        addition += t[i]
    return addition

def somme3(t) :
    """Fonction qui fait la somme de tout les éléments du tableau
    param t : (tableau) Tableau contenant les éléments
    return (int/float) Somme de tous les éléments"""
    addition = 0
    ind = 0
    while ind <len(t)-1:
        addition += t[ind]
        ind += 1
    return addition


def recherche_dichotomique(t, v):
    """
    Fonction qui applique la recherche dichotomique dans un tableau
    param tableau : Tableau où l'on va rechercher une valeur
    param valeur : valeur à retrouver
    return : Renvoie l'indice de la position de val, -1 si val n'est pas dans le tableau
    """
    debut = 0
    fin = len(t)-1
    while debut <= fin :
        milieu = (debut + fin) // 2
        if t[milieu] > v :
            fin = milieu - 1
        elif t[milieu] < v :
            debut = milieu + 1
        elif t[milieu] == v :
            return milieu
    return -1

def dentiste(texte):
    voyelles = ['a','e','i','o','u','y']
    resultat = ''
    for lettre in texte :
        if lettre in voyelles :
            resultat.append(lettre)
    return resultat