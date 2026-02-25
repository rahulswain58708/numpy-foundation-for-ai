# 6️⃣ Stack with New Axis
# Use:
# a = [1,2,3]
# b = [4,5,6]
# Join using np.stack() with:
# axis=0
# axis=1
# Check shape difference.

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

newarr = np.stack((arr1,arr2),axis=0)
newarr1 = np.stack((arr1,arr2),axis=1)
print(newarr.shape)
print(newarr1.shape)