# 9️⃣ Row-wise Sum (2D Array)
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
s = arr.sum(axis = 1)
# 👉 Har row ka sum nikaalo.
print(s)