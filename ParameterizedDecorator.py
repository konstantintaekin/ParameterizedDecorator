def compose(*funcs):
    def decorator(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            for fn in funcs:
                result = fn(result)
            return result
        return inner
    return decorator


def double_it(a):
    return a * 2


def increment(a):
    return a + 1


@compose(increment, increment, double_it)
def get_sum(*args):
    return sum(args)


print(get_sum(5))
print(get_sum(20, 10))
print(get_sum(5, 15, 25))