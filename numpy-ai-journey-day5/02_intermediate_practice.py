# 2D Array Indexing (6–10)
# Use this array for Q6–Q10:
import numpy as np

arr = np.array([
     [10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]
 ])

# 6. Print element 50.
print(arr[1,1])
# 7. Print the entire second row.
print(arr[1])
# 8. Print the entire third column.
print(arr[0:3,2])
# 9. Slice and print this submatrix:
# [[10, 20],
#  [40, 50]]
print(arr[0:2,0:2])
# 10. Replace 80 with 800 using indexing.
arr[2,1] = 800
print(arr)
# 🔹 Boolean & Conditional Indexing (11–13)
# Use:
arr1 = np.array([5, 12, 7, 18, 3, 21])
# 11. Print all elements greater than 10.
print(arr1[arr1 > 10])
# 12. Print all even numbers.
print(arr1[arr1 % 2 == 0])
# 13. Replace all numbers less than 10 with 0.
arr1[arr1 < 10] = 0
print(arr1)