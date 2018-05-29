"""
=================================================================================
                      MODULE: degré de défaut de symétrie
=================================================================================
"""
from Vertex import *
from aire_polygone import *
from tkinter import *
from numpy import *
#nécessite l'importe du module aire_polygone


#-------------------------------------------------------------
#Pour trouver le point de l'axe qui complète
def sym(Poly_entree, pas, critere):

    Poly_sortie = [[0, -1], [0, 1], [0.1, 4], [0.15, 0], [0.1, -4]]
    for i in range(1000):
        if abs(aire_poly(Poly_entree) - aire_poly(Poly_sortie)) > critere:
            Poly_sortie[3][0] += pas
    return Poly_sortie, aire_poly(Poly_entree), aire_poly(Poly_sortie)


#-------------------------------------------------------------
#renvoie le second plus grand terme d'une liste
def second(L):
    L.remove(max(L))
    return max(L)

#-------------------------------------------------------------
#   teste le signe d'un nombre
def signe(nbr):
    if nbr > 0:
        return 1
    elif nbr == 0:
        return 0
    else:
        return -1


#-------------------------------------------------------------*=
#si x abscisse  d'un point
#la fonction renvoie les (un ou deux) couples de sommets consecutifs
#dont les abscisses des points respectifs
#encadrent x
def trouver_sommets(Poly, x):
    sommets = []
    Poly.append(Poly[0])
    for i in range(len(Poly) - 1):
        if signe(Poly[i][0] - x) != signe(Poly[i+1][0] - x):
            sommets.append([Poly[i], Poly[i+1]])

    #renvoie la borne xmax aussi
    return sommets


#-------------------------------------------------------------
#   Renvoie le y lié à la droite passant par point 1 et ponit 2
def interpol(point1, point2, x): #interpole l'ordonnée
    if point1[0] > point2[0] :
        point1, point2 = point2, point1
    a = (point2[1] - point1[1]) / (point2[0] - point1[0])
    b = point1[1] - a * point1[0]
    return a * x + b


#-------------------------------------------------------------
#    Main function
#    Renvoie le scalaire donnant le score de symétrie

#Fonction auxiliaire pour trouver la borne
def trouver_xmax(Poly):
    xmax = 0 #initialisation
    for increment in range(2, len(Poly)):
        if Poly[increment][0] > xmax:
            xmax = Poly[increment][0]
    return xmax

def deg_sym(Poly, nbr_pas):

    xborne = trouver_xmax(Poly) #initialisation de la borne a ne pas depasser pour sortir du polygone
    pas = xborne / nbr_pas #le pas de déplacement le long de l'axes
    x, xmax, deg = 0, -1, 0 #initialisation

    for increment in range(nbr_pas):

        #incrémentation de l'abscisse le long de l'axe de symétrie
        x += pas

        # Précaution pour ne pas qu'on sorte du polygone
        if x >= xborne: #teste si x est dans le polygone
            break

        #Pour optimiser les calculs, on ne change de sommet
        #que lorsque c'est nécessaire
        if x >= xmax:
            sommets_vois = trouver_sommets(Poly, x)
            xmax =  second([sommets_vois[0][0][0],
                            sommets_vois[0][1][0],
                            sommets_vois[1][0][0],
                            sommets_vois[1][1][0]])

        yhaut = interpol(sommets_vois[0][0], sommets_vois[0][1], x)
        ybas = interpol(sommets_vois[1][0], sommets_vois[1][1], x)

        if signe(yhaut) != signe(ybas):
            deg += abs(yhaut + ybas) / min(abs(yhaut), abs(ybas)) #normalisation de la longueur
        else:
            deg += abs((yhaut - ybas) / 2) / min(abs(yhaut), abs(ybas))

    return - deg

#poly0 = [[0, -1], [0, 1], [2, 2], [3, 0], [2, -2]]
#poly1 = [[0, -1], [0, 1], [1, 1.5], [2, -7], [1, -5]]
#poly2 = [[0, -2], [0, 2], [2, 3], [4, -14], [2, -10]]
#poly3 = [[0, -1], [0, 1], [1, 1.5], [2, -4], [1, -1.5]]
#poly4 = [[0, -1], [0, 1], [2, 1], [3,0], [2, -2]]

# Exemple à decommenter
#print(deg_sym(poly0, 500))
#print(deg_sym(poly1, 500))
#print(deg_sym(poly2, 500))
#print(deg_sym(poly3, 500))
#print(deg_sym(poly4, 500))

def recup(Poly):
    x, y =  [], []
    for e in Poly:
        x.append(e[0]), y.append(e[1])
    x.append(Poly[0][0])
    y.append(Poly[0][1])
    return x,y



#from pylab import *
#
#x,y = recup(poly4)
#plot(x, y)
#title("Polygone 4")
#show()
