#use enurmate to acess both index and value, in numpy we use ndenumerate

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
for idx,val in np.ndenumerate(arr):
    print(idx,val)
