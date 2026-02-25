# 4️⃣ Use np.hstack()
# Join:
# a = [1,2,3]
# b = [4,5,6]

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

newarr = np.hstack((arr1,arr2))
print(newarr)