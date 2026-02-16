import numpy as np
#Find minimum and maximum in 1-Dimensional Array
arr = np.array([1,2,3,4])
print("min:",np.min(arr))
print("max:",np.max(arr))
#Find Position
print("min position:",np.argmin(arr))
print("max position:",np.argmax(arr))
#sqrt
print("sqrt:",np.sqrt(arr))
#sin value
print("sin:",np.sin(arr))
print("cos:",np.cos(arr))
#cumsum
print("cumsum:",np.cumsum(arr))
#Find minimum and maximum in 2-Dimensional Array
arr2d = np.array([[9,5,4,6],
                  [8,3,4,5]])
print("min:",np.min(arr2d,axis=1))
print("max:",np.max(arr2d,axis=1))
#Find Position
print("min position:",np.argmin(arr2d,axis=1))
print("max position:",np.argmax(arr2d,axis=1))
#sqrt
print("sqrt:",np.sqrt(arr2d))
#sin value
print("sin:",np.sin(arr2d))
#cos value
print("cos:",np.cos(arr2d))
