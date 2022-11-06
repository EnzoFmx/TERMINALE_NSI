# Programmation itérative :

# 1.
def maximum(t : list) :
    if len(t)==0:
        return 'Tableau vide'
    else :
        maxi = t[0]
        for elem in t :
            if elem > t :
                maxi = elem
        return elem
    
# 2.
for i in range(6):
    print(i)
    
ind1 = 0
while ind1 < 6 :
    print(ind1)
    ind1+=1
# 3.
s = "J'adore la NSI"
for i in s :
    print(i)

ind2 = 0
while ind2<len(s):
    print(s[ind2])
    ind2+=1

# 2. Manipulation de tableaux

# 1.
t = [0,1,2,3]
print(t[0])

# 2.
t = ['N','S','I','Y','O','U','P','I']
print(t[3:])

# 3. Programmation récursive

# 1. Permet de programmer en réutilisant la fonction en valeur de retour

# 2. Il s'agit du cas d'arrêt

# 3.

def nb_chiffre(n) :
    if n <= 9 :
        return 1 
    else : 
        return 1 + nb_chiffre(n//10)


# 4.

def dentiste(texte) :
    voyelles = ["a","e","i","o","u","y"]
    if len(texte) == 1 :
        if texte[0] in voyelles :
            return texte[0]
    else :
        if texte[0] in voyelles :
            return texte[0] + dentiste(texte[1:])
        else :
            return dentiste(texte[1:])