import random

import random

def jeu():
    print('Bienvenue au jeu du pierre feuille ciseau')
    t = ["Pierre","Feuille","Ciseau"]
    m_gagnée = 0
    manches = 0
    while manches < 3 :
        choix = input('Choissisez entre "Pierre", "Feuille", "Ciseau"')
        while choix not in t :
            choix = input('Choissisez entre "Pierre", "Feuille", "Ciseau" (Sans fautes !!!)')
        choix2 = random.randint(0,2)
        if t.index(choix) == choix2 :
            print("Egalité, l'ordinateur a choisi "+t[choix2])
        elif t.index(choix) == (choix2-1) or (choix == 'Ciseau' and choix2 == 0) :
            print("Manche perdue, l'ordinateur a choisi "+t[choix2])
        else : 
            print("Manche gagnée, l'ordinateur a choisi "+t[choix2])
            m_gagnée = m_gagnée + 1
        manches = manches + 1
    if m_gagnée < 2 :
        print('Vous avez perdu')
    else : 
        print('Vous avez gagné')