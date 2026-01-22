import numpy as np
import matplotlib.pyplot as plt

#Создание пространства для анимации
fig,ax = plt.subplots(subplot_kw = {'projection': '3d'})

#Определение параметров поверзности
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)
a = 1
b = 2
c = 3

#Параметрическое задание поверхности
x = np.outer(phi,  np.cos(theta)) + np.outer(a, theta**2)
y = np.outer(phi, np.sin(theta)) + np.outer(b, theta**2)
z = np.outer(c * theta**2, np.ones(np.size(phi)))

#Построение пространственной кривой
ax.plot_surface(x, y, z)

ax.legend()

#Подписи осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#Подпись графика
ax.set_title('3D Test')

plt.savefig('test1.4.png')