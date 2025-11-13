import numpy as np
from lec_test4 import m, n, trigonometry_array
trigonometry_array1 = trigonometry_array[:, 1:2]
trigonometry_array2 = trigonometry_array[:, 0:1]
trigonometry_array3 = trigonometry_array[:, 2:m+1]
print(np.concatenate((trigonometry_array1, trigonometry_array2, trigonometry_array3), axis=1))
print()