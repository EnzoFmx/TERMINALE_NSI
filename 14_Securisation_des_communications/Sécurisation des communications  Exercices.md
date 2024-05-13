# Sécurisation des communications : Exercices

## 1. Attaque de l'homme du milieu :

A l'aide d'internet expliquer "L'attaque de l'homme du milieu".

## 2. Codage :

### Partie 1 : 

Pour cette partie considerer l'Alphabet suivant : 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

1. Ecrire une fonction `cesar(message : str, cle : int) => str` permettant de chiffré un message à l'aide du chiffrement de césar. 
2. Ecrire une fonction `vigenere(message :str, cle : tab) => str` appliquant le chiffrement de vignenère à un message.
   - Le fonctionnement de ce chiffrement est le suivant : Un tableau possède des entier utilisés comme clés pour chiffrer un message. 
   - Exemple : 'TEST' comme message et [1,2] comme clé => 'UGTV' 

### Partie 2 :

1. Ecrire la fonction `chiffrement_xor(message : str, cle : str) => list` appliquant le chiffrement XOR vu dans le cours.
   - Le message chiffré se retrouve dans un tableau, chaque élément du tableau contient le code de chaque caractère chiffré.

## Partie 3 :

Dans cette partie nous allons déchiffrer le chiffrement de césar :

1. Ecrire une fonction `déchiffrement_cesar(message : str, cle : int) => str` permettant de déchiffrer un message à l'aide de la clé de chiffrement `cle` 

La fonction précédente permet de dechiffrer un message en **connaissant** la clé, mais pour l'heure nous ne savons pas comment la retrouver. 

Il est possible de retrouver (pas à tout les coups) le message initial en utilisant les occurences de chaque lettres. En effet dans la langue française, la lettre la plus présente est la lettre 'E', en retrouvant le caractère le plus présent dans le message codé on peut supposer que ce caractère chiffré correspond à la lettre E. 

2. Ecrire une fonction `lettre_plus_represente(message : str) => str`permettant de renvoyer la lettre la plus présente dans le message.
3. Ecrire la suite du raisonnement en instruction python permettant de retrouver le message initial à partir d'un message chiffré.

 