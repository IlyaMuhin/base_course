import numpy as np
from lec_test_const import g
x0 = 5
y0 = 7
v0x = 2
v0y = 3
a = np.zeros((5, 3))
print(a)
for i in range(5):
    a[i, 0] = i + 1
for x in range(5):
    a[x, 1] = x0 + v0x * (x + 1)
for y in range(5):
    a[y, 2] = y0 + v0y * (y + 1) - (g * (y+1)**2)/2
print(a)