#The numpy array object has a property called 'dtype' that return datatype of the array.
#Check the data type of an array object
import numpy as np
arr = np.array([1,2,3,4])
print("Data Type:",arr.dtype)
#Get the data type of an array containing strings:
arr_str = np.array(["apple","banana","cat"])
print("Data Type:",arr_str.dtype)
#Create Array with a define data type
#we use the array() function to create arrays,this function can take optional argument 'dtype'
#that allow us to expected datatype of the array element.

#Create an array with datatype string
arr_s = np.array([1,5,7,8,9],dtype='S')
print(arr_s)
print("Data Type:",arr_s.dtype)

# Create an array with data type 4 bytes integer:
arr4byte = np.array([10,4,8,9,5],dtype="i4")
print(arr4byte)
print("Data Type:",arr4byte.dtype)

