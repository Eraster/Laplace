# -*- coding: utf-8 -*-

from math import*
from random import*
from turtle import*

speed()

hideturtle()

screen = getscreen()
screen.tracer(False)

#----------

global xhome
global yhome

global xline
global yline
global zline

global zmax

global ax
global ay

global xyangle

#-----

global k
#global h

#-------------------------------------------------------------

# Einstellungen

i = 20 #randint(3, 25) # Werte in x Richtung
j = 20 #randint(3, 25) # Werte in y Richtung

maxinput = 100

Abweichung = 0.001 #Abweichung der Annäherung (average(i,j)-4*(i,j))

#-----

xhome = -300
zhome = -250

xline = 400
yline = 250
zline = 300

xyangle = 45 #degrees


#-------------------------------------------------------------

# Programmstart...

p = maxinput #randint(5, maxinput) # randint maximum
q = 0        #randint minimum

#-----

home = (xhome, zhome)

zmax = p

ax = i - 1 #Anzahl x Werte -1
ay = j - 1 #Anzahl y Werte -1

#----------

u = [] # u = j in der Liste
v = [] # v = i in der Liste
k = [] # Berechnungsschritt



h = 0 # Automatische grösse zum Berechnungsschritt

z = Abweichung * Abweichung

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
            f = (e-k[h][a][b])*(e-k[h][a][b])
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

#----------

def zpoint(x, y, zk): 
    xstartup = (x/ax)*xline
    yxstartup = (y/(i-1))*yline*cos(xyangle*(pi/180))
    zstartup = (zk/zmax)*zline
    yzstartup = (y/(j-1))*yline*sin(xyangle*(pi/180))

    cor = (xstartup + yxstartup  + xhome,  zstartup + yzstartup + zhome ) 

    return cor
           
#-----

for a in range(0, i):
    for b in range(0, j):

        middle = zpoint(a, b, k[h][a][b])

        pu()
        goto(middle)
        pd()

        if a == ax:
           pass
           
        else:
            c = zpoint(a + 1, b, k[h][a + 1][b])
            goto(c)
            goto(middle)

        if b == ay:
           pass
           
        else:
            d = zpoint(a, b + 1, k[h][a][b + 1])
            goto(d)
            goto(middle)
           
        pu()        
        
               

#-----

pu()
goto(home)
pd()
fd(xline)
left(xyangle)
fd(yline)
left(90-xyangle)
fd(zline)
right(90-xyangle)
bk(yline)
left(90-xyangle)
bk(zline)
fd(zline)
right(90)
bk(xline)
left(90)
bk(zline)
fd(zline)
right(90-xyangle)
fd(yline)
left(90-xyangle)
bk(zline)
right(90-xyangle)
bk(yline)
fd(yline)
right(xyangle)
fd(xline)
left(90)
fd(zline)
right(90)
bk(xline)

#---------------

hideturtle()
update()
exitonclick()





    
        
