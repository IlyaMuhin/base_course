import numpy as np
a,b = map(float, input('Введите промежуток: ').split(' '))
n = int(input('Введите количество точек: '))
def func(massive = np.linspace(a,b,n)):
    for i in range(len(massive)):
        massive[i] **= 2
    return massive

tmp = func()
print(f'Функция y = x**2 на заданном промежутке:{tmp}')
    
 