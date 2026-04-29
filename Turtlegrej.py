import math as meth
import random
from Turtletest import *
"""laddaturtle()"""
t=turtle.Turtle()
t.speed(9940)
def hörnfram(sida):
    t.forward(120)
    t.right(90)

def rita_cirkel(radie):
    t.penup()
    t.forward(radie)
    t.right(90)
    t.pendown()
    for i in range(360):
        t.forward(2*radie*3.14159265/360)
        t.right(1)

def mönster_rund():
    for i in range(60):
        rita_cirkel(random.randint(5,120))
        t.right(90)
        t.forward(random.randint(60,100))

t.color("blue")
mönster_rund()


turtle.done()