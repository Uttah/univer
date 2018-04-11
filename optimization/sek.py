import math

def fx(x):
    return 3 * x ** 2 - (7/x)

def fx1(x):
    return 6 * x - (7/x ** 2)

def fx2(x):
    return 6 - (7/x ** 3)

def sek(iter):
    new_list = []
    a = int(input("Левая граница интервала:  "))
    b = int(input("Правая граница интервала: "))
    x1 = float(input("Введите x1: "))
    eps = float(input("Введите погрешность: "))
    for i in range(iter):
        xn = b - fx(b) * ((x1 - b)/(fx(x1) - fx(b)))
        if math.fabs(xn - x1) < eps:
            print("Погрешность превышена!!!")
            break
        x1 = xn
        print("Итерация №{}: x = {}, y = {}".format(i+1, xn, fx(xn)))
        new_list.append(fx(xn))
    return new_list

kolvo = int(input("Укажите количество итераций - "))
tmp = sek(kolvo)
print("Минимальное значение функции: {}".format(min(tmp)))