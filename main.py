from numpy.ma import array
from gradient import *
from conjugateGradient import conjugate_gradient


def main():
    e = dec(0.0001)
    x = array([dec(-10), dec(10)])
    draw_func(my_func, -100, 100)
    gradient_descent_const(e, x)
    gradient_crushed_step(e, x)
    gradient_descent_golden(e, x)
    gradient_descent_fibonacci(e, x)
    x = array([-4, 3])
    '''A = array([[2, 1],
         [1, 4]])
    b = array([0, 0])'''
    '''A = array([[2, 0],
               [0, 2]])
    b = array([-1, 0])
    conjugate_gradient(x, A, b, e)'''


main()
