#joining means putting element of two or more array in a single array.
#Example:-join two arrays
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.concatenate((arr1,arr2))
print(arr)