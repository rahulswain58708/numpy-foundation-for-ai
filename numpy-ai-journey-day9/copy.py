#Copy is the copy of a new array.
#Copy has own data , we change the copy array element doesnot effect original array,
#or we change original array element doesnot effect copy array because copy array has own data.

#Example:- Make a copy , change the original and display both.
import numpy as np
arr = np.array([1,2,3,4,5])
co = arr.copy()
arr[0] = 10
print("Original Array:",arr)
print("Copy Array:",co)

#Output:-
# Original Array: [10  2  3  4  5]
# Copy Array: [1 2 3 4 5]