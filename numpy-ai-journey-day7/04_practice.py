# 4️⃣ Replace Negative Values with 0
import numpy as np
arr = np.array([-3, 5, -1, 7, -9])
# 👉 Negative numbers ko 0 se replace karo (loop allowed nahi).
res = np.where(arr < 0, 0,arr)
print(res)
