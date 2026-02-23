#Numpy array have a attribute called base used to check array own data.
#if base return None then array own data.
#if base return array object then array doesn't own data.
import numpy as np
arr = np.array([1,2,3,4,5])
co = arr.copy()
vi = arr.view()
print(co.base)
print(vi.base)
# output:-
# None
# [1 2 3 4 5]