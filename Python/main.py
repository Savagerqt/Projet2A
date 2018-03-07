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
s4 = Vertex(3,0.5)
s5 = Vertex(1,-1.5)
S = Polygon(s1, s2, s3, s4, s5)

S.plotPY('r')
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
