a = int(input())
b = int(input())
if b != 0 and a % b == 0:
    print("Первое число делится на второе")
    print(f'Остаток:{a % b}')
    print(f'a / b = {int(a / b)}')
elif b == 0:
    print('На ноль делить нельзя!')
else:
    print('Первое число не делится на второе')
    print(f'Остаток:{a % b}')
    print(f'a / b = {int(a / b)}')


