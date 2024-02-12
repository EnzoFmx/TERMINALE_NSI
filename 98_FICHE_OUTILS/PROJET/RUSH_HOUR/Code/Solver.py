import class_game
import File
import class_vehicule

def solver(game) :
    file=File.File1()
    file.enfile((game,''))
    ens =  set()
    while not file.est_vide():
        game_d,chemin_d=file.defile()
        if str(game_d) not in ens :
            ens.add(str(game_d))
            for vehicule in game_d.vehicules :
                moves =game_d.mouv_vehicule(vehicule)
                for m in moves:
                    config=m[0]
                    if not str(config) in ens:
                        chemin_final = chemin_d + ' ' + m[1] +'\n'+str(config)+'\n'
                        file.enfile((config,chemin_final))
                        if config.est_fini():
                            return (chemin_final)
                    
    return 'impossible'

if __name__ == '__main__' :
    pass
