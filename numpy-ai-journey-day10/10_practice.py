# 🔟 Split 1D Array
# Create:
# arr = [1,2,3,4,5,6]
# Split into 3 equal parts using np.split().

import numpy as np
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr)



