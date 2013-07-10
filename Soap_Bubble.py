from math import*
from random import*

#-------------------------------------------------------------

i = 3 # Werte in x Richtung
j = 3 # Werte in y Richtung

p = 100 # randint maximum
q = 0 # randint minimum

z = 0.1 # Abweichung der Annäherung average(n)-4*n

u = [] # u = j in der Liste
v = [] # v = i in der Liste
k = [] # Berechnungsschritt

h = 0 # Automatische grösse zum Berechnungsschritt

r = p # Kontrollkonstante

#-------------------------------------------------------------

for a in range(0, i):
    u = []
    for b in range(0, j):
        u.append(randint(q, p))
    v.append(u)
k.append(v)

print(k)
        
print("Input")
for a in range(0, i):
    for b in range(0, j):
        print("(", a + 1, ", ", b + 1, ") =", k[h][a][b])

#-------------------------------------------------------------

while r > z :

    h += 1

    #print("k = ", h)

    for a in range(0, i):
        for b in range(0, j):
            e = k[h - 1][a][b]
            u.append(e)
        v.append(u)
    k.append(v)



    for a in range(1, i - 1):
        for b in range(1, j - 1):
            k[h][a][b] = (k[h][a + 1][b] + k[h][a - 1][b] + k[h][a][b + 1] + k[h][a][b - 1]) / 4 
            #print(k[h][c][d])

    r = 0
    for a in range(1, i - 1):
        for b in range(1, j - 1):
            e = (k[h][a + 1][b] + k[h][a - 1][b] + k[h][a][b + 1] + k[h][a][b - 1]) / 4
            f = sqrt(e*e)- sqrt(k[h][a][b]*k[h][a][b])
            r = r + f
    r = r/((i-2)*(j-2))
            
            

else:
    print("Berechnungstiefe: ", h)
    for a in range(0, i):
        for b in range(0, j):
            print("(", a + 1, ", ", b + 1, ") =", k[h][a][b])
    
            



    
        
