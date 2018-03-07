from Vertex import *
from Polygon_Optimization import *
import matplotlib.pyplot as plt
import math as m
import numpy as np
import matlab.engine
import time


#   Définition de S
s1 = Vertex(0,-1)
s2 = Vertex(0,1)
s3 = Vertex(2,1.5)
s4 = Vertex(3,0.5)
s5 = Vertex(1,-1.5)
S = Polygon(s1, s2, s3, s4, s5)


#   Définition de P
v1 = Vertex(0, -1)
v2 = Vertex(0, 1)
v3 = Vertex(0.2, 1)
v4 = Vertex(5.549999999999926, 0)
v5 = Vertex(0.2, -1)
P = Polygon(v1, v2, v3, v4, v5)


#   Définition de Q Symétrique
c1 = Vertex(0, -1)
c2 = Vertex(0, 1)
c3 = Vertex(0.1, 4)
c4 = Vertex(1.410000000000001, 0)
c5 = Vertex(0.1, -4)
Q = Polygon(c1, c2, c3, c4, c5)

r1 = Vertex(0, -1)
r2 = Vertex(0, 1)
r3 = Vertex(0.05, 1.3)
r4 = Vertex(4.379999999999951, 0)
r5 = Vertex(0.05, -1.3)
R = Polygon(r1, r2, r3, r4, r5)



eng = matlab.engine.start_matlab()
print(S.valueIntegral(0, 0, eng))




plt.show()



'''


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

'''
