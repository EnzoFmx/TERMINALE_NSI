# 1
def motif(cle,mot):
    tab=[]
    for i in range(len(mot)):
        ind2 = 0
        i2 = i
        if mot[i2] == cle[ind2]:
            while ind2 < len(cle) and mot[i2] == cle[ind2] :
                ind2+=1
                i2+=1
            if ind2 >= len(cle) :
                tab.append(i)
    return tab
    



# 2

def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc: 
        acc.append(x)
        for y in adj[x]: 
            parcours(adj, y, acc) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc) 
    return acc
