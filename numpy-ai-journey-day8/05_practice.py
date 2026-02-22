# 5️⃣ Print All Elements of 2D Array
# [[1,2,3],
#  [4,5,6]]
# Print all elements using nested loops.

import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])
for row in arr:
    for element in row:
        print(element)
