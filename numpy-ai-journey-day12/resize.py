#This function return a new array with the specified shape and size.
import numpy as np

arr = np.array([1,2,3,4,5,6])
resize_arr = np.resize(arr,(2,3))
resize_arr1 = np.resize(arr,(3,2))
print(resize_arr)
print(resize_arr1)