from math import *
import scipy.integrate as spi 
import numpy as np


def f(x): return 1/(1 + sqrt(log(x)))


def simpson(f, a = 2.0, b = 4.0, n = 10):
    h = (b - a) / n
    k = 0.0
    x = a + h
    for i in range(1, int(n / 2) + 1):
        k += 4 * f(x)
        x += 2 * h
    x = a + 2 * h
    for i in range(1, int(n / 2)):
        k += 2 * f(x)
        x += 2 * h
    return (h / 3) * (f(a) + f(b) + k)


def scipyCheck(f, n = 10):
    x = np.linspace(2, 4, num = n)
    y = []
    for elm in range(0, len(x)):
        y.append(f(x[elm]))
    solve = spi.simps(np.array(y), x)
    return(solve)

print(f'Solve: {simpson(f)} \nSciPy: {scipyCheck(f)} \nR: {abs(scipyCheck(f) - simpson(f))}')    

