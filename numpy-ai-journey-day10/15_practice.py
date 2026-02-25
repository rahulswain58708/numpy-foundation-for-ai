# 1️⃣5️⃣ Vertical Split

# Use same array from Q14
# Split into 2 parts using np.vsplit().
import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8]])
newarr = np.vsplit(arr,2)
print(newarr)