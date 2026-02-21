#Vectorization:- Vectorization in numpy refer to applying operation entire array without using explict loops.
#Why vectorization matters?
#1.improve performance
#2.produces cleaner code: easy to maintain
#3.scales better :- can efficently handel large scientific data and machine learning workloads.
# Example 1:- Add a number to each element
import numpy as np
arr = np.array([10,20,30,40])
num = 5
res = arr + num
print(res)

# Example 2: Adding Two Arrays Element-wise
a1 = np.array([1,2,3,4])
a2 = np.array([4,5,6,7])
print(a1 + a2)

# Example 3: Element - wise scalar multiplication
a3 = np.array([1,2,3,4])
res = a3 * 2
print(res)

# Example 4: Logical Operations on Arrays
ages = np.array([15,20,30])
res = ages > 18
print(res)
