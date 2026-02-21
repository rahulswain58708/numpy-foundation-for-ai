# 3️⃣ Even Numbers Filter
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# 👉 Sirf even numbers nikaalo using vectorization.
even_number = arr[ arr % 2 == 0]
print(even_number)
