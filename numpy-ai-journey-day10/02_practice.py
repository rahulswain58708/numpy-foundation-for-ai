# 2️⃣ Concatenate 2D Arrays (Row-wise)
# a = [[1,2],
#      [3,4]]

# b = [[5,6],
#      [7,8]]
import numpy as np

arr1 = np.array([[1,2],
                 [3,4]])
arr2 = np.array([[5,6],
                 [7,8]])
newarr = np.concatenate((arr1,arr2),axis = 0)
print(newarr)