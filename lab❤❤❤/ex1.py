import math
from math import sqrt


def f(xk):
    return (2 * abs(xk) * math.tan(xk)) / (4 - sqrt(1 - sqrt(abs(xk))))


def gauss():
    n = 10 
    solve = 0
    a = math.pi / n
    for i in range(1, n):
        xk = math.cos((2 * (i - 1) * math.pi) / (n * 2))
        solve += a * f(xk)
    solve = solve / 2
    return solve

print(gauss())
