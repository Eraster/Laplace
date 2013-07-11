speed(0)
hideturtle()

screen = getscreen()
screen.tracer(True)

#-------------------------------------------------------------

global xhome
global yhome

xhome = -300
zhome = -250

home = (xhome, zhome)

global xline
global yline
global zline

xline = 400
yline = 250
zline = 300

global zmax

zmax = maxinput

global ax
global ay

ax = i - 1 #Anzahl x Werte -1
ay = j - 1 #Anzahl y Werte -1

global xyangle

xyangle = 45 #degrees

#-------------------------------------------------------------

def zpoint(x, y, zk): 
    xstartup = (x/ax)*xline
    yxstartup = (y/(i-1))*yline*cos(xyangle*(pi/180))
    zstartup = (zk/zmax)*zline
    yzstartup = (y/(j-1))*yline*sin(xyangle*(pi/180))

    cor = (xstartup + yxstartup  + xhome,  zstartup + yzstartup + zhome ) 
    print(zstartup + yzstartup + zhome)
    return cor
           
#-------------------------------------------------------------

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
        
               

#-------------------------------------------------------------

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

#-------------------------------------------------------------

update()
hideturtle()
exitonclick()



