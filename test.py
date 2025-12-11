import time

general_list = []

for i in range(10**5):
    general_list.append(i)

def my_func(a):
    return 2 * a**2 + 3 * a

time2 = time.time()
list2 = (my_func(num) for num in general_list)
print(f'Время списк.вкл. = {time.time() - time2}')