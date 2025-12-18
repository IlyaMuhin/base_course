import matplotlib.pyplot as plt
import numpy as np

phi = np.arange(0, 8*np.pi, 0.01)

p = 2

e = 0.5

r = p/(1 + e * np.cos(phi))

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('dop2.png')