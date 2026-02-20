# 9️⃣ Row-wise Normalization
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
row_sum = arr.sum(axis=1).reshape(2,1)
# Divide each row by its row sum using broadcasting.
print(arr / row_sum)