# Create random array (size 15).
# Filter numbers between 10 and 30.


import numpy as np

filter_arr = []
arr = np.random.randint(1,31,15)

for num in arr:
    if num >= 10:
        filter_arr.append(num)

print("Original:", arr)
print("Filtered:", filter_arr)