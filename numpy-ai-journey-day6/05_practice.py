# 🔟 Mean Centering (Column-wise)
import numpy as np
arr = np.array([[10, 20],
                [30, 40],
                [50, 60]])
# Subtract column mean from each column using broadcasting.
col_mean = arr.mean(axis=0)
res = arr - col_mean
print(res)