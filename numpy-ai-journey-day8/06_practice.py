# 6️⃣ Print Row Wise
# From the same 2D array, print row by row.
# Output should look like:
# [1 2 3]
# [4 5 6]

import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])
for row in arr:
    print(row)