def decorator(func):
    print('Hello World!')
    return func

@decorator
def decorate_example():
    print("Привет Вселенная!")

decorate_example()


#Другое объявление декоратора
decorate_example = decorator(decorate_example)
decorate_example()