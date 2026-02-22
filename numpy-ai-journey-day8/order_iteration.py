#we can also specify the order of iteration
# (row-major order 'c' column major order 'F' )

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])

for element in np.nditer(arr,order='F'):
    print(element)
print()
#output:-
# 1
# 4
# 2
# 5
# 3
# 6
for elem in np.nditer(arr,order='C'):
    print(elem)
# output:-
# 1
# 2
# 3
# 4
# 5
# 6