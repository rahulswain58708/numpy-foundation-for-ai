# 6️⃣ Element-wise Conditional Operation
import numpy as np
arr = np.array([5, 12, 7, 20, 3])
# 👉 Agar value > 10 hai to 100 multiply karo, warna as it is rakho.
res = np.where(arr > 10,arr * 100,arr)
print(res)