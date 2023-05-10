import decimal


def dec(x):
    return decimal.Decimal(x)


def my_func(x, y):
    # return x ** 2 + y ** 2 - x
    return (2 * x + 5) ** 2 + (3 + y) ** 2 - 3 * x * y
    # return x ** 2 + y ** 2 + x * y + 2 * y
