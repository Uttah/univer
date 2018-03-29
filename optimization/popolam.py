import math

def fx(x):
    return 3 * x ** 2 - (7/x)

def midle(a,b):
    return b - a

def midle_int(iter):
    a = int(input("Левая граница интервала -  "))
    b = int(input("Правая граница интервала - "))
    xm = (a + b) / 2
    for i in range(iter):
        x1 = a + midle(a,b)/4
        x2 = b - midle(a,b)/4
        if fx(x1) < fx(x2):
            b = xm
            xm = x1
            midle(a, b)
        else:
            if fx(x2) < fx(xm):
                a = xm
                xm = x2
            else:
                a = x1
                b = x2
                midle(a, b)
        print(x1, " ", x2)
    return midle(a,b)

kolvo = int(input("Введите количество итераций "))
midle_int(kolvo)