def parcours_largeur(a):
    file = File()
    file.enfile(a)
    while file.est_vide() == False :
        enfant = file.defile()
        print(enfant.valeur)
        if enfant.fils_gauche != None :
            file.enfile(enfant.fils_gauche)
        if enfant.fils_droite != None :
            file.enfile(enfant.fils_droite)
        
    
def parcours_prefixe(a):
    print(a.valeur,end='')
    if a.fils_gauche != None :
        parcours_prefixe(a.fils_gauche)
    if a.fils_droite != None :
        parcours_prefixe(a.fils_droite)
        
def parcours_infixe(a):
    if a.fils_gauche != None :
        parcours_prefixe(a.fils_gauche)
    print(a.valeur,end='')
    if a.fils_droite != None :
        parcours_prefixe(a.fils_droite)

def parcours_postfixe(a):
    if a.fils_gauche != None :
        parcours_prefixe(a.fils_gauche)
    if a.fils_droite != None :
        parcours_prefixe(a.fils_droite)
    print(a.valeur,end='')