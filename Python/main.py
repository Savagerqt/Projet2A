from Vertex import *
from Polygon_Optimization import *
import matplotlib.pyplot as plt
import math as m
import numpy as np
import matlab.engine
import time

#   Définition de S un polynome quelconque
s1 = Vertex(0,-1)
s2 = Vertex(0,1)
s3 = Vertex(2,1.5)
s4 = Vertex(2.5,0.5)
s5 = Vertex(2,-1)
S = Polygon(s1, s2, s3, s4, s5)

v1 = Vertex(0,-1)
v2 = Vertex(0,1)
v3 = Vertex(1.019,1.691)
v4 = Vertex(2.5,0.5)
v5 = Vertex(2,-1)
V = Polygon(v1, v2, v3, v4, v5)

w1 = Vertex(0,-1)
w2 = Vertex(0,1)
w3 = Vertex(1.543,1.7)
w4 = Vertex(2.043,0.5)
w5 = Vertex(1.5437,-1)
W = Polygon(w1, w2, w3, w4, w5)

S.plotPY('b')
V.plotPY('r')
W.plotPY('g')
plt.show()







#S.plotPY('r')
#plt.show()





"""


print(P.valueIntegral(0, 0, eng))
print(P.area())
P.plotPY('g')
plt.show()
# Tracé initial et stockage de la valeur de l'intégrale initiale

start = time.clock()
initMean = P.valueIntegral(0,0,eng)             # Valeur initiale
initArea = P.area()


values = []
# Boucle principale
naiveMainloop(P, 0.1, 2, 5, values, eng)
print(values)


endMean = P.valueIntegral(0,0,eng)             # Valeur finale
endArea = P.area()

print("Valeur initiale : " + str(initMean))
print("Valeur finale : " + str(endMean))
print("Aire initiale : " + str(initArea))
print("Aire finale : " + str(endArea))

# Affichage temps de simulation
end = time.clock()
print("\nTemps de la simulation " + str(end - start))


# Tracé final
P.plotPY('b')
plt.show()

"""
