# Graphes TD

------

## Exercice 1 : Réseau social

Construire un graphe non orienté du réseau social à partir des informations suivantes :

- **Arthur** est ami avec **Benoit** et **Elodie** ;
- **Benoit** est ami avec **Arthur** et **Coralie** ;
- **Coralie** est ami avec **Benoit**, **Franck** et **David** ;
- **David** est ami avec **Coralie**, **Franck** et **Elodie** ;
- **Elodie** est ami avec **Arthur**, **David** et **Franck** ;
- **Franck** est ami avec **Coralie**, **David** et **Elodie**.

## Exercice 2 : Réseau routier

Eva décide de faire un graphe orienté représentant les différentes ruelles de son village. On y trouve une boulangerie, une école, un bureau de poste, une boucherie, une mairie, une église et une salle des fêtes. Certaines ruelles sont à double sens et d'autres à sens unique.

Eva décide de donner pour chacune des arêtes de son graphe une valeur qui correspond au temps qu'elle met pour traverser la ruelle à pied (chaque arête représente un sens de circulation).

Voici ses données :

- il y a une ruelle entre la boulangerie et le bureau de poste (double sens) - 2 minutes ;
- il y a une ruelle entre la boulangerie et l'école (sens unique de l'école vers la boulangerie) - 3 minutes ;
- il y a une ruelle entre la boulangerie et la boucherie (sens unique de la boulangerie vers la boucherie) - 4 minutes ;
- il y a une ruelle entre l'école et l'église (sens unique de l'école vers l'église) - 3 minutes ;
- il y a une ruelle entre l'école et la mairie (sens unique de la mairie vers l'école) - 4 minutes ;
- il y a une ruelle entre l'école et la salle des fêtes (double sens) - 6 minutes ;
- il y a une ruelle entre la boucherie et la salle des fêtes (double sens) - 5 minutes ;
- il y a une ruelle entre la mairie et l'église (double sens) - 7 minutes.

1. Dessiner le graphe représentant le village d'Eva.

2. Donner l'ordre du graphe ci dessus ainsi que le degré de chaque sommet.

3. Représenter par un dictionnaire le graphe ci dessus puis donner sa matrice d'adjacence.

## Exercice 3 : Grandes villes

Emmanuel veut faire un tour avec sa compagne sur chaque continent du monde : **Brasilia**, **San Francisco**, **Paris**, **Dakar**, **Pékin**, **Sydney**. Du fait de la distance entre ces grandes villes, nos 2 aventuriers n'ont d'autre choix que de prendre l'avion.

1. Dessiner un graphe non orienté représentant pour chaque sommet une ville citée dans le parcours d'Emmanuel et sa compagne. On supposera que toute les villes sont reliées entre elles par les voix aériennes.

2. Quel est ordre de ce graphe et que peut on dire des sommets ainsi que de la matrice d'adjacence du graphe ?

Après s'être concertés, nos 2 protagonistes décident d'ajouter à leur liste 2 villes supplémentaire : **Moscou** & **le Caire** malgré le fait que pour aller à **Moscou**, on ne peut y accéder que en partant de **Paris** et aussi malgré le fait que pour aller du **Caire**, on ne peut passer que par **Dakar**.

3. Que peut on dire des sommets correspondant à Paris et Dakar ?

Après sa journée de travail, Emmanuel va voir dans une agence de voyage les trajets possibles par rapport aux villes citées plus haut et voici ce qu'il trouve :

- De **Brasilia**, nous pouvons prendre l'avion et aller jusque **Paris** (6 heures) et **San Francisco** (5 heures) ;
- De **San Francisco**, nous pouvons prendre l'avion et aller jusque **Pékin** (3 heures), **Paris** (4 heures) et **Sydney** (3 heures) ;
- De **Pékin**, nous pouvons prendre l'avion et aller jusque **Dakar** (7 heures), **Sydney** (3 heures) ;
- De **Dakar**, nous pouvons prendre l'avion et aller jusque **Paris** (2 heures) et **le Caire** (1 heure) ;
- De **Paris**, nous pouvons prendre l'avion et aller jusque **Dakar** (2 heures), **Moscou** (5 heures) et **Brasilia** (6 heures) ;
- De **Sydney**, nous pouvons prendre l'avion et aller jusque **San Francisco** (3 heures) et **Dakar** (3 heures) ;
- De **Moscou**, nous pouvons prendre l'avion et retourner sur **Paris** (5 heures) ;
- Du **Caire**, nous pouvons prendre l'avion et retourner sur **Dakar** (1 heure).

4. Dessiner le graphe orienté selon les informations données.

5.  Donner l'ordre du graphe et donner dans un tableau tous les degrés entrants et sortants de tous les sommets du graphe.

6. Donner la matrice d'adjacence du graphe. 