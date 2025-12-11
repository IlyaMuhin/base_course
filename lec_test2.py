import matplotlib.pyplot as plt
import numpy as np

def hyperbola_plotter(x_start, x_finish, n):
    x = np.arange(x_start, x_finish, n)
    y = 1/x
    plt.plot(x, y, label = 'my hyperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('Hyperbola plotter')
    plt.legend()
    # plt.axis('equal')

    plt.savefig('fig_6.png')


if __name__ == '__main__':
    hyperbola_plotter(-10,10,0.5)

