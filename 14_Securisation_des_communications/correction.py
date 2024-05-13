def cesar(message : str, cle : int) :
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultat = ''
    for lettre in message :
        resultat += alphabet[alphabet.index(lettre)+cle%26]
    return resultat

def cesar2(message, cle):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultat = ''
    for lettre in message
        # Position de la lettre
        for i in range(alphabet):
            if alphabet[i] == lettre :
                position_lettre = i
        # Ajout de la cle à la position
        position_lettre += cle
        # Passage à une valeur inférieure à 26 pour être dans l'alphabet
        while position_lettre >= 25 :
            position_lettre -= 26
        # Ajout la nouvelle lettre dans résultat
        resultat = resultat + alphabet[position_lettre]
    return resultat

# même chose mais en une ligne :
def cesar2(msg,cle,alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    return ''.join([alphabet[alphabet.index(i)+cle%26] for i in msg])


# Vigenere en 1 ligne :
def vigenere(message,cle,alphabet= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    return ''.join(cesar2(message[i],cle[i%len(cle)],alphabet) for i in range(len(message)))

