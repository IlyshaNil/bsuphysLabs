import math, numpy
import matplotlib.pyplot as plt


def dy1(x, b = 0.78):
    return(x / (b + x**2))


def dy0(x, a = 0.87):
    return(-(1 + math.cos(x)) / (math.sqrt(a**2 + x**2)))


def fy(x, a = 0.87):
    return(math.exp(-a * x**2))

i = 0
n = 0
x0 = 0

a = 0.87
b = 0.78    
g1 = 1
g2 = -0.5
g3 = 1
g4 = 4.50
g5 = 0.3
g6 = 4.7
h = 0.001

k = []
l = []
y = []

x0 = a
n = round(abs((b - a)) / h)

for i in range(1, n+2):
    k.append(i)
    l.append(i)
    y.append(i)

#print(k)

k[0] = (h**2 * g2 + h * (2-h*dy1(x0))*g3) / (g2 * (h**2 * dy0(x0) - 2) + h * (2 - h * dy1(x0))*g1)
l[0] = 2 * g2 / (g2*(h**2 * dy0(x0)-2) + h * (2-h*dy1(x0))*g1)

i = 0
for i in range(1, n):
    x0 = x0 + h
    k[i] = (h**2 * 2 * fy(x0) - (2 - h * dy1(x0)) * k[i-1]) / (h**2 * dy0(x0) * 2 -4 -(2 - h*dy1(x0))*l[i-1])
    l[i] = (2+h*dy1(x0)) / (2 * h**2 * dy0(x0) - 4 - (2 - h * dy1(x0)) * l[i-1])

y[n] = (2*h*g6 + (k[n-1]-k[n]/l[n]) * g5) / (2*h*g4 + (l[n-1]-1/l[n])*g5)
for i in range(n-1, 0, -1):
    y[i] = k[i] - l[i] * y[i+1]

xGraph = numpy.linspace(a, b, len(y)-1)  
yGraph = numpy.array(y[1:])  
print(yGraph)

plt.plot(numpy.array(xGraph), yGraph)    
plt.grid()
plt.show()