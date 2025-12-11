import time

m = int(input('Введите число M: '))
n = int(input('Введите число N: '))

for i in range(m+1):
    print(i)
    for x in range(n+1):
        time.sleep(1)
        print(f'\t {x}')
    time.sleep(1)
