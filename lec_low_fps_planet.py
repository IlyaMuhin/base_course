import numpy as np
import pyvista as pv
from scipy import ndimage
import math

# Создаем сферу - основу планеты с высоким разрешением
sphere = pv.Sphere(radius=1.0, phi_resolution=300, theta_resolution=300)


# Функция для добавления плавного шума
def add_smooth_noise(mesh, octaves=4, scale=0.08, seed=42):
    points = mesh.points
    normals = mesh.point_normals

    # Получаем сферические координаты
    r = np.linalg.norm(points, axis=1)
    theta = np.arctan2(points[:, 1], points[:, 0])
    phi = np.arccos(points[:, 2] / r)

    np.random.seed(seed)
    height_map = np.zeros(len(points))

    for i in range(octaves):
        frequency = 2 ** i
        amplitude = scale / frequency

        # Генерируем шум на основе сферических координат
        noise = np.random.randn(len(points))
        # Сильное сглаживание для плавности
        noise = ndimage.gaussian_filter(noise.reshape(-1, 1),
                                        sigma=20 / frequency).flatten()

        # Добавляем гармонические компоненты для естественного вида
        harmonic = (np.sin(frequency * theta * 2) *
                    np.cos(frequency * phi * 2) + 1) / 2

        height_map += amplitude * noise * harmonic

    # Ограничиваем максимальную амплитуду
    height_map = np.tanh(height_map) * 0.15

    # Применяем изменения
    displaced_points = points + normals * height_map.reshape(-1, 1)
    mesh.points = displaced_points

    return mesh, height_map


# Функция для создания аккуратных кратеров
def add_subtle_craters(mesh, num_craters=30, max_crater_depth=0.1):
    points = mesh.points
    normals = mesh.point_normals
    original_norm = np.linalg.norm(points, axis=1)

    np.random.seed(123)
    crater_positions = np.random.randn(num_craters, 3)
    crater_positions = crater_positions / np.linalg.norm(crater_positions, axis=1, keepdims=True)
    crater_radii = np.random.uniform(0.08, 0.25, num_craters)
    crater_depths = np.random.uniform(0.03, max_crater_depth, num_craters)

    for i in range(num_craters):
        # Угловое расстояние (более точно для сферы)
        dot_products = np.dot(points, crater_positions[i])
        angular_distances = np.arccos(np.clip(dot_products, -1, 1))

        # Плавная функция кратера (квадратичная с плавными краями)
        mask = angular_distances < crater_radii[i]
        if np.any(mask):
            # Нормализованное расстояние от центра
            t = angular_distances[mask] / crater_radii[i]

            # Квадратичная форма с плавными краями
            crater_shape = crater_depths[i] * (1 - t ** 2) * np.exp(-t ** 2 * 3)

            # Смещение с сохранением сферичности
            displacement = normals[mask] * crater_shape.reshape(-1, 1)
            points[mask] -= displacement

    # Корректируем, чтобы сохранить сферичность
    current_norm = np.linalg.norm(points, axis=1)
    correction_factor = original_norm / current_norm
    points = points * correction_factor.reshape(-1, 1)

    mesh.points = points
    return mesh


# Функция для создания плавных горных цепей
def add_smooth_mountains(mesh, num_mountain_ranges=6):
    points = mesh.points
    normals = mesh.point_normals
    original_norm = np.linalg.norm(points, axis=1)

    np.random.seed(456)
    mountain_axes = []
    mountain_strengths = []

    for _ in range(num_mountain_ranges):
        axis = np.random.randn(3)
        axis = axis / np.linalg.norm(axis)
        mountain_axes.append(axis)
        mountain_strengths.append(np.random.uniform(0.05, 0.15))

    # Комбинируем все горные хребты
    total_displacement = np.zeros_like(points)

    for axis, strength in zip(mountain_axes, mountain_strengths):
        # Проекция на ось горного хребта
        projection = np.dot(points, axis)

        # Синусоида с несколькими частотами для естественности
        freq1 = np.random.uniform(4, 8)
        freq2 = np.random.uniform(12, 20)
        phase = np.random.uniform(0, 2 * np.pi)

        mountain_profile = (
                0.7 * np.sin(freq1 * projection + phase) +
                0.3 * np.sin(freq2 * projection + phase * 2)
        )

        # Гауссово затухание по окружности
        gaussian_width = np.random.uniform(0.3, 0.6)
        latitudinal_factor = np.exp(-(np.arccos(np.abs(np.dot(points, axis))) ** 2) /
                                    (2 * gaussian_width ** 2))

        displacement = strength * mountain_profile.reshape(-1, 1) * \
                       latitudinal_factor.reshape(-1, 1) * normals

        total_displacement += displacement

    # Применяем смещение
    points += total_displacement

    # Корректируем радиус для сохранения сферичности
    current_norm = np.linalg.norm(points, axis=1)
    correction_factor = original_norm / current_norm
    points = points * correction_factor.reshape(-1, 1)

    mesh.points = points
    return mesh


