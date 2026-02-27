# Given sorted array:
# arr = np.array([1, 3, 5, 7, 9])
# Use np.searchsorted() to find where 6 should be inserted.
import numpy as np

arr = np.array([1, 3, 5, 7, 9])
x = np.searchsorted(arr,6)
print(x)
