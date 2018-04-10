import math

def fx(x):
    return x*x*x + 8*x*x + x +5

def fx1(x):
    return 3*x*x + 16*x + 1

def cas(iter):
    x1 = float(input("Введите x1 - "))
    eps = float(input("Введите погрешность - "))
    for i in range(iter):
        xn = x1 - (fx(x1)/fx1(x1))
        if (math.fabs(xn - x1) < eps) or \
            (math.fabs(fx1(xn))) < eps:
            print("Погрешность превышена!!!")
            break
        x1 = xn
        print("Итерация №{}: x = {}, y = {}".format(i+1, xn, fx(xn)))

kolvo = int(input("Укажите количество итераций - "))
cas(kolvo)