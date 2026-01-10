import numpy as np


class Number:
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return Number(self.data + other)
    


a = Number(12)
c = Number(4)
b = a + 5
print(b.data)



a = 'Good'
b = [1, 4, 6]
c = 3
d = 4.3
e = np.zeros(5)
f = {'a':4, 'b':5}
g = (1, 6, 7)
def fun():
    pass
class A:
    pass
aA = A()

print(dir(dir(dir(dir))))
# print()        
# print(dir(aA))
# print()        
# print(dir(fun))