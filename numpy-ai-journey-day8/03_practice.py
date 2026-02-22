# 3️⃣ Find Sum Using Loop
# Using iteration, find the sum of [5,10,15,20].
# (⚠ Don’t use np.sum() — use loop.)

import numpy as np

total = 0
arr = np.array([5,10,15,20])
for element in np.nditer(arr):
    total += element
print(total)