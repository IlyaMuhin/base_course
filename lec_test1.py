import numpy as np
len1 = int(input('Введите количество элементов: '))
a = np.zeros((len1))
for i in range(len1):
    a[i] = int(input(f'Введите {i+1} число:'))


def middle(a):
    sum = 0
    for x in range(len1):
        sum+=a[x]
    print(sum / len1)

middle(a)

