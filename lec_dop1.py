import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation



R = 10
t = np.arange(0, 4 * np.pi + 0.1, 0.1)
x = R * np.cos(t)**3
y = R * np.sin(t)**3



fig, ax = plt.subplots()
star, = plt.plot([],[], '-', color = 'r', label = 'Star')

frames = 180
coords = np.zeros((frames, 2))




def animate(alpha):
    X = (x+10) * np.cos(alpha) - (y+10) * np.sin(alpha)
    Y =  x * np.sin(alpha) + y * np.cos(alpha)
    star.set_data(X, Y)




edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate,frames = np.arange(0, 2 * np.pi, 0.1), interval = 30)
ani.save('dop1.gif', writer = 'pillow')