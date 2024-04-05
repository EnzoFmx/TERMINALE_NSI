def recherche(elt,tab):
    occurence = None
    for i in range(len(tab)):
        if tab[i] == elt:
            occurence = i  
    
    
    return occurence

class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères 
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = ["0","255"] 
        return self.liste_octets()[3] in reservees

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = self.liste_octets()[3]
        if octets == 254: 
            return None
        octet_nouveau = octets + 1 
        return AdresseIP('192.168.0.' + str(octet_nouveau)) 



















