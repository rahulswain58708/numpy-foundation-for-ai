# Example 3: Broadcasting in Conditional Operations
# This example checks each age in the array and assigns "Adult" or "Minor" using np.where().
import numpy as np
a = np.array([12, 24, 35, 45, 60, 72])
b = np.array(["Adult","Minor"])
res = np.where(a > 18,b[0],b[1])
print(res)

# Output:- ['Minor' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult']
