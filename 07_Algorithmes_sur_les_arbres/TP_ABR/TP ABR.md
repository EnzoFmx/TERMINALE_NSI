# TP ABR :

------

## 1. Rappel ABR : 

Un ABR ou Arbre binaire de recherche est un arbre dans le quel les valeurs sont triées selon cette règle :

- Un ABR a pour tout nœud ayant une valeur *e* :

  - les valeurs de tous les nœuds du sous-arbre gauche sont inférieures ou égales à *e* ;
  - les valeurs de tous les nœuds du sous-arbre droit sont supérieures à *e*.

Pour ce TP nous utiliserons cette classe :

```python
class Arbre :
    """Classe Arbre, permettant de créer des arbres binaire"""
    def __init__(self,valeur=None,fils_gauche=None,fils_droit=None):
        """
        Méthode constructeur permettant de créer un arbre
        param valeur : (int/str) Valeur du noeud
        fils_gauche/fils_droit : (Arbre/None) Fils gauche/droit de l'arbre
        """
        self.valeur = valeur
        self.fils_droit = fils_droit
        self.fils_gauche = fils_gauche
```

## 2. Insérer un élément dans un ABR :

L'insertion d'élément dans un arbre se fait de manière récursive. Lorsque l'on veut ajouter un élément inférieur on le place à gauche, un élément supérieur sera placé à droite. Si il y a déjà deux fils (gauche et droite), on applique le raisonnement au sous-arbre gauche (si inférieur), au sous-arbre droit (si supérieur).

```python
# Algorithme en pseudo-code :
def ajout_element_dans_abr(element,arbre) :
    # Si l'élément est inférieur à la valeur de l'arbre :
    	#On vérifie si le sous arbre gauche existe
        	# Si oui => On applique l'algo à ce sous arbre
            # On ajoute la valeur sinon
    # Idem pour le sous arbre droit

```

## 3. Recherche d'un élément dans un ABR :

La recherche d'élément se fait aussi de manière récursive. On recherche un élément dans un arbre, on vérifie dans un premier temps si la valeur de l'arbre correspond à l'élément recherché. Si celle-ci ne correspond pas, reste à voir si la recherche se fera dans le sous-arbre droit, ou sous-arbre gauche.

Lorsqu'on tombe sur un arbre vide sans avoir trouvé la valeur. On considère qu'elle n'est pas dans l'arbre.

(La valeur de retour ici est à définir)

## 4. A faire :

Ecrire les deux algorithmes du dessus. Puis les appliquer sur des ABR.

Afficher les résultats des différents tests. (Concluants ou non)

 



