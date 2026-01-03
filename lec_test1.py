def logger(num):
    def f(func):
        def decorator(num2):
            print(int(num) + func(num2))
        return decorator
    return f
    




@logger(10)
def summa(num2):
    return num2

summa(10)