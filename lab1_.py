import numpy as np
# выбор главного элемента
def bubble_max_row(m, col):
    max_element = m[col][col]
    max_row = col
    for i in range(col + 1, len(m)):
        if abs(m[i][col]) > abs(max_element):
            max_element = m[i][col]
            max_row = i
    if max_row != col:
        m[col], m[max_row] = m[max_row], m[col]


def solve_gauss(m):
    n = len(m)
    # прямой ход
    for k in range(n - 1):
        bubble_max_row(m, k)
        for i in range(k + 1, n):
            div = m[i][k] / m[k][k]
            m[i][-1] -= div * m[k][-1]
            for j in range(k, n):
                m[i][j] -= div * m[k][j]

    #######################треугольная матрица###################
    elm = 0 
    for elm in range(0,4):
       print(f'{m[elm]}') 
    ##################################################


    # обратный ход
    x = [0 for i in range(n)]
    #print(x)
    for k in range(n - 1, -1, -1):
        x[k] = (m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, n)])) / m[k][k]
        #print(x[k])

    # вывод результатов
    #print(x)
    return(x)


def is_singular(m):
    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False

m = [
    [2, -8, 5, -5, 147],
    [12, 13, -5, 10, -101],
    [-4, -11, 1, 11, -138],
    [5, -1, -6, -2, 26],
    
]

mLeft = [
    [2, -8, 5, -5],
    [12, 13, -5, 10],
    [-4, -11, 1, 11],
    [5, -1, -6, -2],
]
mRight = [
     147,
     -101,
     -138,
     26
]
A = np.array(mLeft)
B = np.array(mRight)
X = np.array(solve_gauss(m)) 
print(f'Вектор невязки: {B - A.dot(X)} \nОтвет: {X}')