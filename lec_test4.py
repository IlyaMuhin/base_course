a = int(input('Введите натуральное число:'))
a1 = 1
a2 = 1
b = 0
for i in range(1, a+1):
    if i == 1:
        print(a1, end = " ")
    elif i == 2:
        print(a2, end = " ")
    else:
        c = a1 +a2
        print(c, end = ' ')
        a1 = a2
        a2 = c

    
