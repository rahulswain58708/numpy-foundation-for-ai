# Advanced Level (14–15)
# Use:
import numpy as np
arr = np.arange(1, 17).reshape(4, 4)
# This creates:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]
# 14. Extract this submatrix:
# [[ 6  7]
#  [10 11]]
print(arr[1:3,1:3])
# 15. Print elements on the diagonal of the matrix.
print(np.diag(arr))