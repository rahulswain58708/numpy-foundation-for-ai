# 8️⃣ Row Stack

# Use same arrays and join using np.row_stack().

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

newarr = np.row_stack((arr1,arr2))
print(newarr)