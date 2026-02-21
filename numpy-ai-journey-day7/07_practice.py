# 7️⃣ Normalize Array (Min-Max Scaling)
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
mini_val = np.min(arr)
max_val = np.max(arr)
res = (arr - mini_val) / (max_val - mini_val)
print(res)