# Correction :

1. **SELECT** * **FROM** Pokedex
2. **SELECT** nom **FROM** Pokedex
3. **SELECT** nom **FROM** Pokedex **WHERE** hp > 100
4. **SELECT** nom **FROM** Pokedex **WHERE** Type_1 = 'Fire' or Type_2 = 'Fire'
5. **INSERT INTO** Pokedex values (999, 'PokeNSI','Fire','Grass',42,42,1,42,43,67,7,'False')
6. **SELECT** nom **FROM** Pokedex **WHERE** id = 999
7. **SELECT** **DISTINCT** Type_1 **FROM** Pokedex
8. **SELECT** nom,hp,Vitesse,Type_1,Type_2 **FROM** Pokedex **WHERE** (Legendaire = 'True' and (Type_1 = 'Dragon' or Type_2 = 'Dragon') and hp > 90 ) or ((Type_1 = 'Grass' or Type_2 = 'Grass') and Vitesse > 100)
9. **SELECT** nom,Vitesse,Generation **FROM** Pokedex **ORDER BY** Vitesse Desc, Generation
10. **DELETE** **FROM** Pokedex **WHERE** nom = 'Nom'
11. **UPDATE** Pokedex **SET** Legendaire = 'True' **WHERE** nom = 'Torterra'

