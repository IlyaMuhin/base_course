import matplotlib.pyplot as plt
import numpy as np



def kus_func(a = 3, b = 8):
    x1 = np.arange(-10, a, 0.1)
    y1 = a**2 + x1 - x1
    plt.plot(x1, y1)
    plt.savefig('dop3.png')

    x2 = np.arange(a, b + 0.1, 0.1)
    y2 = x2**2
    plt.plot(x2, y2)
    plt.savefig('dop3.png')
    
    x3 = np.arange(b, 20, 0.1)
    y3 = b**2 + x3 - x3
    plt.plot(x3, y3)
    plt.savefig('dop3.png')

kus_func()