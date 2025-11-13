import numpy as np
a = np.zeros((7))
print(a)
for i in range(7):
    a[i] = int(input(f'Введите {i+1} число: '))
print(a)
pos = int(input('Введите позицию нового числа: '))
pos1 = 6
num = int(input('Введите новое число: '))
for x in range(7-pos):
    a[pos1] = a[pos1 - 1]
    pos1-=1
a[pos - 1] = num
print(a) 


