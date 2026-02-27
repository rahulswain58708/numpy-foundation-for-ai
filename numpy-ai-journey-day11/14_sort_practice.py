# Given:
# arr = np.array([3, 1, 4, 1, 5, 9])
# Find index order using argsort()
# Reorder original array manually using returned indexes.
import numpy as np
sort_arr = []
arr = np.array([3, 1, 4, 1, 5, 9])
idx_order = np.argsort(arr)
for i in idx_order:
    sort_arr.append(arr[i])
print(sort_arr)