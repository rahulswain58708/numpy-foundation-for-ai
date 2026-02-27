# Create a 1D array of numbers 1–20.
# Find index of number 15.
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
idx = np.where(arr == 15)
print(idx)