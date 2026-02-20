#Broadcasting in numpy allow us to perform arithmatic operation 
# on array of different shapes without reshaping them.

# It automatically adjusts the smaller array to match the larger array's 
# shape by replicating its values along the necessary dimensions. 
# This makes element-wise operations more efficient by reducing memory usage and eliminating the need for loops.

# Example 1: Broadcasting a Scalar to a 1D Array
# It creates a NumPy array arr with values [1, 2, 3] and adds a scalar value 1 to each element of the array using broadcasting.
import numpy as np

arr = np.array([1,2,3])
res = arr + 1
print(res)
#Output:- [2 3 4]

