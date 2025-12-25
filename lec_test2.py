import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


phi = 2


def circle_move(R):
    alpha = np.arange(0, 2 * np.pi, 0.1)
    # R = phi * t
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([],[], '-', color = 'r', label = 'Ball')


frames = 180
coords = np.zeros((frames, 2))


def animate(i):
    R = phi * i
    ball.set_data(circle_move(R = R))
    return ball

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames = frames, interval = 50)
ani.save('test2.gif', writer = 'pillow')