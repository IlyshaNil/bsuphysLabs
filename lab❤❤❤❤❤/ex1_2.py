import math, numpy
import matplotlib.pyplot as plt


def dy1(x, b = 0.78):
    return(x / (b + x**2))


def dy0(x, a = 0.87):
    return(-(1 + math.cos(x)) / (math.sqrt(a**2 + x**2)))


def fy(x, a = 0.87):
    return(math.exp(-a * x**2))


def main(dy1, dy0, fy):
    i = 0
    a = 0.87
    b = 0.78
    g1 = 1
    g2 = -0.5
    g3 = 1
    g4 = 4.50
    g5 = 0.3
    g6 = 4.7
    n = 100
    h = 0.1
    yMax = 2


    y = [] 
    p = [] 
    q = [] 
    r = [] 
    k = [0,0] 
    l = [0,0]

    x0 = a
    n = round((b - a) / h);
    for i in range(0, n+1):
        k.append(dy1(a+h*i))
        l.append(dy0(a+h*i))
        y.append(fy(a+h*i))
    print(k)

    k[0] = (h * h * g2 + h * (2 - h * dy1(x0)) * g3) / (g2 * (h * h * dy0(x0) - 2) + h * (2 - h * dy1(x0)) * g1)
    l[0] = 2 * g2 / (g2 * (h * h * dy0(x0) - 2) + h * (2 - h * dy1(x0)) * g1)
    for i in range(0, n+1):
        x0 += h
        k[i] = (h*h*2*fy(x0)-(2-h*dy1(x0))*k[i-1])/(h*h*dy0(x0)*2-4-(2-h*dy1(x0))*l[i-1])
        l[i] = (2+h*dy1(x0))/(2*h*h*dy0(x0)-4-(2-h*dy1(x0))*l[i-1])
    
    #y[n] = (2*h*g6+(k[n-1]-k[n]/l[n])*g5)/(2*h*g4+(l[n-1]-1/l[n])*g5)
    for i in range(n-1, 1, -1):
        y[i] = k[i]-l[i]*y[i+1]


    x0 = a
    xGraph = []
    yGraph = numpy.array(y)

    for i in range(1, n+1):
        xGraph.append(x0)
        x0 += h

    plt.plot(numpy.array(xGraph), yGraph)    
    plt.grid()
    plt.show()
  
main(dy1, dy0, fy)
