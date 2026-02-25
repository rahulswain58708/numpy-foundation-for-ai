# 1️⃣3️⃣ Unequal Split
# arr = [1,2,3,4,5,6,7]

# Split at indices [2,5] using np.array_split().
import numpy as np

arr = np.array([1,2,3,4,5,6,7])
newarr = np.array_split(arr,[2,5])
print(newarr)