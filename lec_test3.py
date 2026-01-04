import functools



def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args,**kwargs):
        args_repr = [str(a) for a in args]
        kwargs_repr = [f'{k} = {v}' for k,v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Вызовем функцию {func.__name__}({signature})')
        value = func(*args, **kwargs)
        print(f'Функцию {func.__name__} вернула значение {value}')
        return value
    
    return wrapper_debug

def my_func(num):
    return num**2 - 2

debug_my_func = debug(my_func)


# @debug
# def debug_factorial():
#     return math.factorial


def show_debug_function(terms = 5):
    return [debug_my_func(n) for n in range(terms + 1)]

show_debug_function()