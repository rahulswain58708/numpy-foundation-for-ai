# 9️⃣ Print Only Odd Numbers Using nditer
# From [11,12,13,14,15], print only odd numbers using np.nditer().

import numpy as np

arr = np.array([11,12,13,14,15])

for element in np.nditer(arr):
    if element % 2 != 0:
        print(element)