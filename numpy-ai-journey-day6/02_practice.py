# 7️⃣ Broadcasting with Different Dimensions
import numpy as np
a = np.array([[1], [2], [3]])   # shape (3,1)
b = np.array([10, 20, 30])      # shape (3,)


# Add a + b.
res = a + b
print(res)
# What is result shape? (3,3)