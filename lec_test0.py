import time

def decorator(func):
    def f(N):
        time1 = time.time()
        func(N)
        print(time.time() - time1)
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