#slicing in python means to taking element from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

# Example:- Slice elements from index 1 to index 5 from the following array:
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
#Example:- Slice elements from index 4 to the end of the array:
print(arr[4:])
#Example:- Slice elements from the beginning to index 4 (not included):
print(arr[:4])

#Negative slicing
#use minus operator to refer to an index from the end
# Example:- Slice from the index 3 from the end to index 1 from the end:
print(arr[-3:-1])
# Return every other element from index 1 to index 5:
print(arr[1:5:2])



