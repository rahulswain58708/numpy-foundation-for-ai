# The unique() function return the sorted unique element in array and 
# can optionaly provide additional information like indces and count of occurenc.

import numpy as np

arr = np.array([2,1,2,3,2,4,5,5,6,3])
unique_values = np.unique(arr,return_index=True,return_counts=True)
print(unique_values)