# Circuits intégrés

------

# 1. Rappel première

## 1. 1. Composition d'un ordinateur 

Nous avons vu en première l'évolution de l'architecture d'un ordinateur a abouti à une architecture de Von Neumann. 

Cette architecture possède les composants suivant :

- Mémoire 
  - Dites 'dure' (Disque dur, SSD)
  - RAM
- Processeur
- GPU (Carte graphique) (optionnel)
- Périphériques d'entrée 
  - Souris / Clavier
- Périphériques de sortie
  - Ecran / Son

Tout ces composants sont reliés par des 'bus' (dans le cas d'un ordinateur il s'agit de câbles).

## 1. 2. Evolution de la taille des ordinateurs

- Le premier ordinateur sous l'architecture Von Neumann était l'ENIAC en 1945 et faisait seulement 167m². 

![ENIAC](../Images/Eniac.jpg)Image : Wikipédia

- En 1980 l'IBM PC 5150, un peu plus petit.

 ![IBM PC 5150](../Images/IBMPC5150.jpg) Image : Wikipédia

De nos jours nous utilisons des ordinateurs portables qui sont donc encore plus petit.

## 1. 3. Evolution de la puissance des ordinateurs : 

**Loi de Moore :**

*Gordon E. Moore fut l’un des trois fondateur d’intel (célèbre entreprise d’informatique, encore aujourd’hui)*

La loi de Moore fut établie en 1965. Cette loi a permit d’établir la règle suivante :

- **A coût égal, le nombre de transistor d’un microprocesseur doublera tout les deux ans et ce jusqu’en 2015. (Règle finale en 1975)**

**Pourquoi 2015 ? :**

- Car la miniaturisation des transistors est limitée par la taille des atomes. En effet après 2015 les scientifiques visaient une taille de 2 nanomètres par transistor (soit 10 atomes) qui en 2018 n’était toujours pas atteinte.

A ce jours l’un des derniers processeur en date chez Intel est l’Intel core i9-12900K possédant une puce pouvant traiter des données de 64 bits avec des transistors ayant une taille de 10 nanomètres. Le processeur possède 16 coeurs phyisque (Donc peut effectué 16 opérations simultanées), contre 1 cœur pour l’Intel 4004.

## 2. Circuits intégrés : 

L'évolution des ordinateurs confirme deux points :

- La taille de l'architecture est vouée à être réduite
- La puissance de cette architecture augmente

Afin de satisfaire au mieux le premier point (la taille) des concepteurs se sont concentrés sur la conception d'une carte contenant tous les composant d'un ordinateur sur un seul circuit. C'est ce que l'on appelle un circuit intégrés ou en anglais **S**ystem **o**n **C**hip (**SoC**).

Cette carte contient donc de nombreux composant d'ordinateur, comme le processeur, la mémoire, le GPU (partie graphique), carte son/réseau, etc...

L'architecture ARM se retrouve dans les smartphones notamment, c'est la plus répandue. 

La miniaturisation des circuits a permit quelques améliorations face à une architecture traditionnelle :

- Gain de place
- Consomment moins d'énergie

Cependant, ces circuits sont figés, ils ne peuvent être amélioré, ils font donc face à une obsolescence forcée. Le recyclage de ces cartes est en développement mais peine encore à être efficace.

![image-20220802110716929](../Images/raspberryPI.png)*Image d'une Raspberry PI (Wikipédia)*

