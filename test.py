def ras(x, y):
    return x - y


def dev(x, y):
    return x/y


def add(x, y):
    return x + y


def mult(x,y):
    return x*y


def maine_funk():
    print('wunderbar')

def fact(x):
#Функция факториала
    return x*fact(x-1)





def fact(x):
#Функция факториала
    if x==0:
        return 1
    return x * fact(x-1)


def main():
    pass