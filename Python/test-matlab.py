from Vertex import *
from Polygon_Optimization import *
import matplotlib.pyplot as plt
import math as m 
import numpy as np 
import matlab.engine 
import time 


#   Définition de P 
v1 = Vertex(0,-1)
v2 = Vertex(0,1) 
v3 = Vertex(1,1.5) 
v4 = Vertex(2,-1) 
v5 = Vertex(0.5,-2)
P = Polygon(v1, v2, v3, v4, v5)




#   Définition de Q Symétrique
c1 = Vertex(0, -1) 
c2 = Vertex(0,1)
c3 = Vertex(1,1)
c4 = Vertex(2,0) 
c5 = Vertex(1,-1)
Q = Polygon(c1, c2, c3, c4, c5)




eng = matlab.engine.start_matlab() 

# Tracé initial et stockage de la valeur de l'intégrale initiale 

start = time.clock()
initMean = Q.valueIntegral(0,0,eng)             # Valeur initiale
initArea = Q.area()


Q.plotPY('g')    


values = []
# Boucle principale 
OSMainloop(Q, 0.1, 10, 1, eng)
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



