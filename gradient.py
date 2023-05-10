from math import fabs

import numpy as np
from matplotlib import pyplot as plt

from mathHelpers import dec, my_func
from methods import gold_section, fibonacci

h = dec(0.000001)


def gradient_descent_const(eps, point):
    next_point = point.copy()
    count = 0
    points_x = []
    points_y = []
    e = dec(0.01)
    while True:
        count += + 1
        points_x.append(next_point[0])
        points_y.append(next_point[1])
        f = my_func(point[0], point[1])
        grad_x = (my_func(point[0] + h, point[1]) - my_func(point[0] - h, point[1])) / (2 * h)
        grad_y = (my_func(point[0], point[1] + h) - my_func(point[0], point[1] - h)) / (2 * h)
        next_point[0] = point[0] - e * grad_x
        next_point[1] = point[1] - e * grad_y
        f_next = my_func(next_point[0], next_point[1])
        if fabs(point[0] - next_point[0]) <= eps and fabs(point[1] - next_point[1]) <= eps and fabs(f - f_next) <= eps:
            break
        point = next_point.copy()
    draw(-10, 10, my_func, points_x, points_y, 'Gradient with constant method')
    print('gradient_descent_const', 'func_value = ', my_func(point[0], point[1]), 'x = ', point[0], ' y = ', point[1], 'iterations =  ', count)


def gradient_descent_golden(eps, point):
    next_point = point.copy()
    count = 0
    points_x = []
    points_y = []
    while True:
        count = count + 1
        points_x.append(next_point[0])
        points_y.append(next_point[1])
        f = my_func(point[0], point[1])
        grad_x = (my_func(point[0] + h, point[1]) - my_func(point[0] - h, point[1])) / (2 * h)
        grad_y = (my_func(point[0], point[1] + h) - my_func(point[0], point[1] - h)) / (2 * h)
        gold_ratio = gold_section(point, dec(-8), dec(8), eps, h)
        next_point[0] = point[0] - gold_ratio * grad_x
        next_point[1] = point[1] - gold_ratio * grad_y
        f_next = my_func(next_point[0], next_point[1])
        if fabs(point[0] - next_point[0]) <= eps and fabs(point[1] - next_point[1]) <= eps and fabs(f - f_next) <= eps:
            break
        point = next_point.copy()
    draw(-10, 10, my_func, points_x, points_y, 'Gradient with Golden ration method')
    print('gradient_descent_golden:', 'func_value = ', my_func(point[0], point[1]), 'x = ', point[0], ' y = ', point[1], 'iterations =  ', count)


def gradient_descent_fibonacci(eps, point):
    next_point = point.copy()
    count = 0
    points_x = []
    points_y = []
    while True:
        count = count + 1
        f = my_func(point[0], point[1])
        points_x.append(next_point[0])
        points_y.append(next_point[1])
        fib = fibonacci(point, dec(-8), dec(8), eps, h)
        grad_x = (my_func(point[0] + h, point[1]) - my_func(point[0] - h, point[1])) / (2 * h)
        grad_y = (my_func(point[0], point[1] + h) - my_func(point[0], point[1] - h)) / (2 * h)
        next_point[0] = point[0] - fib * grad_x
        next_point[1] = point[1] - fib * grad_y
        f_next = my_func(next_point[0], next_point[1])
        if fabs(point[0] - next_point[0]) <= eps and fabs(point[1] - next_point[1]) <= eps and fabs(f - f_next) <= eps:
            break
        point = next_point.copy()
    draw(-10, 10, my_func, points_x, points_y, 'Gradient with Fibonacci method')
    print('gradient_descent_fibonacci:', 'func_value = ', my_func(point[0], point[1]), 'x = ', point[0], ' y = ', point[1], 'iterations =  ', count)


def gradient_crushed_step(eps, point):
    next_point = point.copy()
    count = 0
    alfa = dec(0.1)
    points_x = []
    points_y = []
    while True:
        count = count + 1
        points_x.append(next_point[0])
        points_y.append(next_point[1])
        f = my_func(point[0], point[1])
        grad_x = (my_func(point[0] + h, point[1]) - my_func(point[0] - h, point[1])) / (2 * h)
        grad_y = (my_func(point[0], point[1] + h) - my_func(point[0], point[1] - h)) / (2 * h)
        f_next = my_func(point[0] - alfa * grad_x, point[1] - alfa * grad_y)
        if f_next < f:
            next_point[0] = point[0] - grad_x * alfa
            next_point[1] = point[1] - grad_y * alfa
        else:
            alfa = dec(alfa/2)
            next_point[0] = point[0] - grad_x * alfa
            next_point[1] = point[1] - grad_y * alfa
        if fabs(point[0] - next_point[0]) <= eps and fabs(point[1] - next_point[1]) <= eps and fabs(f - f_next) <= eps:
            break
        point = next_point.copy()
    draw(-70, 70, my_func, points_x, points_y, 'Gradient with level sets method')
    print('gradient_crushed_step:', 'func_value = ', my_func(point[0], point[1]), 'x = ', point[0], ' y = ', point[1], 'iterations =  ', count)


def draw(a, b, func, points_x, points_y, title):
    fig, ax = plt.subplots()
    x, y = np.mgrid[a:b:100j, a:b:100j]
    ax.contour(x, y, func(x, y), levels=100, colors='skyblue')
    ax.set_title(title)
    for i in range(len(points_x)):
        ax.scatter(points_x[i], points_y[i], c='black')
    ax.plot([points_x[i] for i in range(len(points_x))], [points_y[i] for i in range(len(points_y))], c='black')
    plt.show()


def draw_func(func, a, b):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    x, y = np.mgrid[a:b:100j, a:b:100j]
    ax.contour(x, y, func(x, y), levels=100, colors='firebrick')
    plt.show()
