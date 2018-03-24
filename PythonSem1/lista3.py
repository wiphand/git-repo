import re
from turtle import fd, bk, lt, rt, pu, pd, speed, fillcolor,begin_fill,end_fill

speed('fastest')

def kwadrat(bok):
  for i in range(4):
    fd(bok)
    rt(90)

def rozeta(N, a, b):
  for i in range(N):
    fd(b)
    kwadrat(a)
    bk(b)
    rt (360 / N)
    
def wzorek():
  for i in range(100):
    kwadrat(20 + i)
    rt(4)
    pu()
    fd(12)
    pd()


def turtleParty(size, depth):
    
    for i in range(depth):
        change = 0.05*size
        for i in range(4):
            fd(size)
            rt(90)
        pu()
        fd(change)
        rt(90)
        fd(change)
        lt(90)
        pd()
        size = size - 0.10*size
        

def spirala(wysokosc):
    color = 1
    for z in range(int(wysokosc/2)):
        for j in range(2):
            for k in range(2):
                for i in range(wysokosc+1):
                    
                    fillcolor(1,0.01*color,0.3)
                    begin_fill()
                    kwadrat(20)
                    end_fill()
                    fd(20)
                    color +=1
                lt(180)
                fd(20)
                rt(90)
            
            wysokosc=wysokosc-2

spirala(9)
x = input('Nacisnij cos, prosze')


"""
def turtleParty(size, depth):
    for i in range(depth):
        for i in range(4):
            turtle.Turtle.fd(size)




turtleParty(10,4)
"""