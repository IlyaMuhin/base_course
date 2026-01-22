import pyvista as pv
import numpy as np

# Создаём планету (сферу)
planet = pv.Sphere(radius=1.0, theta_resolution=100, phi_resolution=100)

# Создаём кратеры с помощью синусоидальных неровностей
# Сначала создаём базовую поверхность с шумом
points = planet.points.copy()
center = np.array([0, 0, 0])

# Добавляем кратеры разного размера
np.random.seed(42)
for _ in range(30):
    # Случайное положение на сфере
    theta = np.random.uniform(0, 2*np.pi)
    phi = np.random.uniform(0, np.pi)
    
    # Координаты центра кратера
    crater_center = np.array([
        np.sin(phi) * np.cos(theta),
        np.sin(phi) * np.sin(theta),
        np.cos(phi)
    ])
    
    # Размер кратера
    crater_radius = np.random.uniform(0.1, 0.3)
    crater_depth = np.random.uniform(0.05, 0.15)
    
    # Применяем кратер к поверхности
    for i, point in enumerate(points):
        # Нормализуем точку (чтобы была на сфере)
        point_normalized = point / np.linalg.norm(point)
        
        # Расстояние от центра кратера
        dist = np.arccos(np.clip(np.dot(point_normalized, crater_center), -1, 1))
        
        if dist < crater_radius:
            # Форма кратера - параболическая яма
            factor = (dist / crater_radius) ** 2
            displacement = crater_depth * (1 - factor)
            points[i] = point * (1 - displacement / np.linalg.norm(point))

# Обновляем точки планеты
planet.points = points
planet = planet.compute_normals()

# Создаём текстуру для цвета (лунная поверхность)
texture = pv.Texture()

# Цветовая карта для планеты
colors = np.zeros((planet.n_points, 3))
for i, point in enumerate(planet.points):
    height = np.linalg.norm(point)
    # Базовый серый цвет луны с вариациями
    gray_base = 0.4 + 0.2 * np.sin(point[0]*5) * np.cos(point[1]*5)
    colors[i] = [gray_base, gray_base*0.9, gray_base*0.8]

planet['colors'] = colors

# Визуализация
plotter = pv.Plotter(window_size=[800, 600])
plotter.add_mesh(planet, scalars='colors', rgb=True, smooth_shading=True)
plotter.add_light(pv.Light(position=(5, 5, 5)))
plotter.set_background('black')
plotter.show()