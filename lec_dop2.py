import random

def my_func(n, *lista):

    while True:
        is_not_in_list = True
        num = random.randint(0,n-1)
        for i in lista:            
            if num == i:
                is_not_in_list = False
        if is_not_in_list == True:
            break

    print(num)    

my_func(11, 3, 6, 5, 4, 1)