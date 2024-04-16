def insertion_abr(a, cle):
    if a == None:
        return (None, cle, None)
    elif a[1] == cle :
        return a
    elif a[1] >= cle :
        return (insertion_abr(a[0], cle), a[1], a[2])
    else :
        return (a[0], a[1],insertion_abr(a[2], cle))

n0 = (None, 0 ,None)

def empaqueter(liste_masses, c):
    """Renvoie le nombre minimal de boîtes nécessaires pour
    empaqueter les objets de la liste liste_masses, sachant
    que chaque boîte peut contenir au maximum c kilogrammes"""
    n = len(liste_masses)
    nb_boites = 0
    boites = [ 0 for _ in range(n) ]
    for masse in liste_masses: 
        i = 0
        while i < nb_boites and boites[i] + masse > c: 
            i = i + 1
        if i == nb_boites:
            nb_boites += 1
        boites[i] = masse + boites[i] 
    return nb_boites 