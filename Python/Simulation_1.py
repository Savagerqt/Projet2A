"""
======================================================================
                        Script de simulation
                            COMPARAISON
======================================================================
"""
from Vertex import *
from Polygon_Optimization import *
import matlab.engine
import matplotlib.pyplot as plt

eng = matlab.engine.start_matlab()

# Création du fichier de Sauvegarde
import os
os.chdir("/Users/viviertanguy/Documents/GitHub/Projet-2A/Simulations")
resultat = open("resultat_comparaison_2.txt", "w")

# Entete
resultat.write("======================================================================\n")
resultat.write("              Simulation 1bis - Méthode Souple \n")
resultat.write("======================================================================\n\n\n")

s1 = Vertex(0,-1)
s2 = Vertex(0,1)
s3 = Vertex(2,1.5)
s4 = Vertex(2.5,0)
s5 = Vertex(2,-1.5)
S = Polygon(s1, s2, s3, s4, s5)
S.plotPY('y')
K = S.deepCopy()
area = S.area()
"""
# ---------------------------------------------------------------------------
resultat.write("*********************** ALGO NAIF *****************************\n")
resultat.write("PAS : 0.05, NBTEST = 1\n")
resultat.write("Polygone d'entree d'algorithme NAIF: \n " + S.__str__() + "\n")
resultat.write("Aire Initiale : " + str(area) + "\n")
resultat.write("Methode iterative naive pour 50 itérations maximum \n\n")
# On lance la première simulation
values = []
nbIte = naiveMainloop(S, .05, 1, 50, values, eng)
S.plotPY('r')
resultat.write("Polygone de sortie d'algorithme NAIF : \n " + S.__str__() + "\n")
resultat.write("Aire Finale : " + str(S.area()) + "\n")
resultat.write("Nombre d'iterations : " + str(len(values)) + "\n")
resultat.write("Valeurs après chaque itération : " + str(values) + "\n\n")
"""
# ---------------------------------------------------------------------------
S = K.deepCopy()
resultat.write("*********************** ALGO SOUPLE ****************************\n")
resultat.write("r = 0.05, NBTEST = 4\n")
resultat.write("Polygone d'entree d'algorithme SOUPLE : \n " + S.__str__() + "\n")
resultat.write("Aire Initiale : " + str(S.area()) + "\n")
resultat.write("Methode iterative souple pour 50 itérations maximum \n\n")
values = []
mainloopContraction(S, 4, 100, .05, area, values, eng)
S.plotPY('b')
resultat.write("Polygone de sortie d'algorithme SOUPLE : \n " + S.__str__() + "\n")
resultat.write("Aire Finale : " + str(S.area()) + "\n")
resultat.write("Nombre d'iterations : " + str(len(values)) + "\n")
resultat.write("Valeurs après chaque itération : " + str(values) + "\n\n")


resultat.close()

plt.show()
