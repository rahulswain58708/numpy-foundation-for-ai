# 8️⃣ Column-wise Scaling
import numpy as np
arr = np.array([[1, 2, 3],
                 [4, 5, 6]])
scale = np.array([1, 10, 100])
# Multiply each column differently using broadcasting.
print(arr * scale)
