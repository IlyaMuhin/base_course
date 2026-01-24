def gen_sqrt(num):
    yield num**2
num = gen_sqrt(5)
print(next(num))