#stack is same as concatination , the only difference is it join arrays by creating a new axis(new dimension).

import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

arr = np.stack((arr1,arr2))
print(arr)