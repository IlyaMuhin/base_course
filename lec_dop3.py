import numpy as np
stroki = int(input('Введите количество строк: '))
stolbs = int(input("Введите количество столбцов: "))
massive = np.zeros((stroki, stolbs))
for i in range(stroki):
    for x in range(stolbs):
        massive[i, x] = int(input(f"Введите число: "))
print(massive)
max_list = []
max = -1
for i in range(stolbs):
    for y in range(stroki):
        for x in range(stroki):
            if massive[x, i] > max:
                max = massive[x, i]
    max_list.append(int(max))
    max = -1
print(max_list)
