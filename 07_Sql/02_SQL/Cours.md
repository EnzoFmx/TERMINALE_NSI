# Manipuler des bases de données avec le langage SQL :

------

Nous avons vu dans le chapitre précédent les SGBD (système de gestion de base de données), ces logiciels permettent de manipuler des bases. Nous voyons dans ce cours des bases de données dites relationnelle, la majorité des SGBD relationnel utilisent le langage **SQL**.

Le SQL (Structured Query Language) permet d'envoyer des ordres au SGBD. On peut notamment créer des relations (tables), ajouter des lignes (n-uplet), en supprimer, sélectionner des lignes avec certains critères, etc.

## 1. Création de table

La création d'une table en SQL reprend le schéma relationnel vu dans le chapitre précédent.

Exemple :

```sql
# Exemple 1 :
CREATE TABLE Livre(titre VARCHAR(300), editeur VARCHAR(90) NOT NULL, annee INT, isbn CHAR(14) PRIMARY KEY)

CREATE TABLE Auteur(a_id INT PRIMARY KEY,
                   nom VARCHAR(90),
                   prenom VARCHAR(90))

CREATE TABLE Auteur_de(a_id INT REFERENCES Auteur(a_id), isbn CHAR(14) REFERENCES Livre(isbn), PRIMARY KEY(a_id, isbn))
```

 On voit avec cet exemple plusieurs choses :

- "CREATE TABLE nom_table" permet de créer une table qui aura comme nom *nom_table*
- Une clé primaire est définie après l'attribut (la colonne) par PRIMARY KEY
- Une clé étrangère est définie après l'attribut par REFERENCES suivit de la table contenant **initialement** l'attribut
- On défini un couple de clés primaires par PRIMARY KEY(attribut1, attribut2, etc.)
- NOT NULL permet de forcer l'existence de l'attribut sans qu'il soit clé primaire pour autant

**Suppression de table :  DROP TABLE nom_table ;**

 ## 2. Type des attributs

| Nom        | Description                                 |
| ---------- | ------------------------------------------- |
| INTEGER    | Entier 32 bits signé                        |
| INT        | Idem qu'INTEGER                             |
| REAL       | Nombre réel sur 32 bits                     |
| CHAR(n)    | Chaîne d'exactement n caractères            |
| VARCHAR(n) | Chaîne d'au plus n caractères               |
| TEXT       | Chaîne de taille quelconque                 |
| DATE       | Date au format 'AAAA-MM-JJ'                 |
| TIME       | heure au format 'hh:mm:ss'                  |
| TIMESTAMP  | Date et heure combiné "AAAA-MM-JJ hh:mm:ss" |

## 3. Insertion d'éléments 

L'insertion en SQL se fait de la manière suivante :

```sql
INSERT INTO Livre VALUES ('Manuel de NSI Terminale', 'Mr le prof',2023, '12345678910110'),('Manuel de NSI Première', 'Mr le prof',2023, '12345678910111'),('Manuel de SNT', 'Mr Dupond',2023, '12345678910112')

# Ou alors :

INSERT INTO Livre (titre , editeur , annee , isbn) VALUES ('Manuel de NSI Terminale', 'Mr le prof',2023, '12345678910110')
```

## 4. Sélection d'éléments

La sélection d'éléments se fait de manière très simple en SQL. 

```sql
Select colonne1, colonne2 FROM table
```

Ici on sélectionne la *colonne1* et la *colonne2* depuis la base appelée *table*

<u>Afin de sélectionner toutes les colonnes d'une table :</u>

```
Select * FROM Table
```

## 5. Conditions sur la sélection d'éléments

Reprenons la table Livre du dessus, si nous voulons par exemple sélectionner les livre écrits par 'Mr le prof' il est possible de :

```sql
select * From Livre where editeur = 'Mr le prof'
```

Le mot clé **Where** permet ici de sélectionner seulement les lignes où l'éditeur vaut *'Mr le prof'* et aucune autre.

Il est possible de faire des **expression booléennes** avec les conditions, concrètement :

```sql
select * From Livre where editeur = 'Mr le prof' and annee > 2
```

On sélectionne ici toutes les colonnes de la table Livre ou l'éditeur est 'Mr le prof' et l'année de sortie est > 2.

## 6. Sélectionner des données sur deux tables :

Il est possible de sélectionner des lignes sur deux tables différentes à la fois. Il faut pour cela utiliser le mot clé **JOIN**, qui permettra de combiner les tables selon un critère que l'on définira.

<u>Prenons un exemple :</u> 

```sql
/* Nous avons notre table Livre(titre,editeur,annee,isbn,auteur_id)
Imaginons une table Auteur(nom,prenom,auteur_id) */

/* On remarque ici que les deux tables ont (par pur hasard) un attribut qui serait le même (il l'est), il est donc possible de créer des lignes combinant le livre suivit des informations de son auteur */

select titre,nom,editeur,annee,prenom,auteur_id,annee from Livre join Auteur on Auteur.auteur_id = Livre.auteur_id

/* Il est possible de faire des conditions sur les lignes,d'afficher toutes les colonnes avec '*', de compléxifier etc...*/

select titre,nom,editeur,annee,prenom,auteur_id,annee from Livre join Auteur on Auteur.auteur_id = Livre.auteur_id where titre = 'Manuel de NSI Terminale'


```

On applique ici le mot clé JOIN à deux tables, puis on explicite ou est le lien entre les deux tables, ici comme les deux tables ont une colonne identique (on peut imaginer qu'il y ait une clé étrangère par exemple), on agit donc sur cette colonne afin de lier ces tables.

## 7. Modifier des données de la table :

Afin de modifier des données dans la table il faut utiliser le mot clé **UPDATE** table **SET**

<u>Exemple :</u>

```sql
/* Permet de modifier l'éditeur 'Mr le prof' en 'Mr le prof Frémeaux' */
UPDATE Livre SET editeur = 'Mr le Prof Frémeaux' where editeur =  'Mr le prof'

/* Il est possible de modifier plusieurs colonnes en ajoutant des virgules */
UPDATE Livre SET editeur = 'Mr le Prof Frémeaux', titre = 'Nouveau titre' where editeur =  'Mr le prof'
```

## 8. Supprimer des valeurs :

Afin de supprimer des valeurs il faut utiliser le mot clé **DELETE**

<u>Exemple :</u>

```sql
/* Ici je supprime les livre écrit par 'Mr le prof' */
DELETE FROM Livre WHERE editeur = 'Mr le prof'

/* Supprimer toutes les données de livre*/
DELETE FROM LIVRE
```

## 9. Mots clés supplémentaire

Le mot clé DISTINCT permet d'afficher les élément d'une colonne seulement une fois.

```sql
/* Ici on affichera seulement une fois chaque donnée, si 'Mr le prof' a édité deux livres, alors cette valeur n'apparaîtra qu'une fois */
select DISTINCT editeur From Livre 
```

Le mot clé ORDER BY permet de classer les résultats par ordre (croissant / décroissant)

```sql
/* Ici on affichera toutes les lignes, seulement elles seront triées par leur isbn */
Select * From livre Order by isbn
```

