# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:14:42 2013

@author: Jonas
"""

import numpy as np


n = 18
a = np.array(np.zeros((n,n)))
len = np.alen(a)
l = float(len)

dk = (l-1)/2-0.1

for i in range(0, len):
    for j in range(0, len):
        dx = ((l-1)/2-i)**2
        dy = ((l-1)/2-j)**2
        dis = sqrt(dx+dy)
        
        if dis < dk:
            a[i][j] = 1
        else:
            a[i][j] = 0





#n = 4
#a = np.zeros((n, n))
#l = np.alen(a)
#bb = 0*a
#
#print(l)
#
#for i in range(l):
#    for j in range(l):
#        b = sqrt(i+j)
#        bb[i][j]= b
#        if b < ((l-1)/2)-0.1:
#            a[i][j] = 1
#        else:
#            a[i][j] = 0
#
#print(bb)        
#print(a)
#print(bb[0][0])
