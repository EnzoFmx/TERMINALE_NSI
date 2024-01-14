def recherche(t,v,d,f):
    """Fonction récursive de recherche
    param t (tableau) : tableau dans lequel on recherche l'élément
    param v ( ) : valeur à rechercher
    param d (int) : indice de début de recherche dans le tableau
    param f (int) : indice de fin de recherche dans le tableau
    return (None/ ) : None si pas trouvé, position de v dans t sinon"""
    if d > f :
        return None
    milieu = (d+f)//2
    if t[milieu] < v :
        return recherche(t,v,milieu+1,f)
    elif t[milieu] > v :
        return recherche(t,v,d,milieu-1)
    else :
        return milieu
    
def recherche_dichotomique(t,v):
    """Algo de recherche dichotomique, renvoie None si pas trouvé, position de v dans t sinon,
    le tableau t est trié, v est la valeur à rechercher dans le tableau"""
    return recherche(t,v,0,len(t)-1)   