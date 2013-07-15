#https://www.google.ch/search?q=matplotlib%20animation&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:de:official&client=firefox-a&channel=np&source=hp#client=firefox-a&hs=4jz&rls=org.mozilla:de%3Aofficial&channel=np&biw=1366&bih=647&sclient=psy-ab&q=matplotlib+funcanimation&oq=matplotlib+func&gs_l=serp.3.0.0l2j0i30l2.25291.27343.0.29806.6.5.0.1.1.0.189.688.0j5.5.0....0...1c.1.19.psy-ab.JpS0kO7FiFA&pbx=1&bav=on.2,or.r_qf.&bvm=bv.48705608,d.bGE&fp=eee66d236af74eaf

import math as math
import random as random


# Einstellungen

i = 20 #randint(3, 25) # Werte in x Richtung
j = 20#randint(3, 25) # Werte in y Richtung

maxinput = 100

maxtiefe = 300

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

while z*((i - 2)*(j - 2)) < r and h < maxtiefe :
    
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
            k[h][a][b] = (k[h-1][a + 1][b] + k[h-1][a - 1][b] + k[h-1][a][b + 1] + k[h-1][a][b - 1]) / 4 

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
    
    print("Output (Berechnungstiefe: ", h + 1," )")
    for a in range(0, i):
        for b in range(0, j):
            print("(", a + 1, ", ", b + 1, ") =", k[h][a][b])
    print("Output (Berechnungstiefe: ", h + 1," )")


    
xwerte = []
zwerte = []

for l in range(0, h+1):
    xwertezwischen = []
    zwertezwischen = []
    for m in range(0, i):
        awert = k[l][m][int(j/2)]
        xwertezwischen.append(awert)
        
        
        zwertezwischen.append(m)
        
    xwerte.append(zwertezwischen) #ueberskreuz
    zwerte.append(xwertezwischen)
        
              
        

#"""
#Matplotlib Animation Example
#
#author: Jake Vanderplas
#email: vanderplas@astro.washington.edu
#website: http://jakevdp.github.com
#license: BSD
#Please feel free to use and modify this, but keep the above information. Thanks!
#"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, j), ylim=(0, maxinput))
line, = ax.plot(xwerte[0], zwerte[0], lw=1)

# initialization function: plot the background of each frame
def init():
    line.set_data(xwerte[0], zwerte[0])
    return line,

# animation function.  This is called sequentially
def animate(w):
    
    line.set_data(xwerte[w], zwerte[w])
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=h, interval=100, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=2, extra_args=['-vcodec', 'libx264'])

plt.show()




    
        
