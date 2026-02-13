import pyvista as pv
import numpy as np


def create_parametric_surface(func, u_range=(0, 2 * np.pi), v_range=(0, 2 * np.pi), n_u=50, n_v=50):
    u = np.linspace(u_range[0], u_range[1], n_u)
    v = np.linspace(v_range[0], v_range[1], n_v)
    u, v = np.meshgrid(u, v)

    x, y, z = func(u, v)
    return pv.StructuredGrid(x, y, z)





def ponchik(u, v):

    x = np.cos(u)*(np.cos(v) + 3)
    y = np.sin(u)*(np.cos(v) + 3)
    z = np.sin(v)
    return x, y, z

def keglya(u, v):
    H = 1
    A = 0.8
    B = -1.5
    C = 1.2
    R = A* (1 - u) + B*u*(1 - u) + C*u
    x = R*np.cos(v)
    y = H*u
    z = R*np.sin(v)
    return x, y, z

def spiral(u, v):
    x = np.cos(u)*(np.cos(v) + 3)
    y = np.sin(u)*(np.cos(v) + 3)
    z = np.sin(v) + u
    return x, y, z

def log_spiral(u, v):
    x = u*np.cos(u)*(np.cos(v) + 1)
    y = u*np.sin(u)*(np.cos(v) + 1)
    z = u*np.sin(v)
    return x, y, z

def shell(u, v):
    x = u * np.cos(u)*(np.cos(v) + 1)
    y = u*np.sin(u)*(np.cos(v) + 1)
    z = u * np.sin(v) - (np.pi*((u+3)/8))**2 - 20
    return x, y, z


def threeleaf(u, v):
    x = np.cos(u)*np.cos(v) + 3 * np.cos(u)*(1.5 + np.sin(1.5*u / 2))
    y = np.sin(u) * np.cos(v) + 3 * np.sin(u) * (1.5 + np.sin(1.5*u / 2))
    z = np.sin(v) + 2 * np.cos(1.5 * u)
    return x, y, z

def diniplot(u, v):
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v) + np.log(np.tan(v/2)) + 0.2 * u - 4
    return x, y, z

def mebius(u, v):
    x = (1 + v/2 * np.cos(u/2))* np.cos(u)
    y = (1 + v/2 * np.cos(u/2))*np.sin(u)
    z = v/2 * np.sin(u/2)
    return x, y, z


def collatz_surface(u, v):
    x = u * np.cos(v)
    y = u * np.sin(v)
    z = np.sin(3 * u) * np.cos(v)
    return x, y, z







keglya = create_parametric_surface(keglya, (0, 1), (0, 2 * np.pi))
spiral = create_parametric_surface(spiral, (-2*np.pi, 2*np.pi), (-np.pi, np.pi))
ponchik = create_parametric_surface(ponchik, (-np.pi, np.pi), (-np.pi, np.pi))
log_spiral = create_parametric_surface(log_spiral, (0, 3 * np.pi), (-np.pi, np.pi))
shell = create_parametric_surface(shell, (0, 8 * np.pi), (-np.pi, np.pi))
threeleaf = create_parametric_surface(threeleaf, (-2*np.pi, 2*np.pi), (-np.pi, np.pi))
diniplot = create_parametric_surface(diniplot, (0, 4 * np.pi), (0.001, 2))
mebius = create_parametric_surface(mebius, (0, 2 * np.pi), (-1, 1))
collatz_surface = create_parametric_surface(collatz_surface, (0, 4), (0, 2 * np.pi))




pl = pv.Plotter(shape=(3,3))
pl.subplot(0, 0)
pl.add_mesh(keglya, color="r", show_edges=True)
pl.subplot(0, 1)
pl.add_mesh(ponchik, color="r", show_edges=True)
pl.subplot(0, 2)
pl.add_mesh(spiral, color="r", show_edges=True)
pl.subplot(1, 0)
pl.add_mesh(shell, color="r", show_edges=True)
pl.subplot(1, 1)
pl.add_mesh(threeleaf, color="r", show_edges=True)
pl.subplot(1, 2)
pl.add_mesh(diniplot, color="r", show_edges=True)
pl.subplot(2, 0)
pl.add_mesh(mebius, color="r", show_edges=True)
pl.subplot(2, 1)
pl.add_mesh(collatz_surface, color="r", show_edges=True)





pl.show()




