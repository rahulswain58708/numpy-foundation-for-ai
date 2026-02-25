#spiliting is reverse operation of joining.
#joining merge multiple array into single array but spliting break single array into multiple array.
#we use array_split(array,number of split) function.

#Example:- split the array in 3 parts
import numpy as np

arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
