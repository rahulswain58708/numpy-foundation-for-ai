# Create a random array of 15 integers (0–50).
# Find all indexes where number is divisible by 3.

import numpy as np

arr = np.random.randint(0,50,15)
idx = np.where(arr % 3 == 0)
print(idx)