import math
choice_list = {1:"Круг", 2:'Прямоугольник', 3:'Треугольник'}
choice = int(input(f'Выберите фигуру - {choice_list}: '))
if choice == 1:
    r = int(input('Введите радиус круга: '))
elif choice == 2:
    a1 = int(input('Введите первую сторону прямоугольника: '))
    a2 = int(input('Введите вторую сторону прямоугольника: '))
elif choice == 3:
    b1 = int(input('Введите первую сторону треугольника: '))
    b2 = int(input('Введите вторую сторону треугольника: '))
    b3 = int(input('Введите третью сторону треугольника: '))
def S(s_circ = 0,s_cube = 0,s_triangle = 0):
    if choice == 1:
        s_circ = 3.14 * r**2
        print(s_circ)
        
    elif choice == 2:
        s_cube = a1 * a2
        print(s_cube)
        
    elif choice == 3:
        if b1 > (b2 + b3) or b2 > (b3 + b1) or b3 > (b1 + b2):
            print('Такого треугольника не существует')
        else:
            s_triangle = math.sqrt(((b1+b2+b3)/2)*((b1+b2+b3)/2-b1)*((b1+b2+b3)/2-b2)*((b1+b2+b3)/2-b3))
            print(int(s_triangle))
    
S()
