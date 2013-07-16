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
    
    
