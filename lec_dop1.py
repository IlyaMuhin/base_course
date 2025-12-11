import time

general_list = []

for i in range(10**5):
    general_list.append(i)

def my_func(a):
    return 2 * a**2 + 3 * a


time1 = time.time()
list1 = list(map(my_func, general_list))
print(f'Время map = {time.time() - time1}')


time2 = time.time()
list2 = [my_func(num) for num in general_list]
print(f'Время списк.вкл. = {time.time() - time2}')


time3 = time.time()
list3 = []
for i in range(len(general_list)):
    list3.append(my_func(general_list[i]))
print(f'Время цикла = {time.time() - time3}')