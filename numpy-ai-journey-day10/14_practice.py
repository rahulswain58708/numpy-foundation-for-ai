# 1️⃣4️⃣ Horizontal Split

# Create:

# arr = [[1,2,3,4],
#        [5,6,7,8]]

# Use np.hsplit() into 2 parts.

import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8]])
newarr = np.hsplit(arr,2)
print(newarr)