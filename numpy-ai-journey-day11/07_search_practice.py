# Create a 2D array (3x4).
# Find positions where value > 20.

import numpy as np

arr = np.array([[1,3,5,7],
                [10,15,20,25],
                [14,32,25,8]])
x = np.where(arr > 20)
print(x)