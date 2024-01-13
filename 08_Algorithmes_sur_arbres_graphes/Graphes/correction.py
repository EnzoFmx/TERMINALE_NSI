def parcours_profondeur(graphe,depart,deja_visite) :
    """
    Fonction permettant de faire le parcours en profondeur d'un graphe
    en partant de depart. La variable deja_visite permet de stocker les sommets déjà visités
    et ainsi éviter les appels réccursifs (infinis). 
    La valeur de retour est None, mais les sommets parcourus sont affichés
    """ 
    print(depart, end='')
    deja_visite.add(depart)
    for voisin in graphe[depart] :
        if voisin not in deja_visite :
            parcours_profondeur(graphe,voisin,deja_visite)


def parcours_largeur(graphe,depart) :
    """
    Fonction permettant de faire le parcours en largeur d'un graphe
    en partant de depart.
    La valeur de retour est None, mais les sommets parcourus sont affichés.
    """
    f = File()
    f.enfile(depart)
    ensemble = set()
    while f.est_vide() == False: 
        n = f.defile()
        if n not in ensemble :
            print(n, end='')
            ensemble.add(n)
            for voisin in graphe[n] :
                if voisin not in ensemble :
                    f.enfile(voisin)

def presence_cycle_graphe(graphe,depart,deja_visite=set()) :
    """
    Permet de savoir si un cycle est présent dans un graphe.
    """
    deja_visite.add(depart)
    for voisin in graphe[depart] :
        if voisin in deja_visite :
            return True
        else :
            presence_cycle_graphe(graphe,voisin,deja_visite)
    return False

def plus_court_chemin(graphe, depart, arrive) :
    """
    Algorithme permettant de retrouver le plus court chemin entre deux sommets d'un graphe
    return : (list) vide si pas de chemin, sinon contient les sommets parcourus.
    """
    f = File()
    f.enfile(depart,[depart])
    ensemble = set()
    while f.est_vide() == False: 
        noeud,chemin = f.defile()
        """ Même chose détaillée :
        tupl = f.defile
        noeud = tupl[0]
        chemin = tupl[0]
        """
        if noeud not in ensemble :
            ensemble.add(n)
            for voisin in graphe[n] :
                if voisin not in ensemble :
                    copie = chemin.copy()
                    copie.append(voisin)
                    f.enfile((voisin,copie))
                    if voisin == arrive :
                        return copie
    return []