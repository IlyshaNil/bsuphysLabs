import math, numpy
import matplotlib.pyplot as plt


def dy1(x, b = 0.78):
    return(x / (b + x**2))


def dy0(x, a = 0.87):
    return(-(1 + math.cos(x)) / (math.sqrt(a**2 + x**2)))


def fy(x, a = 0.87):
    return(math.exp(-a * x**2))


def solution(dy1, dy0, fy):
    
    i = 0
    a = 0.87
    b = 0.78
    g1 = 1
    g2 = -0.5
    g3 = 1
    g4 = 4.50
    g5 = 0.3
    g6 = 4.7
    n = 1000
    yMax = 2


    y = [] 
    p = [] 
    q = [] 
    r = [] 
    k = [] 
    l = []

    dx = (b - a) / n
    for i in range(0, n+1):
        p.append(dy1(a + i * dx))
        q.append(dy0(a + i * dx))
        r.append(fy(a + i * dx))

    u = (dx**2 * q[0] - 2) * g2 + dx * (2 - dx * p[0]) * g1
    k.append((dx**2 * r[0] * g2 + dx * (2 - dx * p[0]) * g3) / u)
    l.append(2 * g2 / u)

    for i in range(0, n+1):
        u = 2 * dx**2 * q[i] - 4 - (2 - dx * p[i]) * l[i-1]
        k.append((2 * dx**2 * r[i] - (2-dx*p[i]) * k[i-1]) / u)
        l.append((2 + dx * p[i]) / u)

    xGraph = []
    for i in range(0, n+1):
        y.append(i)
        #print(y[i])
        xGraph.append(a + i*dx) 

    xGraph.reverse()
    jz = 0  

    y[n] = ((2 * dx * g6 + (k[n-1] - k[n] / l[n]) * g5) / (2 * dx * g4 + (l[n-1] - 1 / l[n]) * g5))
    for i in range(n-1, 0, -1):
        y[i] = k[i] - l[i] * y[i+1]
        jz +=1
        print(y[i])
    print(jz)

    xGraph = numpy.linspace(a, b, len(y))  
    yGraph = numpy.array(y)  

    plt.plot(numpy.array(xGraph), yGraph)    
    plt.grid()
    plt.show()


solution(dy1, dy0, fy)




    


