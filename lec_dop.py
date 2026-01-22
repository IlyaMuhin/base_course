import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def cycloid_move(angle_vel, time):
    R = 1
    alpha = angle_vel * np.pi / 180 * time

    x = R * (alpha - np.sin(alpha)) - 10
    y = R * (1 - np.cos(alpha))
    return x, y

R1 = 1
t = np.arange(0, 4 * np.pi + 0.1, 0.1)
x = R1 * np.cos(t)
y = R1 * np.sin(t)

fig, ax = plt.subplots()
ball, = plt.plot([],[], '-', color = 'r', label = 'Ball')

# frames = 180
# coords = np.zeros((frames, 2))




# def animate1(alpha):
#     X = (x+10) * np.cos(alpha) - (y+10) * np.sin(alpha)
#     Y =  x * np.sin(alpha) + y * np.cos(alpha)
#     ball.set_data(X, Y)





# ball, = plt.plot([], [], '-', color = 'r', label = 'Ball')
cycloid, = plt.plot([], [], '-', color = 'r', label = 'Ball')

frames = 1000
coords = np.zeros((frames, 2))



def animate(i):
    coords[i] = cycloid_move(angle_vel = 2, time = i)
    # ball.set_data([coords2[i][0]], [coords2[i][1]])
    cycloid.set_data(coords[:i, 0], coords[:i, 1])
    X = x * np.cos(i) - y * np.sin(i)
    Y =  x * np.sin(i) + y * np.cos(i)
    ball.set_data(X, Y)
    return  cycloid, ball

edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


ani = FuncAnimation(fig, animate, frames = frames, interval = 30)
# ani2 = FuncAnimation(fig, animate1,frames = np.arange(0, 2 * np.pi, 0.1), interval = 30)
# ani2.save('dop1.gif', writer = 'pillow')
ani.save('dop1.gif', writer = 'pillow')