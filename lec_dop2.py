import matplotlib.pyplot as plt
import numpy as np

phi = np.pi


def r_e_func():
    p1 = 2

    e1 = np.arange(0, 1, 0.1)

    r = p1 / (1 + e1 * np.cos(phi))

    plt.plot(e1, r)
    plt.axis('equal')
    plt.savefig('dop2_2.png')

r_e_func()


def r_p_func():
    e2 = 0.3

    p2 = np.arange(0, 10, 0.1)

    r = p2 / (1 + e2 * np.cos(phi))

    plt.plot(p2, r)
    plt.axis('equal')
    plt.savefig('dop2_2.png')

r_p_func()