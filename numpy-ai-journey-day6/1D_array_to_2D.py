# Example 2: Broadcasting a 1D Array to a 2D Array
# This example shows how a 1D array a1 is added to a 2D array a2.
# NumPy automatically expands the 1D array along the rows of the 2D array to perform element-wise addition.

import numpy as np
a1 = np.array([1,2,3])
a2 = np.array([[4,5,6],[1,3,7]])
print(a1 + a2)
# output:- 
# [[ 5  7  9]
#  [ 2  5 10]]


