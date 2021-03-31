import math
import numpy as np 
import matplotlib.pyplot as plt


tau = 0.001
h = 0.1
xmin = 0
xmax = 1
tmin = 0
tmax = 1


def fmu1(t):
    return 0.4


def fmu2(t):
    return 1.2 * t


def fi(x):
    return (x + 0.4) * math.cos((math.pi * x) / 2)


def f(x):
    return 0.3 * (x*x + 1)


def aSqrt(x):
    return 1/2


n = round((xmax - xmin) / h)
m = round((tmax - tmin) / tau)

u = np.zeros((n+1, m+1))
x = np.zeros(n+1)
#print(x[0])
t = np.zeros(m+1)
k = np.zeros(n+1)
l = np.zeros(n+1)


for i in range(1, n+1):
    x[i] = xmin + h * i
    u[i, 0] = fi(x[i])


for i in range(1, m+1):
    t[i] = tmin + tau * i
    u[0, i] = fmu1(t[i])
    u[n, i] = fmu2(t[i])


for j in range(1, m+1):
    k[0] = (u[0,j-1]/tau + f(x[0])) / (2*aSqrt(x[0])/h**2+1/tau)
    l[0] = -aSqrt(x[0])/(h**2 * (2 * aSqrt(x[0])/h**2+1/tau))
    for i in range(1, n):
        k[i] = (-u[i,j-1]/tau-f(x[i])-aSqrt(x[i])*k[i-1]/h**2)/(-(2*aSqrt(x[i])/h**2+1/tau)-aSqrt(x[i])*l[i-1]/h**2)
        l[i] = (aSqrt(x[i])/h**2)/(-(2*aSqrt(x[i])/h**2+1/tau)-aSqrt(x[i])*l[i-1]/h**2)


for i in range(n-1, 1, -1):
    u[i,j] = k[i]-l[i]*u[i+1,j]

plt.plot(x, u)    
plt.grid()
plt.show()
          
