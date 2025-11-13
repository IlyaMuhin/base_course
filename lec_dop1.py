import numpy as np
a = np.zeros((2, 3))
b = np.zeros((2, 3))
c  = np.zeros((2, 3))
for i in range(2):
    for x in range(3):
        a[i, x] = int(input("Введите число для первого массива: "))
        c[i, x] = a[i, x]
for j in range(2):
    for y in range(3):
        b[j, y] = int(input("Введите число для второго массива: "))
        if c[j, y] < b[j, y]:
            c[j, y] = b[j, y]
print(f'Первый массив:\n{a}')
print(f'Второй массив:\n{b}')
print(f'Третий массив:\n{c}')

