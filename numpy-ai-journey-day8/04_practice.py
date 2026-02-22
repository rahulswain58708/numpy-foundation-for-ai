# 4️⃣ Count Numbers Greater Than 25
# Array: [10, 35, 50, 5, 60, 15]
# Count how many numbers are greater than 25 using iteration.
import numpy as np
arr = np.array([10, 35, 50, 5, 60, 15])
count = 0
for element in np.nditer(arr):
    if element > 25:
        count += 1
print(count)