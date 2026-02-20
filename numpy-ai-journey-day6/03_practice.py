# 3️⃣ Add Row Vector
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
row = np.array([10, 20, 30])
# Add row to arr using broadcasting.
print(row + arr)