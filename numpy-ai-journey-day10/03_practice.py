# 3️⃣ Concatenate 2D Arrays (Column-wise)

# Use same arrays from Q2
# Join them using axis=1.
import numpy as np

arr1 = np.array([[1,2],
                 [3,4]])
arr2 = np.array([[5,6],
                 [7,8]])
newarr = np.concatenate((arr1,arr2),axis = 1)
print(newarr)
