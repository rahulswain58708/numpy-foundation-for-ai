#flattening means convert multidimensional array into 1D .
#We can use reshape(-1) to do this.
import numpy as np
mult_arr = np.array([[9,8,7],[6,5,4]])
arr = mult_arr.reshape(-1)
print(arr)