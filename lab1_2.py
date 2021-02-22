import numpy as np
from math import sqrt


#eps = np.finfo(float).eps
eps = 0.0000001
print(f'Точность: {eps}\n')

def f(x):
    return sqrt(2 + x) + sqrt(3 + x) - 5 * (x**2 - 2)**3


def df(x):
    return (1/2*sqrt(x + 3)) + (1/2*sqrt(2 + x)) - 30 * x * (x**2 - 2)**2


def newton(f, df, x, eps):
    f1 = f(x)
    iteration = 0
    while abs(f1) > eps and iteration < 1000000:
        try:
            x = x - f1 / df(x)
            print(x)
        except ZeroDivisionError as err:
            print(f'Деление на ноль ({err})')
            break
        
        f1 = f(x)
        iteration += 1
    return x


def interval(x0, xn, delta):
    point = x0
    
    while (point < xn):
        print(f'ТОЧКА: {point}')
        solve = newton(f, df, point, eps)
        point += delta
              

#solve = interval(1, 2, 0.001)

solve = newton(f, df, 2, eps)
print(solve)
