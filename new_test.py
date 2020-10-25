def ras(x, y):
    """function for x - y"""
    return x - y


def dev(x, y):
    '''Эта функция делить значение переменной x на значение переменной y'''
    return x / y


def printf(string):
    string = input()
    return string 


def add(x, y):
    """Not add function"""
    z = lambda p: p**p
    return z(4)


def mult(x, y):
#Функция умножения
    return x * y


def fact(x):
#Функция факториала
    if x==0:
        return 1
    return x * fact(x-1)


def F(n):
    """"simple recurcia"""
    if n == 1:
        return 1
    return n + F(n-1)


def main():
    print("Hello,world!")
    pass
