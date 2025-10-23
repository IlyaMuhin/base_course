a = int(input())
b = int(input())
c = int(input())
D = b ** 2 - 4 * a * c
if D < 0:
    print('У уравнения нет корней')
elif D == 0:
    print(int((-b + D ** 0.5) / (2 * a)))
else:
    print(int((-b + D ** 0.5) / (2 * a)))
    print(int((-b - D ** 0.5) / (2 * a)))
