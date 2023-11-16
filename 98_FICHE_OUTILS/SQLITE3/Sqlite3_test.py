import sqlite3

#Accès à la base 
var = sqlite3.connect("Chemin_vers_la_base.db")

# Création du curseur, variable qui permettra d'exécuter les requêtes
curseur = var.cursor()


## Création d'une table :
curseur.execute("CREATE TABLE Livre(titre VARCHAR(300), editeur VARCHAR(90) NOT NULL, annee INT, isbn CHAR(14) PRIMARY KEY)")


## Insertion dans une table :
curseur.execute("INSERT INTO Livre VALUES ('Manuel de NSI Terminale', 'Mr le prof',2023, '12345678910110'),('Manuel de NSI Première', 'Mr le prof',2023, '12345678910111'),('Manuel de SNT', 'Mr Dupond',2023, '12345678910112')")
### On oublie pas de valider les résultats lors de l'insertion.
var.commit()


## Selection d'élément
res = curseur.execute("Select * From Livre")
# Ici le résultat de la commande select sera stocké dans la variable res
# Le contenu de res est stocké dans un tableau de tuple :
print(res.fetchall())
"""
[('Manuel de NSI Terminale', 'Mr le prof', 2023, '12345678910110'),
('Manuel de NSI Première', 'Mr le prof', 2023, '12345678910111'),
('Manuel de SNT', 'Mr Dupond', 2023, '12345678910112')]
"""