import matplotlib.pyplot as plt
import numpy as np

phi = np.arange(0, 8*np.pi, 0.01)

k = 0.159

r = k * phi

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('test4.2.png')