def recherche_dichotomique(t, v):
    debut = 0
    fin = len(t)-1
    while debut <= fin :
        milieu = (debut + fin) // 2
        if t[milieu] == v :
            return True 
        else:
            if t[milieu] > v :
                fin = milieu - 1
            else :
                debut = milieu + 1
    return False

def recherche_recur(t,v):
    if len(t) == 1:
        return t[0] == v
    else :
        milieu = len(t)//2
        if t[milieu] > v :
            return recherche_recur(t[:milieu],v)
        else :
            return recherche_recur(t[milieu:],v)