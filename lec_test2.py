try:
    n = int(input('Введите число: '))
    if n<1 or n>100:
        raise ValueError('ты ДАУН')
    print('Число корректно')

    
except ValueError as e:
    print(e)

def guess(min, max):
    if max - min == 2 or max - min == 0:
        print(f'Ваше число - {min + 1}')
    else:
        print(f'Ваше число меньше {int((min + max)/2)}?')
        choice = input()
        if choice == 'Да':
            max = int((min + max)/2) - 1
        elif choice == 'Нет':
            min = int((min + max)/2)
            print(f'Ваше число больше {int((min + max)/2)}?')
            choice = input()
            if choice == 'Да':
                min = int((min + max)/2) + 1
            elif choice == 'Нет':
                max = int((min + max)/2)
        guess(min, max)

guess(0,100)

             


    


