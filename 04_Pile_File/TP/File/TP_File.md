# TP File

------

## 1. Première implémentation

Pour cette implémentation, le constructeur de la classe utilisera un tableau pour stocker les données.

1. Créez cette classe File contenant les méthodes suivantes :

   * **enfile( )**

   * **defile( )**

   * **top( )**

   * **est_vide( )**

   * **taille( )**

## 2. File à taille fixe :

Supposons que notre file à une taille fixe, disons 7 éléments maximum. 

1. Ecrire une méthode ajout_element( ) qui ajoute un élément dans la file seulement si il n'y a pas trop d'éléments dans la file.
2. Ecrire une méthode vide_file( ) qui enlève tous les éléments de la file.

## 3.  Deuxième implémentation

Ici nous allons implémenter la file de manière récursive. Elle possèdera deux attributs, le premier sera un élément de la file nommé tête, le second sera une autre File. Cette seconde file possèdera elle aussi un élément et une autre file en attribut. Ainsi de suite.

1. Programmez cette classe nommée File2 avec les méthodes suivantes
   * **enfile( )**
   * **defile( )**
   * **top( )**
   * **est_vide( )**
   * **taille( )**

## 4. Implémentation d'un jeu de bataille :

La bataille : règles du jeu

Chacun tire la carte du dessus de son paquet et la pose sur la table. Celui qui a la carte la plus forte ramasse les autres cartes. L'as est la plus forte carte, puis roi, dame, valet, 10, etc. Lorsque deux joueurs posent en même temps deux cartes de même valeur il y a "bataille".

Lorsqu'il y a "bataille" les joueurs tirent la carte suivante et la posent, face cachée, sur la carte précédente. Puis ils tirent une deuxième carte qu'ils posent cette fois-ci face découverte et c'est cette dernière qui départagera les joueurs.

Lorsqu'il y a bataille et qu'un des deux joueur à moins de 3 cartes alors il a perdu

Le gagnant est celui qui remporte toutes les cartes. 

Le jeu de la bataille peut être facilement coder avec des Files. 

Un fichier carte.py contient la classe carte et les fonctions suivantes :

- comp
- game

- creer_jeu

1. Pour ce travail vous allez devoir compléter les fonctions :

   - tour 

   - bataille

   - jeu_fini

​	Ces fonctions se trouvent dans un fichier nommé carte_eleve.py

## Pour aller plus loin :

Ecrire une nouvelle implémentation d'une file, cette fois-ci il faut manipuler la file avec deux piles.