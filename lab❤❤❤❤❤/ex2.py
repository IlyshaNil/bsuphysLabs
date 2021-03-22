import math, numpy
import matplotlib.pyplot as plt



n = 10

def bottomBorder(x):
    return(-1 /(x**2 + 1))


def topBorder(x):
    return(-3/(x**2 + 9))


def leftBorder(y):
    return(-1 / y)


def rightBorder(y):
    return(-y /(y**2 + 1))


e = 0.1
a1 = 0
a2 = 1
b1 = 1
b2 = 3

h = (a2 - a1) / n
l = (b2 - b1) / n
t = h**2 / l**2

u = numpy.zeros((n+1, n+1))

i = 0
for i in range(0, n+1):
    x = a1 + i * h
    u[0,i] = bottomBorder(x)
    u[n,i] = topBorder(x)
    
    y = b1 + i * l
    u[i,0] = leftBorder(y)
    u[i,n] = rightBorder(y)

i = 0
M = 0
while(M < e):
    M = 0
    for i in range(1, n):
        for j in range(1, n):
            R = u[i,j]
            u[i,j] = (u[i+1,j] + u[i-1,j] + t * (u[i, j+1] + u[i, j+1])) / (2 + 2 * t)

            if (M < abs(u[i,j] - R)): M = abs(u[i,j] - R)

#numpy.set_printoptions(precision=2, suppress=True)
print(u)