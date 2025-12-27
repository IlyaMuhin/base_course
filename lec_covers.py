import numpy as np
import matplotlib.pyplot as plt

#Создание пространства для анимации
fig,ax = plt.subplots(subplot_kw = {'projection': '3d'})

#Определение параметров поверзности
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
R = 1

#Параметрическое задание поверхности
x = R * np.outer(np.cos(phi), np.sin(theta))
y = R * np.outer(np.sin(phi), np.sin(theta))
z = R * np.outer(np.ones(np.size(phi)), np.cos(theta))

#Построение пространственной кривой
ax.plot_surface(x, y, z)

ax.legend()

#Подписи осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#Подпись графика
ax.set_title('3D Test')

plt.savefig('fig2.png')