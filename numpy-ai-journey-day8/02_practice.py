# 2️⃣ Print Only Even Numbers
# From array [1,2,3,4,5,6,7,8] print only even numbers using iteration.

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
for element in np.nditer(arr):
    if element % 2 == 0:
        print(element)
