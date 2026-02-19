#array indexing is the same as acess an array element.
#you can acess an array element by refering to the index number
#The index number in numpy array start with 0,meaning that first element has index 0,
#and the second element has index 1 etc.
# Exampe:- Get the first elment in following array
import numpy as np
arr = np.array([8,2,6,0])
print(arr[0])
#Get the second element in following array
print(arr[1])
# Get third and fourth elements from the following array and add them.
print(arr[2] + arr[3])

#Acess 2-D Array
#To access element from 2d arrays we can use comma separated integer represent the dimension and the index of element.
#Think of a 2d array like a table with,where dimension represent the row and the index represent the column.

#Example:- Acess the element on the first row ,second column.
arr2d = np.array([[1,2,3,4],[5,6,7,8]])
print("2nd element on first row:",arr2d[0,1])

#Example:- Access the element on the 2nd row, 5th column.
arr_2d = np.array([[1,2,3,4,5],
                   [6,7,8,9,10]])
print("5th element on 2nd row is:",arr_2d[1,4])

#Acess 3-D Array
#to acess element from 3d array we can use comma separate integers and represet the dimension at the index of element.
#Access the third element of the second array of the first array:
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d[0,1,2])

#Negative indexing
#use negative indexing acess array from the end.
# Print the last element from the 2nd dim:
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1[1,-1])
