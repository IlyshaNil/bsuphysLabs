from math import sin, cos, pi
import numpy as np 
import matplotlib.pyplot as plt


def fmu1(t):  #U(0,t)
    return 1


def fmu2(t):  #U(1,t)
    return -cos(2*pi*t)


def fi(x):   #U(x,0)
    return 1-x


def psi(x):  #dU(x,0)/dt
    return sin(pi*x) + 1/3 * sin(2*pi*x)


h = 0.1
tau = 0.05
tmin = 0
xmin = 0
tmax = 10
xmax = 1
a = 3


m = round((xmax - xmin) / h)
n = round((tmax - tmin) / tau)


alpha = (3*tau/h)**2

u = np.zeros((n+1, m+1))
x = np.zeros(n+1)
t = np.zeros(m+1)
k = np.zeros(n+1)
l = np.zeros(n+1)

for i in range(0, m+1): t[i] = tmin + tau * i
for j in range(0, n+1): x[i] = xmin + h * j

j = 0
for j in range(1, m):
    u[0, j+1] = fmu1(t[j+1])
    u[n, j+1] = fmu2(t[j+1])

i = 0
for i in range(0, n+1):
    u[i, 0] = fi(x[i])
    u[i, 1] = u[i, 0] + tau * psi(x[i])

i = 0; j = 0
for j in range(1, m):
    for i in range(1, n):
        u[i, j+1] = alpha * (u[i+1,j] + u[i-1,j]) + 2*(1-alpha) * u[i,j] - u[i,j-1]

xGraph = []
yGraph = []
xGraph1 = []
yGraph1 = []
for i in range(0, n+1):
    xGraph.append(x[i])
    yGraph.append(u[i,0])
    xGraph1.append(x[i])
    yGraph1.append(u[i,m])


plt.plot(np.array(xGraph), np.array(yGraph), np.array(xGraph1), np.array(yGraph1))    
plt.grid()
plt.show()
