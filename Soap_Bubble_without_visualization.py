from math import*
from random import*

global k
global h



# Einstellungen

i = 20 #randint(3, 25) # Werte in x Richtung
j = 20 #randint(3, 25) # Werte in y Richtung

maxinput = 100

z = 0.001 #Abweichung der Annäherung (average(i,j)-4*(i,j))



# Programmstart...

p = maxinput #randint(5, maxinput) # randint maximum
q = 0        #randint minimum

#----------

u = [] # u = j in der Liste
v = [] # v = i in der Liste
k = [] # Berechnungsschritt



h = 0 # Automatische grösse zum Berechnungsschritt

r = p # Kontrollkonstante

#-----

for a in range(0, i):
    u = []
    for b in range(0, j):
        u.append(randint(q, p))
    v.append(u)
k.append(v)
        
print("Input (Berechnungstiefe: 0 )")
for a in range(0, i):
    for b in range(0, j):
        print("(", a + 1, ", ", b + 1, ") =", k[h][a][b])

#-----

while z*((i - 2)*(j - 2)) < r :
    
    h += 1

    for a in range(0, i):
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
            f = sqrt(e*e) - sqrt((k[h][a][b])*(k[h][a][b]))
            #print("Tiefe: ", h, " X-Achse: ", a, " Y-Achse: ", b, " Höhe: " , k[h][a][b], " Abweichung: ", f)
            if f <= z:
                r += f

            else:
                r = p*i*j
    
            
            
            

else:
    
    print("Output (Berechnungstiefe: ", h," )")
    for a in range(0, i):
        for b in range(0, j):
            print("(", a + 1, ", ", b + 1, ") =", k[h][a][b])
    print("Output (Berechnungstiefe: ", h," )")

# End




    
        
