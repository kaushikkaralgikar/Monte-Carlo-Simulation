import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

x = np.linspace(42.26,100,100)
y = - math.sqrt(3)* (x - 100) 

plt.plot(x, y, '-b')

x = np.linspace(0,42.26,100)
y = 2.366 * x
plt.plot(x, y, '-r', label='y=2x+1')

plt.axhline(y=0, color='g', linestyle='-')
plt.xticks([0, 20, 40, 60, 80, 100], [100, 80, 60, 40, 20, 0], color="red")
 
G = [10,20,30,40,50,0,50,100,0,0,33.33] #contribution of G
B = [20,30,40,50,50,50,0,0,100,0,33.33] #contribution of B
C = [70,50,30,10,0,50,50,0,0,100,33.33] #contribution of C


for i in range(len(G)):
    y = G[i]
    x = - (G[i]/1.732) + (100 - B[i])
    #scatter plot
    plt.scatter(x,y, s=60, c='black', marker='^')
plt.show()


