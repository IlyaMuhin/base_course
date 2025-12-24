import matplotlib.pyplot as plt
import numpy as np
import math

def stairs_plotter(n):
   x = np.arange(-n, n+1, 0.1)
   y = x // 2  * 2
   plt.plot(x, y )
   plt.savefig('dop4.png')

stairs_plotter(5)