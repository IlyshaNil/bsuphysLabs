from math import sin
import matplotlib.pyplot as plt
import numpy as np


n = 1000
x = [0,]
y = [1,]
xkon = 0.5
xGraph = []
yGraph = []


def f(x, y):
    return 1 + 2.2 * sin(x) + 1.5 * y**2 


dx = (xkon-x[0])/n

for i in range(1, 4):
    x.append(0)
    y.append(0)
    k1 = f(x[i - 1], y[i - 1])
    k2 = f(x[i - 1] + dx / 3, y[i - 1] + dx / 3 * k1)
    k3 = f(x[i - 1] + 2 / 3 * dx, y[i - 1] - dx / 3 * k1 + dx * k2)
    k4 = f(x[i - 1] + dx, y[i - 1] + dx * k1 - dx * k2 + dx * k3)
    y[i] = y[i - 1] + dx / 8 * (k1 + 3 * k2 + 3 * k3 + k4)
    x[i] = x[0] + i * dx
    xGraph.append(x[i])
    yGraph.append(y[i])


plt.plot(np.array(xGraph), np.array(yGraph)) 

for i in range(3, n):
    x.append(0)
    y.append(0)
    x[i + 1] = x[0] + i * dx
    y[i + 1] = y[i] + dx / 24 * (55 * f(x[i], y[i]) - 59 * f(x[i - 1], y[i - 1]) + 37 * f(x[i - 2], y[i - 2]) - 9 * f(x[i - 3], y[i - 3]))
    xGraph.append(x[i + 1])
    yGraph.append(y[i + 1])


plt.plot(np.array(xGraph), np.array(yGraph)) #plt.plot(x, y) 
plt.grid()
plt.show()