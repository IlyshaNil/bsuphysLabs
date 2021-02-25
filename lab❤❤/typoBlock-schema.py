import numpy as np
import matplotlib.pyplot as plt


x=np.array([-0.4, -0.12, 0.16, 0.44, 0.72, 1.0, 1.28], dtype=float)
y=np.array([0.7408, 0.5138, -0.6219, -0.6859, 0.3583, 0.7835, 0.2896], dtype=float)


def lagranz(x,y,t):
    P = 0
    w1 = 0.0
    w2 = 0.0
    w = 0.0
    for k in range(0, len(y)):
        w = 1
        for i in range(0, len(x)):
            if i != k: 
                w1 = (t - x[i])
                w2 = (x[i] - x[k])
                w = w * (w1 / w2) 
        P += w

    return P


xnew=np.linspace(np.min(x),np.max(x),100)
ynew=[lagranz(x,y,i) for i in xnew]
plt.plot(x,y,'go',xnew,ynew)
plt.grid(True)
plt.show()
print(lagranz(x, y, 0.1))