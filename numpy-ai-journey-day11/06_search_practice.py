# Use searchsorted() with side='right' and compare result.
import numpy as np

arr = np.array([1, 3, 5])
x = np.searchsorted(arr,[2,4],side='right')
print(x)