import matplotlib.pyplot as plt
import numpy as np

a = -0.5
b = 0.5

dx = 0.01

x0 = 0
y0 = 0.4


def f(x, y):
    return (2 * x**2) + (3 * y**2)


def rungeKutta(x0, y0, f):
    k1 = f(x0, y0)
    k2 = f(x0 + dx * 1/3, y0 + 1/3 * dx * k1)
    k3 = f(x0 + dx * 2/3, y0 - 1/3 * dx * k1 + dx *k2)
    k4 = f(x0 + dx, y0 + dx * k1 - dx * k2 + dx * k3)
    y0 = y0 + dx * (1/8 * k1 + 3/8 * k2 + 3/8 * k3 + 1/8 * k4)
    return x0, y0


def main(f, rungeKutta, x0 = 0, y0 = 0.4, a = -0.5, b = 0.5, dx = 0.001):
    solve = (0,)
    x = []
    y = []

    while (x0) >= a:
        solve = rungeKutta(x0, y0, f)
        print(solve)
        x.append(solve[0])
        y.append(solve[1])
        x0 -= dx


    while (x0) <= b:
        solve = rungeKutta(x0, y0, f)
        print(solve)
        x.append(solve[0])
        y.append(solve[1])
        x0 += dx

    plt.plot(np.array(x), np.array(y)) 
    plt.grid()
    plt.show()

#print(rungeKutta(x0, y0, f))
main(f, rungeKutta)