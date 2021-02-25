import numpy as np
import matplotlib.pyplot as plt


x=np.array([-0.4, -0.12, 0.16, 0.44, 0.72, 1.0, 1.28]) # создает NumPy массив значений из таблицы
y=np.array([0.7408, 0.5138, -0.6219, -0.6859, 0.3583, 0.7835, 0.2896])


def lagranz(x, y, f): # f - это х из блок-схемы
    P = 0
    for k in range(0, len(y)): #len(y) возвращает длину y 
        p1 = 1
        p2 = 1
        for i in range(0, len(x)):
            if i != k:                   # != не равно
                p1 = p1 * (f - x[i])           ############### МАГИЯ ################
                p2 = p2 * (x[i] - x[k])        ########### ЛАГРАНЖА #################
        P = P + y[k] * p1 / p2                 ############# *тут тоже* #############
    print(P)
    return P


xnew = np.linspace(np.min(x), np.max(x), 100) # numpy.linspace(start, stop, num=50) Функция linspace() возвращает одномерный массив из указанного количества элементов, 
#xnew = np.linspace(0.1, 0.5, 100)                                                    #значения которых равномерно распределенны внутри заданного интервала.
ynew = [lagranz(x, y, i) for i in xnew]  # конструкция y = [f(x, j, i) for i in collection]  - называется генератором.
#заполняет массив ynew = [] количеством элементов равным len(xnew), значение каждого из которых равно lagranz(x, y, i)

plt.plot(x, y, 'r', xnew, ynew)     #снача строит по точкам из таблицы, "r" - это тип red? потом второй график
plt.grid()
plt.show()