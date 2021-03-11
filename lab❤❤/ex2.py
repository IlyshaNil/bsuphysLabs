import numpy as np
import matplotlib.pyplot as plt


x = np.array([4.81, 5.05, 5.29, 5.53, 5.77, 6.01, 6.25]) #ввод х
y = np.array([-9.0821, -4.8035, -0.6962, 0.0295, 1.6033, 7.4974, 12.4176]) #ввод значений функции
x1 = 4.8 #левая граница интервала
x2 = 6.25 #правая граница интервала


def sepDiff(x, y): #Заполнение таблицы 1 разделенных разностей
    n = len(x) #количество узлов
    a = [] #массив коэффициентов разделенных разностей
    for i in range(n): #заполнение массива а элементами массива у
        a.append(y[i])

    for j in range(1, n): # ЦИКЛ МАГИИ НЬЮТОНА
        for i in range(n-1, j-1, -1): # ЦИКЛ ПОДМАГИИ НЬЮТОНА
            a[i] = float(a[i]-a[i-1]) / float(x[i]-x[i-j]) #вставляем значения х и у 
                                                            #в магическую формулу
    return np.array(a) #возвращаем массив коэффициентов 


def evalPoly(a, x, r): #Вычисление значения интерполяционного 
                        #полинома по формуле
    n = len(a) - 1
    p = a[n] + (r - x[n])
    for i in range(n - 1, -1, -1): 
        p = p * (r - x[i]) + a[i]
    return p #возврат интерполированного значения функции


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
