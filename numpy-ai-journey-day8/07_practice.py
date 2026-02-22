# 7️⃣ Print Column Wise
# From the same array, print column-wise elements.
# Expected Output:
# 1 4
# 2 5
# 3 6

import numpy as np
arr = np.array([[1,2,3],
                [4,5,6]])
for x in arr.T:
    for y in x:
        print(y,end=" ")
    print()
    