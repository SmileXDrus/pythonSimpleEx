from functools import partial, wraps, lru_cache
# docs: https://docs.python.org/3/library/functools.html?highlight=functools

power_of_2 = lambda x: pow(x, 2)
print(power_of_2(2))

p2 = partial(pow, exp=2)
print(p2(2), p2(3), p2(4))


def my_lru_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        try:
            return cache[args]
        except KeyError:
            pass
        res = func(*args)
        cache[args] = res
        return res

    return wrapper


# @lru_cache(maxsize=2048)  # хеширует данные, что позволяет не высчитывать по много раз одни и те же значения
@my_lru_cache
def fib(n):
    res = 1
    if n < 0:
        return None
    if n < 2:
        return res
    else:
        return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(100)])
