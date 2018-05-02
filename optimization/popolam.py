import math

def fx(x):
    return x*x*x + 8*x*x + x +5

def midle(a,b):
    return b - a

def value_func(a,b):
    return (b - a) / 2
    #return fx(x_avg)

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
        print("Итерация №{}: интервал - [{}, {}], значение X - {}".format(i+1, x1, x2, value_func(x1,x2)))
    return midle(a,b)

kolvo = int(input("Введите количество итераций "))
midle_int(kolvo)
