"""
Lesson about funcs
iterators, generators, comprehensions
"""

from operator import mul
from time import time
from functools import wraps, reduce


def secondary():
    print("Secondary")


def add(a, b):
    # return a + b
    print("Add", a, b)
    res = a + b
    print("Result:", res)
    return res


def div(a, b):
    """
    Divide a by b
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return
    return a / b


def demo_lines():
    multiline = """Zero line
    First line
    Second line
    12345678'''''"asd""
    """

    online = "line1\nline2"
    print(multiline)
    print(online)


def power(a, p=2):
    return a ** p


def greet(name="World"):
    print("Hello", name)


def multiply_lines(input_line, times, lines=None):
    if lines is None:
        lines = {}
        # print('id of dict:', id(lines))
    for i in range(1, times + 1):
        lines[i] = input_line * i
    return lines


def my_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0
    while start < end:
        yield start
        start += step


def main():
    print('Hello main!')
    greet('John')
    # lines = multiply_lines('foo', 5)
    lines = multiply_lines('foh', 3)
    print(lines)
    print('Получение через список:', count_values(power, 1, 2, 3, 4, as_list=True))
    print('Получение через словарь:', count_values(power, 1, 2, 3, 4))
    ran = my_range(4, 10, 2)
    print(next(ran))
    print(next(ran))
    print(list(ran))


def count_values(counter, *args, as_list=False):
    print(args)
    d = {}
    if as_list:
        return [counter(v) for v in args]
    return {v: counter(v) for v in args}
    # return [


main()


def time_func(func, *args):
    start_time = time()
    print('times:', start_time)
    res = func(*args)
    end_time = time()
    print('time_after:', end_time)
    print('compused in', end_time - start_time)
    return res


def timing_dec(func):
    @wraps(func)
    def wrapper(*args):
        return time_func(func, *args)

    return wrapper


@timing_dec
def power_2(a, p=2):
    return a ** p


def demo_decorators():
    res = time_func(power, 10_534, 1654)
    print(res)


print(power_2(2, 44))

'''
def fact(fac):
    value = list(range(1, fac + 1))
    if fac > 1:
        print(reduce(mul, value))
    else:
        print(1)

fact(0)

def fact_(fac):
    res = 1
    if fac > 1:
        for i in range(1, fac+1):
            res *= i
    print(res)
fact_(5)'''
