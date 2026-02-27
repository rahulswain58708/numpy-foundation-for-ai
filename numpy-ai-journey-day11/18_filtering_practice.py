# Given:

# arr = np.array([5, 15, 25, 35, 45])

# Filter numbers divisible by 5 AND greater than 20.

import numpy as np

filter_arr = []
arr = np.array([5, 15, 25, 35, 45])
for num in arr:
    if num % 5 == 0 and num > 20:
        filter_arr.append(num)
print(filter_arr)