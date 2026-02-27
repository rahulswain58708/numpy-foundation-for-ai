# Create an array with duplicate values.
# Find all indexes of number 5.
import numpy as np
arr = np.array([1,2,3,5,4,5,5])
x = np.where(arr == 5)
print(x)