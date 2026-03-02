#the numpy shuffle() function randomly reorder the elements of an array in place,
# meaning it modify the original array directly and does not return a new array.

import numpy as np

arr = np.array([1,2,3,4,5])
print("Original array:",arr)
np.random.shuffle(arr)
print("Shuffled array:",arr)