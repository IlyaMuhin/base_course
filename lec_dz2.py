a=int(input())
b=int(input())
c=int(input())
if a>=b+c or b>=a+c or c>=a+b:
    print('Треугольник не существует')
else:
    print("Треугольник существует")
    if a==b==c:
        print('Треугольник равносторонний')
    elif a==b!=c or b==c!=a or c==a!=b:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')

