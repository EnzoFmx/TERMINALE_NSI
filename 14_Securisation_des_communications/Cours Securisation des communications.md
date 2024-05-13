# Cours : Sécurisation des communications

Pour établir une communication il faut au minimum deux entités. Ces deux entités une fois identifiées échangent des informations. 

La sécurisation de ces communications est essentielle en informatique, celle-ci permet de ne pas partager certaines données personnelles. Pour sécuriser ces communications les données sont cryptées. Ces données cryptées permettent :

- De chiffrer les messages (illisible pour quiconque n'a pas le moyen de déchiffrer)
- De s'assurer de l'expéditeur

Il existe deux types de chiffrement :

- Le chiffrement **symétrique** : Une clé est utilisé pour chiffrer et déchiffrer un même message.
- Le chiffrement **asymétrique** : Chaque utilisateur possède deux clés. Une publique, une privée, la première permet de chiffrer un message et est disponible pour tous. La seconde clé (privée) est l'unique clé permettant de déchiffrer les données chiffrées par la clé publique, cette clé privée est uniquement à la disposition de l'utilisateur.

## 1. Chiffrement symétrique :

### <u>César</u> :

Le chiffrement de césar (très trivial) permet de chiffrer un message en décalant les caractères d'un texte d'une même valeur. 

Par exemple : 

VIVE LA NSI => WJWF MB OTJ (Décalage d'un caractère => Clé égale à 1)

*Evidemment cet algorithme n'est pas utilisé, il est utile pour comprendre le principe de chiffrement*

### <u>XOR</u> :

Ce chiffrement utilise l'opérateur XOR sur le message à chiffrer à l'aide d'une clé (en chaine de caractère) en utilisant le code associé à chaque caractères.

Ex : 

```python
codage_xor('Je suis une phrase','nsi')
[36, 22, 73, 29, 6, 0, 29, 83, 28, 0, 22, 73, 30, 27, 27, 15, 0, 12]
```

- "Je suis une phrase" se caractérise par les caractères associés aux numéros : [74, 101, 32, 115, 117, 105, 115, 32, 117, 110, 101, 32, 112, 104, 114, 97, 115, 101] (Avec Unicode)
- "nsi" : [110, 115, 105] (Avec Unicode)

S'en suit des calculs à l'aide de l'opérateur xor entre chacun des caractères : 74 ⊕ 110, 101 ⊕ 115, 32 ⊕ 105, 115 ⊕ 110 ....

Le message après calcul sera : [36, 22, 73, 29, 6, 0, 29, 83, 28, 0, 22, 73, 30, 27, 27, 15, 0, 12] (Le message ici ne vaut pas le coup d'être reconstitué certains caractères ne sont pas affichable)

Il est possible de retrouver le message initial en effectuant une nouvelle opération xor entre le message chiffré et la clé.

### <u>DES</u> :

Cet algorithme majoritairement utilisé de 1970 à 2000 permettais de chiffrer des données aux Etats-Unis. Utilisant une clé de 56 bits (offrant 2**56 clés différentes).

Cet algorithme aura subit de nombreuses attaques par force brute (en essayant avec chaque clé), qui aura contraint le gouvernement américain de changer de méthode de cryptage.

### <u>AES</u> : 

Même principe que DES, inventé en 2001, cet algorithme utilise des clés plus grande (jusque 256 bits) et d'autres méthodes de traitement. Mais nous somme toujours avec 1 seule et unique clé.

## 2. Chiffrement asymétrique :

### <u>RSA :</u> 

Le chiffrement RSA est une technique de chiffrement asymétrique largement utilisée pour sécuriser les communications et protéger les données confidentielles. 

Dans un premier temps l'utilisateur génère une paire de clés : une clé publique et une clé privée. La clé publique est partagée avec les autres personnes pour chiffrer les messages. La clé privée est gardée secrète et utilisée pour déchiffrer les messages chiffrés avec la clé publique.

<u>Chiffrement d'un message :</u>

- Supposons que Bob souhaite envoyer un message confidentiel à Alice.
- Alice a déjà partagé sa clé publique avec Bob.
- Bob prend le message qu'il souhaite envoyer et le chiffre avec la clé publique d'Alice.
- Pour ce faire, Bob convertit le message en une valeur numérique et applique un calcul mathématique complexe en utilisant la clé publique d'Alice.
- Une fois le chiffrement terminé, Bob envoie le message chiffré à Alice.

<u>Déchiffrement du message :</u>

- Alice reçoit le message chiffré de Bob.
- Alice utilise sa clé privée pour effectuer un autre calcul mathématique sur le message chiffré.
- Grâce à sa clé privée qui correspond à sa clé publique, Alice est capable de déchiffrer le message et de le récupérer dans sa forme originale.

*La sécurité du chiffrement RSA repose sur la difficulté mathématique de factoriser de grands nombres premiers. La clé publique est basée sur un produit de deux nombres premiers, et la clé privée est calculée à partir de la connaissance des facteurs premiers de ce produit.*

En résumé, le chiffrement RSA utilise une paire de clés : une clé publique pour chiffrer les messages et une clé privée correspondante pour les déchiffrer. Cela permet à l'expéditeur d'envoyer des messages de manière sécurisée, sachant que seul le destinataire possédant la clé privée correspondante pourra les déchiffrer.

## 3. Certificat de tier de confiance :

Un certificat de tiers de confiance est un document électronique utilisé pour authentifier l'identité d'une partie dans une communication en ligne. Il est émis par une autorité tierce, généralement une entité de confiance **reconnue**, telle qu'une **autorité de certification** (CA) ou une **autorité de sécurité**, après vérification de l'identité de la partie concernée. 

Ces certificats sont utilisés pour sécuriser les communications en délivrant la clé publique de l'entité en question.

## 4. Conclusion :

Les chiffrements **symétriques** n'utilisent qu'une seule clé pour chiffer et déchiffrer. Ils sont peu coûteux et aussi très simple à déchiffrer. Ils ont longtemps été utilisé, mais les chiffrements asymétriques les ont remplacé.

Les chiffrement **asymétrique** utilisent deux clés, une publique et une privé. La clé publique peut être accéssible via des certificats de tiers de confiance, ou par l'entité elle même. Cette clé permet de **chiffrer** un message qui sera illisible pour quiconque ne possède pas la clé **privé**. La clé **privé** permet de **déchiffrer** le message chiffré et de retrouver le contenu initial.

## 5. Protocole HTTPS :

Ce protocole utilise à la fois les chiffrement symétrique et asymétrique. Petit rappel, le protocole HTTP permet de consulter des pages WEB, un client (utilisateur) envoie une requête  à un serveur afin de consulter une page, puis le serveur réponds en envoyant la page WEB.

Le problème de ce protocole est le suivant : si le client partage des données confidentielles (Authentification au site, partage de données bancaire pour un achat, ... ), celles-ci sont envoyées sans chiffrement et de ce fait elles peuvent être interceptées et réutilisées.

<u>Établissement de la connexion :</u>

Lorsqu'un utilisateur accède à un site web via HTTPS, le navigateur envoie une requête au serveur web. Celui-ci répond en envoyant son **certificat numérique** au navigateur qui contient la **clé publique du serveur** et est signé numériquement par une autorité de certification (AC) de confiance. (S'en suit une vérification du certificat par le navigateur)

<u>Échange de clés de session :</u>

Le navigateur génère une clé de session aléatoire et l'encrypte à l'aide de la clé publique du serveur. Le serveur reçoit la clé de session encryptée et utilise sa clé privée correspondante pour la déchiffrer.

<u>Établissement d'un canal sécurisé :</u>

Une fois que le navigateur et le serveur disposent de la clé de session, ils utilisent cette clé pour chiffrer et déchiffrer les données échangées pendant la session. Toutes les données transitant entre le navigateur et le serveur sont chiffrées et ne peuvent pas être lues par des tiers non autorisés.
