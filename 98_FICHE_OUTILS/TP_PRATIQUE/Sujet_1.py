def verif(tab):
    tab2=tab.copy()
    tab2.sort()
    if tab2==tab:
        return True
    else:
        return False
    
def verifie(tab):
    val = len(tab)
    if val == 1 :
        return True
    for w in range(val-1):
        if tab[w]>tab[w+1]:
            return False
    return True

def verifie2(tab):
    for i in range(len(tab)):
        el = tab[i]
        for x in tab[i+1:]:
            if el>x:
                return False
    return True

def verifie3(tab) :
    for i in range(len(tab)-1) :
        if tab[i] > tab[i+1] :
            return False
    return True




#ex2
def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale
