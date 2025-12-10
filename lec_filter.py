names = ["John", "David", "Maria", "Richard"]
ages = [16, 25, 19, 41]


def checker(user):
    name, age = user
    return age > 21


users = list(zip(names, ages))
canDrinkAlcohol = list(filter(checker, users))
print(canDrinkAlcohol)