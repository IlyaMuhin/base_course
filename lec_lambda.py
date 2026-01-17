def sum_arg(a, b): #Именованная функция
    return a + b

# print(sum_arg(12, 25))

#lambda аргумент1, аргумент2, и т.д. : выражениеб используемые аргументы

sum_arg = lambda a, b: a + b #Анонимная функция

args = [(1,2), (3,5)]

a_list = [lambda a, b: f'a: {b**2}' for _ in range(100)]

print(a_list[99](1, 5))