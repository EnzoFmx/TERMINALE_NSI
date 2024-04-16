def recherche(elt,tab):
    if elt not in tab:
        return None
    else:
        for n in range (len(tab)):
            if tab[n] == elt:
                return n
            
            
def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < len(tab)-1 and a > [i+1] : 
        tab_a[i] = tab_a[i+1] 
        tab_a[i+1] = a
        i = i+1 
    return tab_a