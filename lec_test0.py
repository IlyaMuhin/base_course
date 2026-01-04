import time

def timer(func):
    def f(N):
        time1 = time.time()
        func(N)
        print(f'Время выполнения функции: {time.time() - time1} секунд')
    return f


@timer
def cycle(N):
    for i in range(N):
        x = 1


cycle(50)

@timer
def printer(N):
    print(f'Число - {N}')

printer(50)