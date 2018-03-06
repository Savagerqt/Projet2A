"""
=================================================================================
                      MODULE: degré de défaut de symétrie
=================================================================================
"""
from aire_polygone import *
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
    if nbr >= 0:
        return 1
    else:
        return -1


#-------------------------------------------------------------
def trouver_sommets(Poly, x): #renvoie les sommets concernés

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
def deg_sym(Poly, pas):

    #initialisation de la borne a pas depassée pour sortir du polygone
    xborne = Poly[0][0]
    for i in range(1, len(Poly)):
        if Poly[i][0] > xborne:
            xborne = Poly[i][0]
    x = 0 #initialisation
    xmax = -1 #initialisation
    deg = 0


    for i in range(int(xborne / pas)):

        #incrémentation de l'abscisse le long de l'axe de symétrie
        x += pas

        # Précaution pour ne pas qu'on sorte du polygone
        if x >= xborne: #teste si x est dans le polygone
            break
        if x >= xmax:
            sommets_vois = trouver_sommets(Poly, x)
            xmax =  second([sommets_vois[0][0][0],
                            sommets_vois[0][1][0],
                            sommets_vois[1][0][0],
                            sommets_vois[1][1][0]])

        yhaut = interpol(sommets_vois[0][0], sommets_vois[0][1], x)
        ybas = interpol(sommets_vois[1][0], sommets_vois[1][1], x)

        if signe(yhaut) != signe(ybas):
            deg += abs(yhaut + ybas)
        else:
            deg += abs((yhaut - ybas) / 2)
            
    return deg
