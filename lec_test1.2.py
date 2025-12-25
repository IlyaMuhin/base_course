import matplotlib.pyplot as plt
import numpy as np

def astroid_plotter(R = 10):
    alpha = np.arange(-3 * np.pi, 3 * np.pi, 0.1)

    x = R * np.cos(alpha)**3
    y = R * np.sin(alpha)**3

    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('test1.2.png')

if __name__ == '__main__':
    astroid_plotter()