# Функция для создания тектонических разломов
def add_tectonic_features(mesh, num_features=15):
    points = mesh.points
    original_norm = np.linalg.norm(points, axis=1)

    np.random.seed(789)
    for _ in range(num_features):
        # Случайное направление разлома
        pole = np.random.randn(3)
        pole = pole / np.linalg.norm(pole)

        # Великий круг (экватор относительно полюса)
        distances_to_pole = np.arccos(np.clip(np.dot(points, pole), -1, 1))

        # Разлом вдоль великого круга с отклонениями
        fault_line = np.abs(distances_to_pole - np.pi / 2) < 0.15

        if np.any(fault_line):
            # Синусоидальное смещение вдоль разлома
            longitude = np.arctan2(points[fault_line, 1], points[fault_line, 0])
            displacement = 0.04 * np.sin(8 * longitude + np.random.uniform(0, 2 * np.pi))

            normals = mesh.point_normals[fault_line]
            points[fault_line] += normals * displacement.reshape(-1, 1)

    # Корректируем радиус
    current_norm = np.linalg.norm(points, axis=1)
    correction_factor = original_norm / current_norm
    points = points * correction_factor.reshape(-1, 1)

    mesh.points = points
    return mesh


# Функция для коррекции сферичности
def enforce_sphericity(mesh, target_radius=1.0, strength=0.5):
    """Корректирует форму к идеальной сфере"""
    points = mesh.points
    norms = np.linalg.norm(points, axis=1)

    # Мягкая коррекция к сфере
    correction = target_radius / norms
    smoothed_correction = 1 + (correction - 1) * strength

    points = points * smoothed_correction.reshape(-1, 1)
    mesh.points = points

    return mesh


# Создаем аккуратную планету
print("Создание аккуратной планеты со сложной поверхностью...")

# 1. Начинаем со сферы высокой детализации
planet = sphere

# 2. Добавляем плавный базовый рельеф
planet, elevation = add_smooth_noise(planet, octaves=5, scale=0.1, seed=42)

# 3. Добавляем аккуратные кратеры
planet = add_subtle_craters(planet, num_craters=40, max_crater_depth=0.08)

# 4. Добавляем плавные горные цепи
planet = add_smooth_mountains(planet, num_mountain_ranges=8)

# 5. Добавляем тектонические особенности
planet = add_tectonic_features(planet, num_features=12)

# 6. Корректируем к идеальной сфере
planet = enforce_sphericity(planet, target_radius=1.0, strength=0.3)

# 7. Финализируем с небольшим детализирующим шумом
planet, final_elevation = add_smooth_noise(planet, octaves=2, scale=0.02, seed=999)

# 8. Финальная коррекция сферичности
planet = enforce_sphericity(planet, target_radius=1.0, strength=0.1)

# Вычисляем нормали для красивого отображения
planet = planet.compute_normals(cell_normals=False, point_normals=True,
                                consistent_normals=True, auto_orient_normals=True)

# Создаем красивые цвета на основе высоты
elevation = np.linalg.norm(planet.points, axis=1)
elevation_normalized = (elevation - elevation.min()) / (elevation.max() - elevation.min())

# Расширенная цветовая схема
colors = np.zeros((len(elevation_normalized), 3))

# Океаны и глубокие впадины
water_mask = elevation_normalized < 0.25
colors[water_mask] = np.array([0.05, 0.15, 0.4])  # Глубокий синий

# Равнины и низменности
plains_mask = (elevation_normalized >= 0.25) & (elevation_normalized < 0.4)
colors[plains_mask] = np.array([0.2, 0.5, 0.2])  # Зеленый

# Холмы и предгорья
hills_mask = (elevation_normalized >= 0.4) & (elevation_normalized < 0.6)
colors[hills_mask] = np.array([0.4, 0.6, 0.3])  # Светло-зеленый

# Горы
mountains_mask = (elevation_normalized >= 0.6) & (elevation_normalized < 0.85)
colors[mountains_mask] = np.array([0.6, 0.5, 0.4])  # Коричневый

# Высокие пики и вулканы
peaks_mask = elevation_normalized >= 0.85
colors[peaks_mask] = np.array([0.9, 0.9, 0.9])  # Белый (снег)

# Добавляем полярные шапки
theta = np.arctan2(planet.points[:, 1], planet.points[:, 0])
phi = np.arccos(planet.points[:, 2] / elevation)
polar_mask = (np.abs(phi) < 0.3) | (np.abs(phi) > 2.84)
colors[polar_mask] = np.array([0.95, 0.95, 1.0])  # Голубовато-белый

