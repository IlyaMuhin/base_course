def decorator(func):
    def f(num1, num2, sign):
        if sign == '+':
            print(f'{num1} + {num2} = {num1 + num2}')
        elif sign == '-':
            print(f'{num1} - {num2} = {num1 - num2}')
        elif sign == '*':
            print(f'{num1} * {num2} = {num1 * num2}')
        elif sign == '/':
            print(f'{num1} / {num2} = {num1 / num2}')
    return f
    

@decorator
def two_variables(num1, num2, sign):
    return num1, num2, sign


two_variables(8,5,'+')
    
    