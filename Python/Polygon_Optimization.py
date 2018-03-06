# -*- coding: utf-8 -*-
"""
=================================================================================
                                 Main Algorithm
=================================================================================
"""

from Vertex import *
import matlab.engine
import matplotlib.pyplot as plt
import numpy as np



# ===============================================================================
#                             Best Value of a vertex
# ===============================================================================

#   On cherche la position du sommet i qui maximise la fonctionnelle de forme
#   la fonction prend en paramètres :
#
#   - initValue : la valeur de l'intégrale du polygone initial (pour optimiser
#     et ne pas avoir à le calculer à chaque fois)
#
#   - dl : la longueur du pas
#
#   - i : le numéro du sommet
#
#   - nbTest : le nombre de valeur testée de part et d'autre du sommet, en tout
#     2*nbTest valeurs sont testées sur chaque sommet
#
#   - eng : le moteur matlab
#

def bestValue(polygon, initValue, i, nbTest, dl, eng) :

    #   On stocke les valeurs des intégrales liées à chacun des déplacements
    #   dans une liste
    #   right correspond aux déplacements à droite du point
    #   left correspond aux déplacement à gauche du point

    left = [polygon.valueIntegral(i, -j * dl, eng) for j in range(nbTest)]
    right = [polygon.valueIntegral(i, j * dl, eng) for j in range(nbTest)]
    L = np.array(left + [initValue] + right)

    #   On cherche le maximum dans cette liste, puis on trouve l'index de ce
    #   maximum, qu'on appelle indexMax
    indexMax = np.argmax(L)

    #   Le résulat retourné contient la valeur maximum de l'intégrale,
    #   et le déplacement associé à celui-ci
    return [L[indexMax], (indexMax - nbTest) * dl]







def bestValueOS(polygon, initValue, i, nbTest, dl, eng) :
    #    OS : Odd Symetrical
    #   On stocke les valeurs des intégrales liées à chacun des déplacements
    #   dans une liste
    #   right correspond aux déplacements à droite du point
    #   left correspond aux déplacement à gauche du point

    left = [polygon.valueIntegral(i, -j * dl, eng) for j in range(nbTest)]
    right = [polygon.valueIntegral(i, j * dl, eng) for j in range(nbTest)]
    L = np.array(left + [initValue] + right)

    #   On cherche le maximum dans cette liste, puis on trouve l'index de ce
    #   maximum, qu'on appelle indexMax
    indexMax = np.argmax(L)

    #   Le résulat retourné contient la valeur maximum de l'intégrale,
    #   et le déplacement associé à celui-ci
    return [L[indexMax], (indexMax - nbTest) * dl]





# ===============================================================================
#                              Naive Mainloop
# ===============================================================================

#   Cette boucle naïve se contente de parcourir les sommets pour trouver le
#   meilleur déplacement possible


def naiveMainloop(polygon, dl, nbTest, nbIteration, values, eng) :
    #   Conservation des données de la temperature moyenne pour chaque itération
    #   values est une liste vide destinée à conserver les valeurs de l'intégrale

    if nbIteration == 0 :
        print("Fin de la simulation")
        return 0

    initValue = polygon.valueIntegral(0,0,eng)

    #   On cherche le petit déplacement qui maximise notre fonctionnelle
    #   de forme lors d'une itération de l'algorithme
    #   On examine chacun des sommets indépendamment

    max = [0,0]                                                     # Initialisation du maximum
    rank = 0
    for i in range(2, polygon.N) :
        val = bestValue(polygon, initValue, i, nbTest, dl, eng)
        if val[0] > max[0] :
            max = val
            rank = i

    #   Si la valeur maximum est atteinte pour un déplacement nul,
    #   on arrête la simulation
    if max[1] == 0 :
        print("Il reste " + str(nbIteration) + " itérations")
        return 0

    # Sinon on bouge un sommet
    polygon.move(rank, max[1])
    values.append(max[0])

    # Appel récursive de la fonction
    naiveMainloop(polygon, dl, nbTest, nbIteration - 1, values, eng)



# ===============================================================================
#                          Mainloop with refinement
# ===============================================================================

#   Il s'agit plus ou moins de la même boucle que la précédente, sauf que cette fois
#   ci, l'algorithme rafine le pas quand la polygone a été suffisamment optimisé
#   pour un pas donné

def refineMainloop(polygon, dl, nbIteration, eng) :

    if nbIteration == 0 or dl < 0.001 :
        print("Fin de la simulation")
        return 0

    initValue = polygon.valueIntegral(0,0,eng)

    #   On cherche le petit déplacement qui maximise notre fonctionnelle
    #   de forme lors d'une itération de l'algorithme
    #   On examine chacun des sommets indépendamment

    max = [0,0]                                                     # Initialisation du maximum
    rank = 0
    for i in range(2, polygon.N) :
        val = bestValue(polygon, initValue, i, dl, eng)
        if val[0] > max[0] :
            max = val
            rank = i

    #   Si le polygone ne bouge plus, on raffine le pas
    #   On ne prend pas non plus un pas trop petit, car
    #   cela sera inutile

    if max[1] == 0 :
        print("Raffinement du pas" + str(dl/2))
        refineMainloop(polygon, dl/2, nbIteration - 1, eng)

    # Sinon on bouge un sommet
    polygon.move(rank, max[1])

    # Appel récursive de la fonction
    refineMainloop(polygon, dl, nbIteration - 1, eng)




# ===============================================================================
#               Mainloop on Symetrical Figures with Odd number of sides
# ===============================================================================


#   Cette fois-ci, la boucle de l'algorithme est adaptée pour traiter les
#   figures symétriques, pour gagner du temps d'execution notamment.
#   On travaille d'abord avec un nombre de côtés impaires car les
#   mouvement sont beaucoup plus faciles à traiter qu'avec les polygones
#   pairs

def OSMainloop(polygon, dl, nbIteration, nbTest, eng) :

    if nbIteration == 0 :
        print("Fin de la simulation")
        return 0

    initValue = polygon.valueIntegral(0,0,eng)

    #   On cherche le petit déplacement qui maximise notre fonctionnelle
    #   de forme lors d'une itération de l'algorithme
    #   On examine chacun des sommets indépendamment

    max = [0,0]                                                     # Initialisation du maximum
    rank = 0
    for i in range(2, int((polygon.N + 3) / 2)) :
        val = bestValueOS(polygon, initValue, i, nbTest, dl, eng)
        if val[0] > max[0] :
            max = val
            rank = i

    #   S'il n'y a pas d'améliorations, on stoppe
    if max[1] == 0 :
        print("Fin de la simulation")
        return 1

    # Sinon on bouge un sommet
    polygon.move(rank, max[1])
    polygon.move(polygon.N - rank + 1, -max[1])

    # Appel récursive de la fonction
    OSMainloop(polygon, dl, nbIteration - 1, nbTest, eng)




#   Idées à faire pour le developpement du code :
#
#   @ Exploitation des symétries
