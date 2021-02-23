import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


#eps = np.finfo(float).eps 
# The difference between 1.0 and the next smallest representable float larger than 1.0. 
# For example, for 64-bit binary floats in the IEEE-754 standard, eps = 2**-52, approximately 2.22e-16.
#тип программная погрешность - оч маленькая
eps = 0.000000000000001 # ввожу погрешность ручками

plotX = [] #
plotY = [] # инициализирую два списка, чтобы хранить координаты точек графика


def f(x):
    return sqrt(2 + x) + sqrt(3 + x) - 5 * (x**2 - 2)**3  #захардкодил исходныую функцию


def df(x):
    return (1/2*sqrt(x + 3)) + (1/2*sqrt(2 + x)) - 30 * x * (x**2 - 2)**2 #захардкодил первую производную исходной фукнции 

# реализация метода Ньютона
def newton(f, df, x, eps):
    f1 = f(x) #рассчет начальной точки
    iteration = 0 #счетчик итераций
    while abs(f1) > eps and iteration < 1000000: #работа метода будет продолжатьсядо достижения необходимой точности, или до достижения лимита итераций
        try:                                     #конструкция try - except используется для обработки исключений. После try пишется "опасный" код, который может вызвать ошибку
            x = x - f1 / df(x)                   #формула метода ньютона
        except ZeroDivisionError as errorMessage:            #эта строка ловит ошибки класса ZeroDivisionError из блока try и записывает системный комментарий ошибки в errorMessage
            print(f'Деление на ноль ({errorMessage})')      # f-строка)))
            break                                #принудительный выход из цикла
        f1 = f(x)  #меняем значение f1 для следующего цикла
        iteration += 1
    print(x, iteration)
    return x  

def mainLoop(x0, xn, delta):  #функция, которая прогоняет все x через функцию newton
    point = x0    
    while (point < xn):
        print(f'ТОЧКА: {point}')
        solve = newton(f, df, point, eps)
        if solve > 0: plt.scatter(solve, point)          
        plotX.append(point)
        plotY.append(f(point))     
        point += delta

    
print(f'Точность: {eps}\n')          

solve = mainLoop(0.1, 2, 0.1)
plt.plot(plotX, plotY)
plt.hlines(0, 0, 2)
plt.grid()
plt.show()


class ParabolicMethod:
    def parabolic(f, df, x, eps, delta):
        xn1 = f(x)
        xn = f(x + 2*delta)
        xn_1 = f(x + delta)
        xn_2 = f(x)

        iteration = 0
        while abs(xn1) > eps and iteration < 1000000:
            xn1 = parabolicFirst(xn, xn_1, xn_2, f) + parabolicSecond(xn, xn_1, xn_2, f) + parabolicThird(xn, xn_1, xn_2, f)
            xn_2 = xn_1
            xn_1 = xn
            xn = xn1
            iteration += 1

        return xn1

    def parabolicFirst(xn, xn_1, xn_2, f):
        chislitel = f(xn_1) * f(xn)
        znam = (f(xn_2) - f(xn_1)) * (f(xn_2) - f(xn))
        return (chislitel / znam) * xn_2

    def parabolicSecond(xn, xn_1, xn_2, f):
        chislitel = f(xn_2) * f(xn)
        znam = (f(xn_1) - f(xn_2)) * (f(xn_1) - f(xn))
        return (chislitel / znam) * xn_1

    def parabolicThird(xn, xn_1, xn_2, f):
        chislitel = f(xn_2) * f(xn_1)
        znam = (f(xn) - f(xn_2)) * (f(xn) - f(xn_1))
        return (chislitel / znam) * xn