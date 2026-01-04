import time

def decorator(func):
    def f(N):
        time1 = time.time()
        func(N)
        print(f'Время выполнения функции: {time.time() - time1} секунд')
    return f


@decorator
def cycle(N):
    for i in range(N):
        x = 1


cycle(50)

@decorator
def printer(N):
    print(f'Число - {N}')

printer(50)