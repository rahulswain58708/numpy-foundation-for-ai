# 6️⃣ 3D + 1D Broadcasting
import numpy as np
arr = np.ones((2, 3, 4)) 
vec = np.array([1, 2, 3, 4]) 
# Add vec to arr.
res = vec + arr
print(res)
# 👉 What will be final shape? (2,3,4)
