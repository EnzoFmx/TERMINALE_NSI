def correspond(mot, mot_trous) :
    if len(mot_trous) != len(mot) :
        return False
    for i in range(len(mot_trous)) :
        if mot_trous[i] != '*' :
            if mot[i] != mot_trous[i] :
                return False
    return True

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur] 
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires += 1

    return nb_destinataires == len(plan)