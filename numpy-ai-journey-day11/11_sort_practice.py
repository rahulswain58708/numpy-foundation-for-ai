# Given 2D array:
# arr = np.array([[3, 2, 1],
#                 [6, 5, 4]])
# Sort row-wise.
# Sort column-wise.

import numpy as np

arr = np.array([[3, 2, 1],
                 [6, 5, 4]])
row_sort = np.sort(arr,axis=1)
col_sort = np.sort(arr,axis=0)
print(row_sort)
print(col_sort)