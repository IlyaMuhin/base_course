import pyvista as pv
import numpy as np
import random


choice = input('Выберите форму планеты(сфера,своя): ')

if choice == 'сфера':

    R = float(input('Введите радиус планеты: '))
    sphere = pv.Sphere(radius=R, phi_resolution=100, theta_resolution=100)
    sphere2 = pv.Sphere(radius=R, phi_resolution=100, theta_resolution=100)

    N = int(input('Введите количество кратеров(0 - 25): '))








    for i in range(N):
        try:
            random_vertex_index = random.randint(0, sphere2.n_points - 1)
            random_point = sphere2.points[random_vertex_index]


            crater_sphere = pv.Sphere(radius=0.4*R, center=(random_point[0]*1.3, random_point[1]*1.3, random_point[2]*1.3))


            sphere = sphere.boolean_difference(crater_sphere)


        except ValueError:
            break

    for i in range(len(sphere.points) // 2):
        random_vertex_index = random.randint(0, sphere.n_points - 1)
        random_point = sphere.points[random_vertex_index]
        random_point *= 1.01


    plotter = pv.Plotter()

    plotter.add_mesh(sphere, color='gray', show_edges=True)

    plotter.show()

elif choice == 'своя':

    print('Введите вашу функцию вида x(u,v), y(u,v), z(u,v). (математические функции записывать как:(np.sin, np.cos, np.tg, np.ctg, np.pi): ')

    fx = input('x = ')
    fy = input('y = ')
    fz = input('z = ')

    print('Введите область определения параметров u и v: ')
    u1 = input('u1 = ')
    u2 = input('u2 = ')
    v1 = input('v1 = ')
    v2 = input('v2 = ')



    def create_parametric_surface(func, u_range=(0, 2 * np.pi), v_range=(0, 2 * np.pi), n_u=50, n_v=50):
        u = np.linspace(u_range[0], u_range[1], n_u)
        v = np.linspace(v_range[0], v_range[1], n_v)
        u, v = np.meshgrid(u, v)

        x, y, z = func(u, v)
        return pv.StructuredGrid(x, y, z)


    def object(u, v):

        x = eval(str(fx))
        y = eval(str(fy))
        z = eval(str(fz))
        return x, y, z


    object = create_parametric_surface(object, (eval(u1), eval(u2)), (eval(v1), eval(v2)))

    plotter = pv.Plotter()

    plotter.add_mesh(object, color='gray', show_edges=True)

    plotter.show()
