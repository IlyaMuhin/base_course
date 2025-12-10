import numpy as np

list1 = []
list2 = []
list3 = []


massive_poz = 0

n = int(input('Введите количество элементов в массивах: '))

for i in range(n):
    massive_poz += 1
    list1.append(int(input(f'1 массив, {massive_poz} число: ')))

massive_poz = 0


for i in range(n):
    massive_poz += 1
    list2.append(int(input(f'2 массив, {massive_poz} число: ')))

massive_poz = 0


for i in range(n):
    massive_poz += 1
    list3.append(int(input(f'3 массив, {massive_poz} число: ')))

massive_poz = 0


massive1 = np.array(list1)
massive2 = np.array(list2)
massive3 = np.array(list3)

max_massive = max([max(massive1), max(massive2), max(massive3)])
print(max_massive)

sum_massive = sum(massive1) + sum(massive2) + sum(massive3)
print(sum_massive)