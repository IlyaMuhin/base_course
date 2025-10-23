a = int(input())
b = int(input())
if a % b == 0:
    print("Первое число делится на второе")
    print(f'Остаток:{a % b}')
    print(f'a / b = {int(a / b)}')
else:
    print('Первое число не делится на второе')
    print(f'Остаток:{a % b}')
    print(f'a / b = {int(a / b)}')


