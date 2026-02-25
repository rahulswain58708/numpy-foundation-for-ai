# 7️⃣ Column Stack

# Use:

# a = [1,2,3]
# b = [4,5,6]

# Join using np.column_stack().

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

newarr = np.column_stack((arr1,arr2))
print(newarr)