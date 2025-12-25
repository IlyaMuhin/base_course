import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33

x,y = [x0], [y0]

for n in range(1, 100):
    x.append(x[n - 1]**2 - y[n - 1]**2 + C)
    y.append(2 * x[n-1] * y[n-1] + D)

fig, ax = plt.subplots()


anim_object, = plt.plot([], [], 'o', lw = 2) #iОбъект анимации


frames_interval= np.linspace(0, 99, 99)
ax.set_xlim(-1, 1)#Пределы изменений переменной X
ax.set_ylim(-1, 1)#Пределы изменений переменной Y

#Функция перестановки параметра в объект анимации
def update(frame):
    anim_object.set_data([x[:frame:]], [y[:frame:]])
    return anim_object

ani = FuncAnimation(fig,#Вызов пространства для анимации
                    update,#Вызов функции подстановки координат
                    frames = 99,#Интервал значений
                    interval = 30)#Интервал между кадрами
                                  #по умолчанию 200 милисекунд

ani.save('test4.gif', writer = 'pillow')