import numpy as np
#Addition 1D array
arr = np.array([1,2,3,4])
total = arr + 5
print(total)
print()

arr1 = np.array([8,2,9,4])
arr2 = np.array([4,5,3,4])
sum_arr = arr1 + arr2
print(sum_arr)
print()
#2D Array Addition 
arr3 = np.array([[4,5,8,7],[3,7,6,6]])
arr4 = np.array([[7,9,8,6],[4,5,8,2]])
sum2d = arr3 + arr4
print(sum2d)
print()

#Substraction 1D array
arr5 = np.array([7,5,4,2,2,4])
arr6 = np.array([9,8,7,6,4,2])
sub = arr5 - arr6
print(sub)
print()

#substraction 2D array
arr7 = np.array([[9,6,5,4,2,8],[7,3,2,4,1,4]])
arr8 = np.array([[8,4,3,1,1,7],[7,7,5,2,0,6]])
sub2d = arr7 - arr8
print(sub2d)
print()

#Multiplication 1D array
arr10 = np.array([1,2,3,4])
arr11 = np.array([4,3,2,1])
mul = arr10 * arr11
print(mul)
print()

#Multiplication 2D array
arr12 = np.array([[7,3,2,6],[4,9,8,2]])
arr13 = np.array([[4,5,2,8],[8,2,4,3]])
mul2d = arr12 * arr13
print(mul2d)
print()

#Division 1D array
arr14 = np.array([28,18,8,16])
arr15 = np.array([7,2,4,4])
div = arr14 / arr15
print(div)
print()

#Division 2D array
arr16 = np.array([[7,3,2,6],[4,9,8,2]])
arr17 = np.array([[4,5,2,8],[8,2,4,3]])
div2d = arr16 / arr17
print(div2d)
print()

#modulus 1D array
arr18 = np.array([9,8,5,3])
arr19 = np.array([4,5,2,8])
mod = arr18 % arr19
print(mod)
print()

#modulus 2D array
arr20 = np.array([[7,2,5,8],[8,4,3,5]])
arr21 = np.array([[7,5,2,4],[4,5,3,2]])
mod2d = arr20 % arr21
print(mod2d)
print()

#power 1D array
arr22 = np.array([1,2,3,4])
power = arr22 ** 2
print(power)
print()
#power 2D array
arr23 = np.array([[9,8,7,6],
                  [4,3,2,5]])
power2d = arr23 ** 3
print(power2d)
print()

#reciprocal 1D array
arr24 = np.array([8,5,2,4])
rec = 1 / arr24
print(rec)
print()

#reciprocal 2D array
arr25 = np.array([[4,5,9,8],
                  [5,8,7,3]])
rec2d = 1 / arr25
print(rec2d)
print()
