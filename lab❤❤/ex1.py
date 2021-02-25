import numpy as np
import matplotlib.pyplot as plt


x=np.array([-0.4, -0.12, 0.16, 0.44, 0.72, 1.0, 1.28])
y=np.array([0.7408, 0.5138, -0.6219, -0.6859, 0.3583, 0.7835, 0.2896])


def lagranz(x, y, f):
    P = 0
    for k in range(0, len(y)):
        p1 = 1
        p2 = 1
        for i in range(0, len(x)):
            if i != k: 
                p1 = p1 * (f - x[i])
                p2 = p2 * (x[i] - x[k])
        P = P + y[k] * p1 / p2
    print(P)
    return P


xnew = np.linspace(np.min(x), np.max(x), 100)
#xnew = np.linspace(0.1, 0.5, 100)
ynew = [lagranz(x, y, i) for i in xnew]
plt.plot(x, y, 'r', xnew, ynew)
plt.grid()
plt.show()