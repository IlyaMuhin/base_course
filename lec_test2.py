import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def circle_move(t,alpha):
    phi = np.arange(0, 2 * np.pi, 0.1)
    R = alpha + t
    x = R * np.cos(phi)
    y = R * np.sin(phi)
    return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color = 'r', label = 'Ball')


frames = 180
coords = np.zeros((frames, 2))


def animate(i):
    ball.set_data(circle_move(t = i, alpha = 0.1))
    return ball
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames = 100, interval = 10)
ani.save('test_2.gif', writer = 'pillow')