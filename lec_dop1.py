import matplotlib.pyplot as plt
import numpy as np

A = 1
B = 1
a = 1
q1 = 0
q2 = np.pi 
b = 2
t = np.arange(0, 2*np.pi, 0.01)

x = A * np.sin(a * t + q1)
y = B * np.sin(b * t + q2)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('dop1.png')