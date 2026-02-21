# 5️⃣ Compute Mean Centering
import numpy as np
arr = np.array([10, 20, 30, 40])
mn = arr.mean()
# 👉 Har element se array ka mean subtract karo.
sub = arr - mn
print(sub)