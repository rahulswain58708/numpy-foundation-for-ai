# 1️⃣1️⃣ Split 2D Array Row-wise
# arr = [[1,2],
#        [3,4],
#        [5,6],
#        [7,8]]

# Split into 2 arrays row-wise.
import numpy as np

arr = np.array([[1,2],
                [3,4],
                [5,6],
                [7,8]])
newarr = np.array_split(arr,2,axis=0)
print(newarr)