# Create random array of 20 numbers.
# Sort only first 10 elements.

import numpy as np

arr = np.array([10,9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19,20])
arr_sort = np.sort(arr[0:10])
print(arr_sort)