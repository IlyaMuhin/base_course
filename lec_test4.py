import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def frac_func(x0 = 0.1, y0 = 0.1, C = 0.3, D = 0.33):
    x = x0**2 - y0**2 + C
    y = 2 * x0 * y0 + D
    return x, y 

fig, ax = plt.subplots()
points, = plt.plot([], [], 'o', color = 'r', label = 'Ball')


frames = 180
coords = np.zeros((frames, 2))


def animate(i):
    
    points.set_data([coords[i][0]], [coords[i][1]])
    return points

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames = frames, interval = 30)
ani.save('animation_2.gif', writer = 'pillow')