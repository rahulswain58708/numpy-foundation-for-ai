# Iterate 2D Array Using nditer
# Use np.nditer() to print all elements of:
# [[7,8],
#  [9,10]]

import numpy as np

arr = np.array([[7,8],
                [9,10]])

for element in np.nditer(arr):
    print(element)