# 1️⃣ Print All Elements
# Create a NumPy array [10, 20, 30, 40, 50] and print each element using a loop.

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
for element in np.nditer(arr):
    print(element)