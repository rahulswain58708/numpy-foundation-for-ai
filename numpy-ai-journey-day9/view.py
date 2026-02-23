#View is the view of original Array
#View doesn't have own data ,We change the original array element effect will be view array 
#Or we change the view array element effect will be original array

#Example:- Make a View,Change the original array and display both arrays
import numpy as np
arr = np.array([1,2,3,4,5])
vi = arr.view()
arr[0] = 50
print("Original Array:",arr)
print("View Array:",vi)

# output:-
# Original Array: [50  2  3  4  5]
# View Array: [50  2  3  4  5]