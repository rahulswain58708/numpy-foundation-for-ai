#Converting datatype of an existing array.
#The astype() function in numpy used to create new copy of array with a speicfic data type.
# this method essential used for converting datatype float to integer string to number.
#Example:- Change data type from float to integer by using 'i' as parameter value:
import numpy as np
arr = np.array([1.1,1.2,1.3,2.1])
new_arr = arr.astype('i')
print("Array:",new_arr)
print("Data Type:",new_arr.dtype)
#Example:- Change data type from float to integer by using 'int' as parameter value:
arr_1 = np.array([2.1,3.2,1.4,1.5])
arr_int = arr_1.astype(int)
print("Array:",arr_int)
print("Data Type:",arr_int.dtype)
