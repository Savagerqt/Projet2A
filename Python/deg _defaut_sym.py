'MODULE: degré de défaut de symétrie'

#nécessite l'importe du module aire_polygone

def sym(Poly_entree, pas, critere): #Pour trouver le point de l'axe qui complète
    Poly_sortie = [[0,-1], [0,1], [0.1, 4], [0.15, 0], [0.1, -4]]
    for i in range(1000):
        if abs(aire_poly(Poly_entree) - aire_poly(Poly_sortie)) > critere:
            Poly_sortie[3][0] += pas
    return Poly_sortie, aire_poly(Poly_entree), aire_poly(Poly_sortie)
    
# print(sym(P, 0.01, 0.01))

def second(L): #renvoit le second plus grand terme d'une liste 
    L.remove(max(L))
    return max(L)
    
#Try
#print(second(list(range(5))))

def signe(nbr): #teste le signe d'un nombre 
    if nbr >= 0:
        return 1
    else: 
        return -1

def trouver_sommets(Poly, x): #renvoie les sommets concernés 
    # print(Poly)
    # print(x)
    sommets = []
    Poly.append(Poly[0])
    for i in range(len(Poly) - 1):
        if signe(Poly[i][0] - x) != signe(Poly[i+1][0] - x): 
            sommets.append([Poly[i], Poly[i+1]])
    return sommets  #renvoie la borne xmax aussi

#Try
# sommets = trouver_sommets(P, 0.2)
# print(sommets)
    
def interpol(point1, point2, x): #interpole l'ordonnée
    if point1[0] > point2[0]:
        point1, point2 = point2, point1
    a = (point2[1] - point1[1]) / (point2[0] - point1[0])
    b = point1[1] - a * point1[0]
    return a * x + b
    
#try 
# print(interpol([1,1], [0,0], 0.5))

def deg_sym(Poly, pas):
    xborne = Poly[0][0] #initialisation de la borne a pas depassée pour sortir du polygone 
    for i in range(1, len(Poly)):
        if Poly[i][0] > xborne:
            xborne = Poly[i][0]
    x = 0 #initialisation
    xmax = -1 #initialisation
    deg = 0
    for i in range(10000):
        x += pas #incrémentation de l'abscisse le long de l'axe de symétrie 
        if x >= xborne: #teste pas hors du polygon 
            break 
        if x >= xmax:
            sommets_vois = trouver_sommets(Poly, x)
            xmax =  second([sommets_vois[0][0][0], sommets_vois[0][1][0], sommets_vois[1][0][0], sommets_vois[1][1][0]]) 
        yhaut = interpol(sommets_vois[0][0], sommets_vois[0][1], x)
        ybas = interpol(sommets_vois[1][0], sommets_vois[1][1], x)
        if signe(yhaut) != signe(ybas):
            deg += abs(yhaut + ybas)
        else: 
            deg += abs((yhaut - ybas) / 2)
    return deg
    
#Try 
# print("deg de défaut de symétrie d'un polygon symétrique")
# poly1 = [[0, -1], [0, 1], [1, 1], [2, 0], [1, -1]]
# print(deg_sym(poly1, 0.1))
# 
# print("deg de défaut de symétrie d'un polygon non symétrique")
# poly2 = [[0, -1], [0, 1], [1, 1.5], [2, -1], [0.5, -2]]
# print(deg_sym(poly2, 0.1))

# print("deg de défaut de symétrie d'un polygon pas mal symétrique")
# poly1 = [[0, -1], [0, 1], [1, 1], [3, 0], [2, -1]]
# print(deg_sym(poly1, 0.1))
# 
# print("deg de défaut de symétrie d'un polygon peu symétrique")
# poly2 = [[0, -1], [1, 2], [1, 1.5], [3, -2], [2, -3]]
# print(deg_sym(poly2, 0.1))
