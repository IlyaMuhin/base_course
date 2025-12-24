import matplotlib.pyplot as plt
import numpy as np

def cicloid_plotter(R = 3):
    alpha = np.arange(-10 * np.pi, 10 * np.pi, 0.1)

    x = R * (alpha - np.sin(alpha))
    y = R * (1 - np.cos(alpha))

    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('test1.png.png')

if __name__ == '__main__':
    cicloid_plotter()


