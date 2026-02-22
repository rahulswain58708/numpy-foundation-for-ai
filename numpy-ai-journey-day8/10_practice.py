# 🔟 Iterate With Index (Advanced)

# Using np.ndenumerate() print both index and value of:

# [[10,20],
#  [30,40]]

# Expected output format:

# Index (0,0) Value 10
# Index (0,1) Value 20
# ...

import numpy as np
arr = np.array([[10,20],
                [30,40]])
for idx,value in np.ndenumerate(arr):
    print(f"Index {idx} Value {value}")