# Given:
# arr = np.array([2, 4, 6, 8, 10, 12])
# Find index of all even numbers.

import numpy as np

arr = np.array([2, 4, 6, 8, 10, 12])

idx = np.where(arr % 2 == 0)
print(idx)