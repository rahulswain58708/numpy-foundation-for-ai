# 1️⃣2️⃣ Split 2D Array Column-wise

# Use same array and split column-wise into 2 parts.
import numpy as np

arr = np.array([[1,2],
                [3,4],
                [5,6],
                [7,8]])
newarr = np.array_split(arr,2,axis=1)
print(newarr)