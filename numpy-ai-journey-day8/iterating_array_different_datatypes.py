#Iterating array with different data type
#We use op_dtypes as argument and pass it excepted datatype to change the datatype of element while iterating.

#numpy does not change the datatype of element inside array it required some other space called 'buffer',
#and in order to enable it in nditer() ,we pass flags = ['buffer']

#Example:- iterating through the array as string

import numpy as np
arr = np.array([1,2,3,4])
for element in np.nditer(arr,flags=['buffered'],op_dtypes='S'):
    print(element)
