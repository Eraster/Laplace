from numpy import zeros
import numpy as np


def Laplace (m):
    
    Genauigkeit = 0.001
    z = np.abs(Genauigkeit)
    
    delta = 1
    
    repeat = 10000
    
    konstant = (1*m)*delta*delta
    
    kd = 0*m
    k = []
    k.append(kd)
    
    h = 0
    

    while z < r and repeat > h :
        
        h += 1
        
        kd = k[h - 1]
        average = k[0: -2, 1: -1] + k[2:, 1: -1] + k[1: -1, 0: -2] + k[1: -1, 2:]
        kd[1:-1, 1:-1] = (average + konstant)/4
        
        k.append(kd)
    
        if  amax(k[h] - k[h-1]) <= z and amin(k[h] - k[h-1]) >= -1*z:
            r = 0
                
            else:
            r = z + 1
                
    else:
        return kd







    
        
