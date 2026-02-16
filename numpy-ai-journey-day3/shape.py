#Check shape of an array
import numpy as np
arr = np.array([[1,2,3,4],
                [4,5,8,2]])
print(arr.shape)
#create 4dimension array using ndmin
arr_4dim = np.array([1,2,3,4],ndmin=4)
print(arr_4dim)
#check dimension
print(arr_4dim.ndim)
