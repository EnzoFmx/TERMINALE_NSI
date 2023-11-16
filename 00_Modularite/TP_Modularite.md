# TP Modularité

## 1. Objectifs

- Ecrire de bonnes documentations
- Faire la distinction entre définition de fonction et appel de fonction
- Utiliser le module Doctest

## 2. A faire

1. Reprendre le fichier contenant les fonctions de rappel de première.

2. Inclure cette ligne dans le fichier (à la première ligne) :

   ```python
   import doctest
   ```

3. Inclure en bas de fichier les lignes :

   ```python
   if __name__=="__main__":
       doctest.testmod(verbose=True)
   ```

4. Pour chaque fonctions du rappel première, les reprendre et écrire la documentation et la doctest.

