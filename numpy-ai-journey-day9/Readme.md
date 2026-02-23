# 📅 Day 9 – NumPy Learning Journey (AI Engineer Roadmap)

## 🚀 Topic Covered:
- NumPy `copy()`
- NumPy `view()`
- Checking array ownership with `.base`

---

## 🧠 1️⃣ NumPy Copy

A **copy** creates a completely new array.

- Copy has its **own data**
- Changes in original array do NOT affect copy
- Changes in copy do NOT affect original

### ✅ Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
copy_arr = arr.copy()

arr[0] = 10

print("Original Array:", arr)
print("Copy Array:", copy_arr)

Original Array: [50  2  3  4  5]
View Array: [50  2  3  4  5]
```
🔎 3️⃣ Checking Array Ownership

We can check whether an array owns its data using .base

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
copy_arr = arr.copy()
view_arr = arr.view()

print(copy_arr.base)
print(view_arr.base)
📌 Output:
None
[1 2 3 4 5]

None → Owns data (Copy)

Not None → Shares data (View)

| Feature          | Copy  | View  |
| ---------------- | ----- | ----- |
| Own Data         | ✅ Yes | ❌ No  |
| Affects Original | ❌ No  | ✅ Yes |
| Memory Efficient | ❌ No  | ✅ Yes |

🎯 Why This Is Important for AI Engineers?

Understanding copy vs view is critical for:

Memory optimization

Large dataset handling

Avoiding unintended data modification

Writing efficient ML pipelines

📈 Progress Status

✔️ Day 9 Completed
✔️ Stronger understanding of NumPy memory behavior
🚀 Next Topic: joining & spliting numpy array
