import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def circle_move(angle_vel, time):
    e = 2.7
    alpha = angle_vel * np.pi / 180 * time
    x = np.sin(alpha) * (e**np.cos(alpha) - 2 * np.cos(4 * alpha) + np.sin(alpha / 12)**5)
    y = np.cos(alpha) * (e**np.cos(alpha) - 2 * np.cos(4 * alpha) + np.sin(alpha / 12)**5)
    return x, y

fig, ax = plt.subplots()
# ball, = plt.plot([], [], 'o', color = 'r', label = 'Ball')
ball_line, = plt.plot([], [], '-', color = 'r', label = 'Ball')

frames = 180
coords = np.zeros((frames, 2))


def animate(i):
    coords[i] = circle_move(angle_vel = 2, time = i)
    # ball.set_data([coords[i][0]], [coords[i][1]])
    ball_line.set_data(coords[:i, 0], coords[:i, 1])
    return  ball_line

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


ani = FuncAnimation(fig, animate, frames = frames, interval = 30)
ani.save('test3.1.gif', writer = 'pillow')