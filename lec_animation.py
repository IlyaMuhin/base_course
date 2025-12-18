import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#fhsfhhfdhufwfiuhhufhluighloewihg erfgg gwegeh
fig, ax = plt.subplots()


anim_object, = plt.plot([], [], '-', lw = 2) #iОбъект анимации

x, y = [], [] #Координаты объекта анимации
frames_interval= np.linspace(0, 2 * np.pi, 100)
ax.set_xlim(0,2 * np.pi)#Пределы изменений переменной X
ax.set_ylim(-1, 1)#Пределы изменений переменной Y

#Функция перестановки параметра в объект анимации
def update(frame):
    x.append(frame)#Расчет координаты X
    y.append(np.sin(frame))#Расчет координаты Y
    
    #Передача координат объекту анимации
    anim_object.set_data(x, y)

    return anim_object

ani = FuncAnimation(fig,#Вызов пространства для анимации
                    update,#Вызов функции подстановки координат
                    frames = frames_interval,#Интервал значений
                    interval = 30)#Интервал между кадрами
                                  #по умолчанию 200 милисекунд

ani.save('animatiom_1.gif', writer = 'pillow')