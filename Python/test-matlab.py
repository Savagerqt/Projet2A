from Vertex import *
from Polygon_Optimization import *
import matplotlib.pyplot as plt
import math as m 
import numpy as np 
import matlab.engine 
import time 


# Construction d'une géometrie sous matlab 

v1 = Vertex(0,-1)
v2 = Vertex(0,1) 
v3 = Vertex(1,1.5) 
v4 = Vertex(2,-1) 
v5 = Vertex(0.5,-2)
P = Polygon(v1,v2,v3,v4,v5)


Q = P.deepCopy()
eng = matlab.engine.start_matlab() 

# Tracé initial et stockage de la valeur de l'intégrale initiale 

start = time.clock()
initMean = Q.valueIntegral(0,0,eng)             # Valeur initiale
initArea = Q.area()


Q.plotPY('g')    


values = []
# Boucle principale 
naiveMainloop(Q, 0.1, 3, 25, values, eng)
print(values)


endMean = Q.valueIntegral(0,0,eng)             # Valeur finale 
endArea = Q.area()

print("Valeur initiale : " + str(initMean))
print("Valeur finale : " + str(endMean))
print("Aire initiale : " + str(initArea))
print("Aire finale : " + str(endArea))

# Affichage temps de simulation
end = time.clock()
print("\nTemps de la simulation " + str(end - start))


# Tracé final 
Q.plotPY('b')
plt.show()


'''
y = [i for i in range(len(values))]
plt.plot(y, values,'x')  
'''



