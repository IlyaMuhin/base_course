import numpy as np
import lec_test_const as const
h = 100
a = np.radians(45)
b = np.radians(35)
v = np.sqrt((const.g * h * (np.tan(b))**2)/(2 * (np.cos(a))**2 * (1 - np.tan(b) * np.tan(a))))
print(v)
N = (2 / np.sqrt(round(np.pi, 2))) * np.sqrt(const.h) * (const.k * 200)**(3 / 2) * (const.e1**(300 / const.k * 200 )) * 300**(200 / 2)
print(N)
