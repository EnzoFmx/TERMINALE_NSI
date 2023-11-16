# Module Sqlite (python)

Le module sqlite permet d'agir sur des bases de données via python.

Documentation officielle : https://docs.python.org/3/library/sqlite3.html

```python
import sqlite3

#Accès à la base 
var = sqlite3.connect("Chemin_vers_la_base.db")

# Création du curseur, variable qui permettra d'exécuter les requêtes
curseur = var.cursor()

# Execution d'une requête
curseur.execute("Ma requête en SQL")

## Création d'une table :
curseur.execute("CREATE TABLE Livre(titre VARCHAR(300), editeur VARCHAR(90) NOT NULL, annee INT, isbn CHAR(14) PRIMARY KEY)")

## Insertion dans une table :
```

## Connexion à la base :

Afin de se connecter à la base de données il faut créer une variable permettant d'agir sur cette connexion :

```python
import sqlite3

#Connexion à la base 
var = sqlite3.connect("Chemin_vers_la_base.db")
```

## Requêtes dans la base :

Pour faire des requêtes dans la base il faut créer un curseur, c'est à partir de ce curseur que l'on créer les requêtes SQL.

```python
# Création du curseur, variable qui permettra d'exécuter les requêtes
curseur = var.cursor()

# Execution d'une requête
curseur.execute("Ma requête en SQL")
```

Ici on crée le curseur grâce à la méthode *cursor( )*, l'exécution de requête ce fait avec *execute( )*

### Création de table :

La création de table se fait donc grâce à *execute( )*

```python
curseur.execute("CREATE TABLE Livre(titre VARCHAR(300), editeur VARCHAR(90) NOT NULL, annee INT, isbn CHAR(14) PRIMARY KEY)")
```

Il faut cependant faire attention, cette requête ne doit pas s'exécuter à chaque fois que l'on souhaite tester son code.

- Il faut soit mettre cette instruction dans une fonction, que l'on peut appeler quand on le souhaite
- Mettre en commentaire cette instruction une fois la table créée

### Insertion d'élément

Afin d'insérer un élément, rien de plus simple on utilise encore *execute( )*

```python
curseur.execute("INSERT INTO Livre VALUES ('Manuel de NSI Terminale', 'Mr le prof',2023, '12345678910110'),('Manuel de NSI Première', 'Mr le prof',2023, '12345678910111'),('Manuel de SNT', 'Mr Dupond',2023, '12345678910112')")
```

Cependant il faut rajouter une instruction :

```python
var.commit()
```

Cette instruction permet de valider l'insertion dans la table.

### Sélection d'élément

La sélection d'élément se fait aussi avec *execut( )*

```python
## Selection d'élément
res = curseur.execute("Select * From Livre")
# Ici le résultat de la commande select sera stocké dans la variable res
# Le contenu de res est stocké dans un tableau de tuple :
>>> print(res.fetchall())
[('Manuel de NSI Terminale', 'Mr le prof', 2023, '12345678910110'),
('Manuel de NSI Première', 'Mr le prof', 2023, '12345678910111'),
('Manuel de SNT', 'Mr Dupond', 2023, '12345678910112')]
```

**La méthode *fetchall( )* permet ici de récupérer les résultats et de les convertir en tableau de tuples.**

