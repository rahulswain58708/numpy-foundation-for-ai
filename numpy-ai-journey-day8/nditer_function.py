#using np.nditer we can iterate over a numpy array element by element using a single loop,
# even if the array is multidimensional.

import numpy as np
#itration 1D Array using np.nditer
arr_1D = np.array([1,2,3,4,5,6])
print("shape:",arr_1D.shape)
for x in np.nditer(arr_1D):
    print(x)
print()
#itration 2D Array using np.nditer
arr_2D = np.arange(1,11).reshape(2,5)
print("shape:",arr_2D.shape)
for y in np.nditer(arr_2D):
    print(y)
print()
#itration 3D Array using np.nditer

arr_3D = np.arange(1,21).reshape(2,2,5)
print("shape:",arr_3D.shape)
for z in np.nditer(arr_3D):
    print(z)