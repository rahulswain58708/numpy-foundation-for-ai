# 1. Create a 1D NumPy array from 1 to 10.
# Print the 4th element.
import numpy as np
arr = np.arange(1,11)
print("Array = ",arr)
print(f"4th element is:",arr[3])
# 2. From the same array, print the last element using negative indexing.
print(f"last element is:",arr[-1])
# 3. Slice the array to print elements from index 2 to index 6.
print(arr[2:7])
# 4. Reverse the array using slicing only.
print(f"reverse:{arr[::-1]}")
# 5. Print every 2nd element from the array.
print(arr[::2])