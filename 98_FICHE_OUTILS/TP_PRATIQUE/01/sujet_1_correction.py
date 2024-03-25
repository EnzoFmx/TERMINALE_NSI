def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = (tab[i], tab[j]) 
    tab[i] = temp[1] 
    tab[j] = temp[0]

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N): 
        imin = k 
        for i in range(k, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin)
        
def taille(abre,somm):
    if somm not in abre.keys():
        return False
    else:
        if abre[somm]==['','']:
            return 1
        elif abre[somm][0]=='':
            return 1+taille(abre,abre[somm][1])
        elif abre[somm][1]=='':
            return 1+taille(abre,abre[somm][0])
        else:
            return 1+taille(abre,abre[somm][1])+taille(abre,abre[somm][0])
        
def taille(abre,somm):
    if somm == '' :
        return 0
    else :
        return 1+taille(abre,abre[somm][1])+taille(abre,abre[somm][0])
        
            