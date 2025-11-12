import numpy as np
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
trigonometry_array = np.zeros((n, m))
for i in range(n):
    if i == n:
        break
    for j in range(m):
        if j == m:
            break
        trigonometry_array[i, j] = np.sin(n * i + m * j + 1)
print(trigonometry_array)


