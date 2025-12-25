import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def circle_move(angle_vel, time):
    e = 2.7
    alpha = angle_vel * np.pi / 180 * time
    x = 16 * np.sin(alpha)**3
    y = 13 * np.cos(alpha) - 5 * np.cos(2 * alpha) - 2 * np.cos(3 * alpha) - np.cos(4 * alpha)
    return x, y

fig, ax = plt.subplots()
ball_line, = plt.plot([], [], '-', color = 'r', label = 'Ball')

frames = 180
coords = np.zeros((frames, 2))


def animate(i):
    coords[i] = circle_move(angle_vel = 2, time = i)
    ball_line.set_data(coords[:i, 0], coords[:i, 1])
    return  ball_line

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


ani = FuncAnimation(fig, animate, frames = frames, interval = 30)
ani.save('test3.2.gif', writer = 'pillow')