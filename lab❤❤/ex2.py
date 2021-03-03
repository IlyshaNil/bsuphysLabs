import numpy as np
import matplotlib.pyplot as plt


x = np.array([4.81, 5.05, 5.29, 5.53, 5.77, 6.01, 6.25])
y = np.array([-9.0821, -4.8035, -0.6962, 0.0295, 1.6033, 7.4974, 12.4176])
x1 = 4.8
x2 = 6.25


def sepDiff(x, y):
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1]) / float(x[i]-x[i-j])
    return np.array(a) # return an array of coefficient


def evalPoly(a, x, r):
    n = len(a) - 1
    temp = a[n] + (r - x[n])
    for i in range(n - 1, -1, -1):
        temp = temp * (r - x[i]) + a[i]
    return temp # return the y_value interpolation


def main(x1, x2):
    ynew = []
    xnew = []
    while (x1 <= x2):
        ynew.append(evalPoly(sepDiff(x, y), x, x1))
        xnew.append(x1)
        x1 += 0.01
    plt.plot(x, y, 'r', xnew, ynew)    
    plt.grid()
    plt.show()

main(x1, x2)
