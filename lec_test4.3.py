import matplotlib.pyplot as plt
import numpy as np

phi = np.arange(0.01, 8*np.pi, 0.01)

k = 0.2

r = k / np.sqrt(phi)

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('test4.3.png')