# Добавляем вулканические регионы (редкие)
np.random.seed(111)
volcanic_mask = (elevation_normalized > 0.7) & (np.random.rand(len(elevation_normalized)) < 0.01)
colors[volcanic_mask] = np.array([0.7, 0.3, 0.2])  # Вулканический

# Плавные переходы между биомами
from scipy.ndimage import gaussian_filter

for i in range(3):
    colors[:, i] = gaussian_filter(colors[:, i], sigma=5)

# Назначаем цвета
planet['colors'] = np.clip(colors, 0, 1)

# Визуализация с улучшенными настройками
plotter = pv.Plotter(window_size=[1400, 900])

# Основная поверхность планеты
plotter.add_mesh(planet, scalars='colors', rgb=True,
                 smooth_shading=True,
                 specular=0.4,
                 specular_power=20,
                 ambient=0.2,
                 diffuse=0.7,
                 metallic=0.1,
                 roughness=0.7,
                 show_scalar_bar=False)

# Добавляем атмосферную дымку (полупрозрачная сфера)
atmosphere = pv.Sphere(radius=1.05, theta_resolution=100, phi_resolution=100)
plotter.add_mesh(atmosphere, color='lightblue', opacity=0.05,
                 smooth_shading=True, show_edges=False)

# Настраиваем сложное освещение
light1 = pv.Light(position=(10, 0, 5), light_type='scene light',
                  intensity=0.8, color='white')
light2 = pv.Light(position=(-5, 8, 3), light_type='scene light',
                  intensity=0.4, color=(1.0, 0.9, 0.8))
light3 = pv.Light(position=(0, -5, -2), light_type='scene light',
                  intensity=0.2, color=(0.8, 0.9, 1.0))

plotter.add_light(light1)
plotter.add_light(light2)
plotter.add_light(light3)

# Настройки камеры и фона
plotter.set_background('black')
plotter.camera_position = [(4, 3, 4), (0, 0, 0), (0, 0, 1)]

# Добавляем информацию
plotter.add_text("Планета Sphaira", position="upper_edge",
                 font_size=24, color="white", font="courier")
plotter.add_text("Радиус: 6371 км | Гравитация: 9.8 м/с²",
                 position="lower_edge", font_size=12, color="lightgray")

# Включаем тени и глубину резкости
plotter.enable_ssao(radius=2.0, bias=0.01)
plotter.enable_anti_aliasing('ssaa')

print("Визуализация планеты...")
plotter.show()

# Дополнительные опции для сохранения
save_option = input("Сохранить планету в файл? (y/n): ")
if save_option.lower() == 'y':
    # Сохраняем в нескольких форматах
    planet.save('sphaira_planet.vtk')
    plotter.screenshot('sphaira_planet.png')
    print("Планета сохранена как 'sphaira_planet.vtk' и 'sphaira_planet.png'")


# Создаем дополнительный вид с разных ракурсов
def create_multi_view():
    """Создает несколько видов планеты"""
    multi_plotter = pv.Plotter(shape=(2, 2), window_size=[1200, 800])

    # Вид 1: Полная планета
    multi_plotter.subplot(0, 0)
    multi_plotter.add_text("Полный вид", position="upper_edge", font_size=12)
    multi_plotter.add_mesh(planet, scalars='colors', rgb=True, smooth_shading=True)
    multi_plotter.camera_position = [(3, 0, 0), (0, 0, 0), (0, 0, 1)]

    # Вид 2: Крупный план рельефа
    multi_plotter.subplot(0, 1)
    multi_plotter.add_text("Крупный план гор", position="upper_edge", font_size=12)
    multi_plotter.add_mesh(planet, scalars='colors', rgb=True, smooth_shading=True)
    multi_plotter.camera_position = [(1.5, 1.5, 1.5), (0.5, 0.5, 0.5), (0, 0, 1)]

    # Вид 3: Вид на полюс
    multi_plotter.subplot(1, 0)
    multi_plotter.add_text("Северный полюс", position="upper_edge", font_size=12)
    multi_plotter.add_mesh(planet, scalars='colors', rgb=True, smooth_shading=True)
    multi_plotter.camera_position = [(0, 0, 2), (0, 0, 0), (0, 1, 0)]

    # Вид 4: Топографическая карта
    multi_plotter.subplot(1, 1)
    multi_plotter.add_text("Топография", position="upper_edge", font_size=12)
    multi_plotter.add_mesh(planet, scalars=elevation_normalized,
                           cmap='terrain', smooth_shading=True)

    multi_plotter.link_views()
    multi_plotter.show()


if input("Показать дополнительные виды? (y/n): ").lower() == 'y':
    create_multi_view()