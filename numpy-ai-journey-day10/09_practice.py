# 9️⃣ Stack 3 Arrays

# Create:

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]

# Stack all three using np.stack().

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([7,8,9])

newarr = np.stack((arr1,arr2,arr3))
print(newarr)