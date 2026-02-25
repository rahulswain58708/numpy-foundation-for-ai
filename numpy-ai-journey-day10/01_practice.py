# 1️⃣ Concatenate 1D Arrays
# Create two arrays:
# a = [1,2,3]
# b = [4,5,6]
# Join them using np.concatenate().

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

newarr = np.concatenate((arr1,arr2))
print(newarr)