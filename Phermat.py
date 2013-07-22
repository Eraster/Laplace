from numpy import zeros, amax, amin
import numpy as np

def Mask(c):
    
    a = 0*c
    len = np.alen(a)
    l = float(len)
    
    dk = (l-1)/2-0.01
    
    for i in range(0, len):
        for j in range(0, len):
            dx = ((l-1)/2-i)**2
            dy = ((l-1)/2-j)**2
            dis = sqrt(dx+dy)
            
            if dis < dk:
                a[i][j] = 1
            else:
                a[i][j] = 0
                
    return a

def Laplace(m):
    
    Genauigkeit = 0.001
    z = np.abs(Genauigkeit)    
    delta = 2    
    repeat = 10000
    
    mas = Mask(m)
    
    konstant = ((1*m)*delta**2)/4    
    kd = 0*m
    k = []
    k.append(kd)
    
    h = 0        
    r = z + 1

    while z < r and repeat > h :
        
        h += 1        
        kd = k[h - 1]
        average = 1*kd
        average[1:-1, 1:-1] = (kd[0: -2, 1: -1] + kd[2:, 1: -1] + kd[1: -1, 0: -2] + kd[1: -1, 2:])/4
        kd = (average + konstant)*mas
        k.append(kd)
    
        if  amax(k[h] - k[h-1]) <= z and amin(k[h] - k[h-1]) >= -1*z:
            r = 0                
        else:
            r = z + 1
                
    return kd
    
def Phermat(m):
    
    place = Laplace(m)
    xlen = float(len(place))
    ylen = float(len(place))
    xy = 0*place
    
    
    for i in range(len(place)):
        for j in range(len(place[0])):
            xy[i][j] = (xlen/2-i)**2+(ylen/2-j)**2
    
    pherma = place + xy
    
    return pherma
    
    
    
    
ma = zeros((100,100), float)
#l = zeros((7, 7), float)
#l = l + float(100)
#ma[60: 67, 55: 62] = l
ma[45: 50, 30: 70] = 10
#for i in range(100):
#    for j in range(100):
#        ma[i][j] = ((i-30)**2+(j-40)**2)
        
h = Phermat(ma)




#"""
#A very simple 'animation' of a 3D plot
#"""
#import matplotlib
#matplotlib.use('QT4agg')
#from mpl_toolkits.mplot3d import axes3d
#import matplotlib.pyplot as plt
#import numpy as np
#import matplotlib.animation as animation
#import time
#
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#xs = range(20)
#ys = range(20)
#X, Y = np.meshgrid(xs, ys)
#
#wframes = []
#
#for rep in range(1):
#    
#    wframe = ax.plot_surface(X, Y, np.array(k[0]), rstride=1, cstride=1, cmap=cm.coolwarm,
#        linewidth=0.1, antialiased=False)
#    wframes.append([wframe])
#
#
#ani = animation.ArtistAnimation(fig, wframes, interval=1000, blit=True)
#plt.show()

import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
import matplotlib.pyplot as plt

# Twice as wide as it is tall.
fig = plt.figure()

#---- First subplot
ax = fig.add_subplot(1, 1, 1, projection='3d')


X = np.arange(0, 100, 1)
Y = np.arange(0, 100, 1)
X, Y = np.meshgrid(X, Y)

plt.axis('equal')

surf = plt.contour(X, Y, h,150,rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0.1, antialiased=False)

#---- Second subplot

plt.show()


            
            
    
    
