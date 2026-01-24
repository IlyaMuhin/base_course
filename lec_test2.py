try:
    n = int(input('Введите число: '))
    if n<1 or n>100:
        raise ValueError('ты ДАУН')
    print('ты ДАУН')
    
except ValueError as e:
    print(e, 'ты ДАУН')
