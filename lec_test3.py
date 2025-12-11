import matplotlib.pyplot as plt
import numpy as np


def ellips_plotter(x_start, x_finish, n):

    x = np.arange(x_start, x_finish, n)
    y = np.arange(x_start, x_finish, n)

    X, Y = np.meshgrid(x, y)

    fxy = (X**2) / 7 + (Y**2) / 3 - 1

    plt.contour(X, Y, fxy, levels = [0])
    plt.axis('equal')

    
    plt.savefig('fig_7.png')

if __name__ == '__main__':
    ellips_plotter(-10,10,0.5)
    
   

   