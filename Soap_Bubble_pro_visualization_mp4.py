#https://www.google.ch/search?q=matplotlib%20animation&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:de:official&client=firefox-a&channel=np&source=hp#client=firefox-a&hs=4jz&rls=org.mozilla:de%3Aofficial&channel=np&biw=1366&bih=647&sclient=psy-ab&q=matplotlib+funcanimation&oq=matplotlib+func&gs_l=serp.3.0.0l2j0i30l2.25291.27343.0.29806.6.5.0.1.1.0.189.688.0j5.5.0....0...1c.1.19.psy-ab.JpS0kO7FiFA&pbx=1&bav=on.2,or.r_qf.&bvm=bv.48705608,d.bGE&fp=eee66d236af74eaf

from math import*
from random import*


# Einstellungen

i = 20 #randint(3, 25) # Werte in x Richtung
j = 20#randint(3, 25) # Werte in y Richtung

maxinput = 100

z = 0.001 #Abweichung der Annaeherung (average(i,j)-4*(i,j))



# Programmstart...

p = maxinput #randint(5, maxinput) # randint maximum
q = 0        #randint minimum

#----------

u = [] # u = j in der Liste
v = [] # v = i in der Liste
k = [] # Berechnungsschritt



h = 0 # Automatische groesse zum Berechnungsschritt

r = p # Kontrollkonstante

#-----

for a in range(0, i):
    u = []
    for b in range(0, j):
        u.append(randint(q, p))
    v.append(u)
k.append(v)
        
#print("Input (Berechnungstiefe: 0 )")
#for a in range(0, i):
#    for b in range(0, j):
        #print("(", a + 1, ", ", b + 1, ") =", k[h][a][b])

#-----

while z*((i - 2)*(j - 2)) < r :
    
    h += 1


    v = []
    for a in range(0, i):
        u = []
        for b in range(0, j):
            e = k[h - 1][a][b]
            u.append(e)
        v.append(u)
    k.append(v)



    for a in range(1, i - 1):
        for b in range(1, j - 1):
            k[h][a][b] = (k[h][a + 1][b] + k[h][a - 1][b] + k[h][a][b + 1] + k[h][a][b - 1]) / 4 

    r = 0
    for a in range(1, i - 1):
        for b in range(1, j - 1):
            e = (k[h][a + 1][b] + k[h][a - 1][b] + k[h][a][b + 1] + k[h][a][b - 1]) / 4
            f = e - k[h][a][b]
            #print("Tiefe: ", h, " X-Achse: ", a, " Y-Achse: ", b, " Hoehe: " , k[h][a][b], " Abweichung: ", f)
            if f <= z and f >= -1*z:
                r += f

            else:
                r = p*i*j
    
            
            
            

else:
    
    print("Output (Berechnungstiefe: ", h," )")
    for a in range(0, i):
        for b in range(0, j):
            print("(", a + 1, ", ", b + 1, ") =", k[h][a][b])
    print("Output (Berechnungstiefe: ", h," )")

    

from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt


# imports specific to the plots in this example


wz = np.array(k[h])



import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data

# Twice as wide as it is tall.
fig = plt.figure()

#---- First subplot
ax = fig.add_subplot(1, 1, 1, projection='3d')
X = np.arange(0, i, 1)
Y = np.arange(0, j, 1)
X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y, wz, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0.1, antialiased=False)

#---- Second subplot

plt.show()




    
        