def v_e(adj ,x):
    result = []
    for i in range(len(adj)):
        if x in adj[i]:
            result.append(i)

    return result
            
                   





def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1,len(s)): 
        if s[i] == chiffre:
            compte = compte + 1 
        else:
            resultat += str(compte) + chiffre 
            chiffre = s[i] 
            ...
    lecture_... = ... + ... 
    resultat += lecture_chiffre
    return resultat