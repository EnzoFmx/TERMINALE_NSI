# TD : SGBD

## Exercice 1 :

On souhaite modéliser un annuaire téléphonique simple dans le quel chaque personne (identifiée par un prénom et un nom) est associée à son numéro de téléphone. Proposer une modélisation relationnelle (un schéma relationnel) de cet annuaire. (N'oubliez pas la/les clé(s) primaire(s))

## Exercice 2 :

Donner la modélisation relationnelle d'un bulletin scolaire, on doit y trouver :

- Les élèves, avec un numéro étudiant alphanumérique unique.
- Un ensemble de matières unique
- Au plus une note par matière pour chaque étudiant

Proposer les trois schémas relationnel associés aux définition ci-dessus.

## Exercice 3 :

Modéliser les informations sur les département français. Chaque données doit contenir le nom du département, son code postal (Ex : 59 pour le nord, 2A ou 2B pour la corse). De plus nous aimerions représenter les département voisins sur une autre relation.

1. Ecrire ces deux schémas relationnel. 
2. Donner des exemples de données pour chaque table.

## Exercice 4 :

On considère deux relations R(<u>a</u> : int, b : int, c : int) et S(<u>#a : int, e : int</u>). l'attribut a de S est clé étrangère faisant référence à a de R.

Dire si les affirmations suivantes sont vraies ou fausses, en justifiant :

1. Les a de R sont tous deux à deux distincts.
2. Les b de R sont tous deux à deux distincts.
3. Les a de S sont tous deux à deux distincts.
4. Les e de S sont tous deux à deux distincts.
5. S peut être vide alors que R est non vide
6. R peut être vide alors que S est non vide