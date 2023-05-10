from math import fabs, sqrt

from mathHelpers import dec, my_func


def fib(n):
    f1 = 1
    f2 = 1
    m = 0
    while m < n - 1:
        f = f1 + f2
        f1 = f2
        f2 = f
        m = m + 1
    return f1


goldenRat = (1.0 + sqrt(5)) / 2.0


def gold_section(point, a, b, eps, h):
    x, y = point[0], point[1]
    grad_x = (my_func(x + h, y) - my_func(x - h, y)) / (2 * h)
    grad_y = (my_func(x, y + h) - my_func(x, y - h)) / (2 * h)

    x1 = a + (b - a) / (dec(goldenRat) + 1)
    x2 = b - (b - a) / (dec(goldenRat) + 1)
    f_1 = my_func(x - grad_x * x1, y - grad_y * x1)
    f_2 = my_func(x - grad_x * x2, y - grad_y * x2)
    while fabs(b - a) > eps:
        if f_1 >= f_2:
            a = x1
            x1 = x2
            x2 = b - (b - a) / (dec(goldenRat) + 1)
            f_1 = f_2
            f_2 = my_func(x - grad_x * x2, y - grad_y * x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - a) / (dec(goldenRat) + 1)
            f_2 = f_1
            f_1 = my_func(x - grad_x * x1, y - grad_y * x1)
    return (a + b) / 2


def fibonacci(point, a, b, eps, h):
    x, y = point[0], point[1]
    k = 0
    n = 0
    fn1 = 1
    fn2 = 1
    dell = (b - a) / eps
    while fn1 < dell:
        fn = fn1 + fn2
        fn1 = fn2
        fn2 = fn
        n = n + 1
    x1 = a + dec(fib(n) / fib(n + 2)) * (b - a)
    x2 = a + dec(fib(n + 1) / fib(n + 2)) * (b - a)
    grad_x = (my_func(x + h, y) - my_func(x - h, y)) / (2 * h)
    grad_y = (my_func(x, y + h) - my_func(x, y - h)) / (2 * h)
    y1 = my_func(x - grad_x * x1, y - grad_y * x1)
    y2 = my_func(x - grad_x * x2, y - grad_y * x2)
    while fabs(b - a) > eps:
        k = k + 1
        if y1 >= y2:
            a = x1
            x1 = x2
            y1 = y2
            x2 = a + dec(fib(n - k + 2) / fib(n - k + 3)) * (b - a)
            y2 = my_func(x - grad_x * x2, y - grad_y * x2)
        else:
            b = x2
            x2 = x1
            y2 = y1
            x1 = a + dec(fib(n - k + 1) / fib(n - k + 3)) * (b - a)
            y1 = my_func(x - grad_x * x1, y - grad_y * x1)
    _x = (a + b) / 2
    return _x
