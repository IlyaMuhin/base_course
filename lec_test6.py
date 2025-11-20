import numpy as np
massive = np.array([[2,3,1,4,5,6,7], [8,1,3,2,2,6,8], [1,4,3,1,0,2,5], [4,5,0,1,3,2,1], [8,7,9,1,0,2,3]])
print(massive)
slice1 = massive[0:3, 0:2]
print(slice1)
slice2 = massive[1:3, 3:5]
print(slice2)
slice3 = massive[0:3, 5:6]
print(slice3)
slice4 = massive[4, 0:2]
print(slice4)
slice5 = massive[3::, 2:4]
print(slice5)
slice6 = massive[3, 5::]
print(slice6)