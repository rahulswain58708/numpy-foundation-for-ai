# Create an array [10, 25, 30, 45, 60, 75]
# Use np.where() to find index of numbers greater than 40.
import numpy as np

arr = np.array([10, 25, 30, 45, 60, 75])
idx = np.where(arr > 40)
print(idx)