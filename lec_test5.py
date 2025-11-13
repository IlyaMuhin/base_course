import numpy as np
from lec_test4 import m, n, trigonometry_array
trigonometry_array[:, [0,1]] = trigonometry_array[:, [1,0]]
print(trigonometry_array)