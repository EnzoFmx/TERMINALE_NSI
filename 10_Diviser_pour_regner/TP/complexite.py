import matplotlib.pyplot as pylab
import time
import random

def construit_tab_alea(taille) :
    """
    Fonction qui crée un tableau avec des valeur aléatoire de taille taille
    param taille : (int) Taille du tableau
    return : (list) Tableau à renvoyer
    """
    tab = []
    for i in range(taille) :
            val = random.randint(0,1000)
            tab.append(val)
    return tab

def moyenne(tab):
    moy = 0
    for i in tab :
        moy += i
    return moy/len(tab)

##############################################################################################################################

"""
# Construction de t_temps_tri_fusion :
t_temps_tri_fusion = []
for taille in t_taille:
    t_moy = []
    for _ in range(3000):
        tab = construit_tab_alea(taille)
        t1 = time.process_time()
        tri_fusion(tab)
        t2 = time.process_time()
        duree = t2 - t1
        t_moy.append(duree)
    duree_moy = moyenne(t_moy)
    t_temps_tri_fusion.append(duree_moy)
    
print("Tri fusion fini")
"""
t_taille = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# Courbes moyenne :
t_temps_tri_insertion_pire_cas_moy = [0.0, 0.0, 5.208333333333333e-06, 0.0, 5.208333333333333e-06, 5.208333333333333e-06, 1.0416666666666666e-05, 5.208333333333333e-06, 1.5625e-05, 5.208333333333333e-06, 1.5625e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 2.604166666666667e-05, 3.125e-05, 3.125e-05, 4.1666666666666665e-05, 4.1666666666666665e-05, 4.6875e-05, 5.208333333333334e-05, 5.208333333333334e-05, 6.25e-05, 6.25e-05, 7.291666666666667e-05, 6.770833333333333e-05, 8.333333333333333e-05, 8.333333333333333e-05, 9.895833333333333e-05, 9.895833333333333e-05, 0.000109375, 0.000109375, 0.00011979166666666666, 0.00013020833333333333, 0.00013020833333333333, 0.00015104166666666667, 0.00015104166666666667, 0.00016666666666666666, 0.00018229166666666667, 0.00017708333333333335, 0.00018229166666666667, 0.000203125, 0.000203125, 0.00022395833333333333, 0.00022395833333333333, 0.00023958333333333332, 0.00025, 0.00026041666666666666, 0.00026041666666666666, 0.00028125, 0.000296875, 0.00030208333333333335, 0.00032291666666666666, 0.000328125, 0.0003385416666666667, 0.0003541666666666667, 0.0003541666666666667, 0.0003802083333333333, 0.0003958333333333333, 0.000421875, 0.00041145833333333334, 0.0004427083333333333, 0.00044791666666666667, 0.0004583333333333333, 0.000515625, 0.000515625, 0.0005364583333333333, 0.0005364583333333333, 0.0005520833333333334, 0.0005572916666666667, 0.0005833333333333334, 0.00059375, 0.000609375, 0.0006145833333333333, 0.0006302083333333333, 0.0006458333333333333, 0.0006666666666666666, 0.0006822916666666667, 0.000703125, 0.0007239583333333333, 0.0007395833333333333, 0.0007552083333333333, 0.0007864583333333333, 0.0007864583333333333, 0.0008177083333333334, 0.000828125, 0.0008541666666666667, 0.0008697916666666667, 0.0008958333333333333, 0.00090625, 0.0009427083333333334, 0.0009635416666666667, 0.0009791666666666666, 0.0009947916666666666, 0.0010208333333333332, 0.0010260416666666666, 0.0010572916666666667, 0.001078125, 0.00109375, 0.001109375]
t_temps_tri_insertion_meilleur_cas_moy = [0.0, 5.208333333333333e-06, 0.0, 0.0, 5.208333333333333e-06, 0.0, 5.208333333333333e-06, 5.208333333333333e-06, 5.208333333333333e-06, 5.208333333333333e-06, 0.0, 5.208333333333333e-06, 1.0416666666666666e-05, 0.0, 5.208333333333333e-06, 5.208333333333333e-06, 5.208333333333333e-06, 5.208333333333333e-06, 1.0416666666666666e-05, 5.208333333333333e-06, 1.0416666666666666e-05, 5.208333333333333e-06, 1.0416666666666666e-05, 1.0416666666666666e-05, 5.208333333333333e-06, 1.0416666666666666e-05, 1.0416666666666666e-05, 5.208333333333333e-06, 1.0416666666666666e-05, 1.0416666666666666e-05, 1.0416666666666666e-05, 1.0416666666666666e-05, 1.0416666666666666e-05, 5.208333333333333e-06, 1.5625e-05, 1.0416666666666666e-05, 1.0416666666666666e-05, 1.5625e-05, 1.0416666666666666e-05, 5.208333333333333e-06, 1.5625e-05, 1.0416666666666666e-05, 1.5625e-05, 1.0416666666666666e-05, 1.5625e-05, 1.5625e-05, 1.5625e-05, 1.0416666666666666e-05, 1.5625e-05, 1.5625e-05, 1.5625e-05, 1.5625e-05, 1.5625e-05, 1.0416666666666666e-05, 1.0416666666666666e-05, 1.5625e-05, 2.0833333333333333e-05, 1.5625e-05, 1.5625e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 1.5625e-05, 1.5625e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 1.5625e-05, 2.0833333333333333e-05, 1.5625e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 1.5625e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 2.604166666666667e-05, 2.0833333333333333e-05, 2.604166666666667e-05, 2.604166666666667e-05, 2.604166666666667e-05, 2.0833333333333333e-05, 2.604166666666667e-05, 2.604166666666667e-05, 2.604166666666667e-05, 2.604166666666667e-05, 2.604166666666667e-05, 2.0833333333333333e-05, 2.0833333333333333e-05, 2.604166666666667e-05, 2.604166666666667e-05, 2.604166666666667e-05, 2.0833333333333333e-05, 2.604166666666667e-05, 3.125e-05, 2.604166666666667e-05, 3.125e-05, 2.604166666666667e-05]
t_temps_tri_fusion = [0.0, 0.0, 5.208333333333333e-06, 0.0, 1.0416666666666666e-05, 1.5625e-05, 5.208333333333333e-06, 2.604166666666667e-05, 5.208333333333333e-06, 2.604166666666667e-05, 2.0833333333333333e-05, 1.0416666666666666e-05, 2.604166666666667e-05, 4.6875e-05, 3.6458333333333336e-05, 5.7291666666666666e-05, 5.7291666666666666e-05, 4.1666666666666665e-05, 4.6875e-05, 6.25e-05, 7.291666666666667e-05, 7.8125e-05, 6.770833333333333e-05, 7.291666666666667e-05, 6.25e-05, 9.375e-05, 8.854166666666667e-05, 0.00011979166666666666, 0.00013020833333333333, 8.854166666666667e-05, 8.854166666666667e-05, 0.000109375, 8.854166666666667e-05, 0.00011458333333333333, 0.00013020833333333333, 0.00013020833333333333, 0.00013020833333333333, 0.00011979166666666666, 0.00015104166666666667, 0.000140625, 0.00011979166666666666, 0.00017708333333333335, 0.00016145833333333333, 0.00013541666666666666, 0.0001875, 0.00019791666666666666, 0.00017708333333333335, 0.00016666666666666666, 0.00019270833333333333, 0.00016666666666666666, 0.00023958333333333332, 0.000203125, 0.00021354166666666668, 0.00021354166666666668, 0.000234375, 0.00022395833333333333, 0.00022395833333333333, 0.000234375, 0.00023958333333333332, 0.00026041666666666666, 0.00023958333333333332, 0.0003125, 0.000328125, 0.00030729166666666665, 0.000328125, 0.00030208333333333335, 0.00028125, 0.00028645833333333333, 0.00030729166666666665, 0.00030729166666666665, 0.0002916666666666667, 0.000328125, 0.00030208333333333335, 0.00030729166666666665, 0.00034375, 0.0003177083333333333, 0.00032291666666666666, 0.0003333333333333333, 0.00030208333333333335, 0.00032291666666666666, 0.00034895833333333334, 0.0003541666666666667, 0.0003958333333333333, 0.000390625, 0.0004166666666666667, 0.00040625, 0.000359375, 0.0004010416666666667, 0.000375, 0.000390625, 0.000390625, 0.00036979166666666665, 0.00044791666666666667, 0.00044791666666666667, 0.00040625, 0.0004427083333333333, 0.00040625, 0.0003958333333333333, 0.0004635416666666667, 0.000421875]
t_temps_selection_moy = [0.0, 5.208333333333333e-06, 5.208333333333333e-06, 1.0416666666666666e-05, 5.208333333333333e-06, 1.0416666666666666e-05, 2.0833333333333333e-05, 1.5625e-05, 2.0833333333333333e-05, 2.604166666666667e-05, 3.125e-05, 3.125e-05, 3.6458333333333336e-05, 3.6458333333333336e-05, 3.6458333333333336e-05, 4.6875e-05, 4.1666666666666665e-05, 4.6875e-05, 5.208333333333334e-05, 5.7291666666666666e-05, 5.7291666666666666e-05, 6.25e-05, 6.25e-05, 7.291666666666667e-05, 7.8125e-05, 7.8125e-05, 8.854166666666667e-05, 9.375e-05, 9.895833333333333e-05, 0.00010416666666666667, 0.00010416666666666667, 0.000109375, 0.00011979166666666666, 0.00011979166666666666, 0.000125, 0.000125, 0.000140625, 0.00013541666666666666, 0.00015104166666666667, 0.00015104166666666667, 0.00016666666666666666, 0.00016666666666666666, 0.000171875, 0.00017708333333333335, 0.00018229166666666667, 0.00019270833333333333, 0.000203125, 0.000203125, 0.00020833333333333335, 0.00022395833333333333, 0.00022395833333333333, 0.000234375, 0.000234375, 0.00023958333333333332, 0.0002552083333333333, 0.00026041666666666666, 0.000265625, 0.0002708333333333333, 0.00028645833333333333, 0.00028645833333333333, 0.00030208333333333335, 0.00030208333333333335, 0.0003125, 0.0003177083333333333, 0.000328125, 0.0003385416666666667, 0.00034375, 0.000359375, 0.000359375, 0.00036979166666666665, 0.0003802083333333333, 0.00038541666666666667, 0.0003958333333333333, 0.00040625, 0.000421875, 0.00043229166666666665, 0.00043229166666666665, 0.000453125, 0.000453125, 0.0004635416666666667, 0.00046875, 0.00047395833333333334, 0.0005, 0.0005104166666666666, 0.0005260416666666666, 0.00053125, 0.0005416666666666666, 0.0005416666666666666, 0.0005520833333333334, 0.0005625, 0.000578125, 0.0005885416666666667, 0.0005989583333333333, 0.0006145833333333333, 0.0006197916666666667, 0.000640625, 0.000640625, 0.0006614583333333333, 0.0006875, 0.0006927083333333334]

pylab.plot(t_taille,t_temps_tri_insertion_pire_cas_moy,label = 'tri insertion pire cas')
pylab.plot(t_taille,t_temps_tri_insertion_meilleur_cas_moy,label = 'tri insertion meilleur cas')
pylab.plot(t_taille,t_temps_selection_moy,label = 'tri selection')
pylab.plot(t_taille,t_temps_tri_fusion,label = 'tri fusion')
pylab.legend()
pylab.show()