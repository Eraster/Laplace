#https://www.google.ch/search?q=matplotlib%20animation&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:de:official&client=firefox-a&channel=np&source=hp#client=firefox-a&hs=4jz&rls=org.mozilla:de%3Aofficial&channel=np&biw=1366&bih=647&sclient=psy-ab&q=matplotlib+funcanimation&oq=matplotlib+func&gs_l=serp.3.0.0l2j0i30l2.25291.27343.0.29806.6.5.0.1.1.0.189.688.0j5.5.0....0...1c.1.19.psy-ab.JpS0kO7FiFA&pbx=1&bav=on.2,or.r_qf.&bvm=bv.48705608,d.bGE&fp=eee66d236af74eaf

from math import*
import numpy as np
#from random import*


Grafik = 1 #1 = 3d, 2 = 2D Hight, 3 = 2D Changing


i = 20 #randint(3, 25) # Werte in x Richtung
j = 20#randint(3, 25) # Werte in y Richtung

istart = 8 # 0 - i
iend = 11 # istart - i  

jstart = 8 # 0 - i
jend = 11 # istart - j

inter = 300 #fps in milliseconds

#maxinput = 100

repeat = 10000

konstant = 100

d = 1  #abstand

Genauigkeit = 0.001 #Abweichung der Annaeherung (average(i,j)-4*(i,j))
z = np.abs(Genauigkeit)


# Programmstart...

#p = maxinput #randint(5, maxinput) # randint maximum
#q = 0        #randint minimum

#----------

u = [] # u = j in der Liste
v = [] # v = i in der Liste
k = [] # Berechnungsschritt

ko = []
kons = []
konst = []

s = []
t = []
l = []

h = 0 # Automatische groesse zum Berechnungsschritt

r = z + 1 # Kontrollkonstante

#-----

for a in range(0, i):
    u = []
    konst = []
    for b in range(0, j):
        u.append(0)
        konst.append(0)
        s.append(0)
    v.append(u)
    kons.append(konst)
    t.append(s)
k.append(v)
ko.append(kons)
l.append(t)

kon = ko[0]

for a in range(istart, iend + 1):
    for b in range(jstart, jend + 1):
        kon[a][b] = konstant
        
#print("Input (Berechnungstiefe: 0 )")
#for a in range(0, i):
#    for b in range(0, j):
        #print("(", a + 1, ", ", b + 1, ") =", k[h][a][b])
        


#-----

while z < r and repeat > h :
    
    h += 1


    v = []
    t = []
    for a in range(0, i):
        u = []
        s = []
        for b in range(0, j):
            e = k[h - 1][a][b]
            ltd = l[h - 1][a][b]
            u.append(e)
            s.append(ltd)
        v.append(u)
        t.append(s)
    k.append(v)
    l.append(t)
    


    for a in range(1, i - 1):
        for b in range(1, j - 1):
            average = k[h-1][a + 1][b] + k[h-1][a - 1][b] + k[h-1][a][b + 1] + k[h-1][a][b - 1]          
            k[h][a][b] = (average + kon[a][b]*(d**2))/4
            
    print(np.max(k[h]))
    r = 0
    for a in range(1, i - 1):
        for b in range(1, j - 1):
            #e = (k[h][a + 1][b] + k[h][a - 1][b] + k[h][a][b + 1] + k[h][a][b - 1]) / 4
            #f = e - k[h][a][b]
            f = k[h - 1][a][b] - k[h][a][b]
            #print("Tiefe: ", h, " X-Achse: ", a, " Y-Achse: ", b, " Hoehe: " , k[h][a][b], " Abweichung: ", f)
            l[h][a][b] = f
            
            if f <= z and f >= -1*z:
                pass
            
            else:
                r = z + 1
                
    

else:   
    #print("Output (Berechnungstiefe: ", h," )")
    #for a in range(0, i):
    #    for b in range(0, j):
    #        print("(", a + 1, ", ", b + 1, ") =", k[h][a][b])
    print("Output (Berechnungstiefe: ", h," )")

    

"""
A very simple 'animation' of a 3D plot
"""


#3D Plot


if Grafik == 1:

    matplotlib.use('QT4agg')
    import matplotlib
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.animation as animation
    import time
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = range(0, i)
    ys = range(0, j)
    X, Y = np.meshgrid(xs, ys)
    
    wframes = []
    
    for rep in range(0, h, 10):
        
        wframe = ax.plot_surface(X, Y, np.array(k[rep]), rstride=1, cstride=1, cmap=cm.coolwarm,
            linewidth=0.1, antialiased=False)
        wframes.append([wframe])
    
    
    ani = animation.ArtistAnimation(fig, wframes, interval=inter, blit=True)
    plt.show()

    
    
if Grafik == 2:    
    
    """
    A very simple 'animation' of a 3D plot
    """
    import matplotlib
    matplotlib.use('QT4agg')
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.animation as animation
    import time
    
    ##Hight
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xs = range(0, i)
    ys = range(0, j)
    X, Y = np.meshgrid(xs, ys)
    
    wframes = []
    
    for rep in range(0, 300, 3):
        
        #wframe = ax.plot_surface(X, Y, np.array(k[rep]), rstride=1, cstride=1, cmap=cm.coolwarm,
        #    linewidth=0.1, antialiased=False)
        #wframes.append([wframe])
    
        wframe = plt.imshow(np.array(k[rep]))
        wframes.append([wframe])
    
    ani = animation.ArtistAnimation(fig, wframes, interval=500, blit=True)
    plt.show()



if Grafik == 3:
    
    """
    A very simple 'animation' of a 3D plot
    """
    import matplotlib
    matplotlib.use('QT4agg')
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.animation as animation
    import time    
    
    #Changing
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xs = range(0, i)
    ys = range(0, j)
    X, Y = np.meshgrid(xs, ys)
    
    wframes = []
    
    for rep in range(0, h, 50):
        
        #wframe = ax.plot_surface(X, Y, np.array(k[rep]), rstride=1, cstride=1, cmap=cm.coolwarm,
        #    linewidth=0.1, antialiased=False)
        #wframes.append([wframe])
    
        ar = np.array(l[rep])
    
    
        wframe = plt.imshow((ar), vmax=(z+3), vmin= (-1*z-3), interpolation = "nearest")
        wframes.append([wframe])
    
    ani = animation.ArtistAnimation(fig, wframes, interval=500, blit=True)
    plt.show()
    
else:
    pass






    
        
