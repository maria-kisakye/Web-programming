import math
from turtle import *

def hearta(t):
    return 15 * math.sin(t) ** 3

def heartb(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

speed(0)
bgcolor("black")

for i in range(10000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    goto(x, y)
    for j in range(5):
        color("#ff7487")
        goto(x, y)

done()