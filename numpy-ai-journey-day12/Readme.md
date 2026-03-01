# 🚀 Day 12 – NumPy Learning (AI Engineer Journey)

## 📚 Today’s Topics:
- Flatten Array
- Shuffle Array
- Unique Values
- Resize Array

Today I explored some powerful NumPy array manipulation functions that are very useful in data preprocessing and AI workflows.

---

# 🔹 1. Flatten Array

Flatten converts a multi-dimensional array into a 1D array.

### ✅ Example:

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

flat_arr = arr.flatten()
print(flat_arr)
```

### 🧠 Output:
```
[1 2 3 4 5 6]
```

📌 Used when converting matrix data into a single vector (common in ML preprocessing).

---

# 🔹 2. Shuffle Array

Shuffle randomly changes the order of elements in an array.

### ✅ Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

np.random.shuffle(arr)
print(arr)
```

📌 Important in AI for randomizing datasets before training models.

---

# 🔹 3. Unique Values

The `np.unique()` function returns unique elements from an array.

### ✅ Example:

```python
import numpy as np

arr = np.array([1, 2, 2, 3, 4, 4, 5])

unique_values = np.unique(arr)
print(unique_values)
```

### 🧠 Output:
```
[1 2 3 4 5]
```

📌 Useful for removing duplicates and analyzing categorical data.

---

# 🔹 4. Resize Array

Resize changes the shape of an array.

### ✅ Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])

resized_arr = np.resize(arr, (2, 3))
print(resized_arr)
```

### 🧠 Output:
```
[[1 2 3]
 [4 1 2]]
```

📌 If new size is larger, NumPy repeats elements automatically.

---

# 🎯 Key Learnings

- Flatten helps convert matrices into vectors.
- Shuffle is important for dataset randomization.
- Unique removes duplicate elements.
- Resize changes shape but may repeat data.

---

# 💡 Reflection

Every small concept builds the base of AI Engineering.  
Today I strengthened my understanding of array manipulation — an essential skill for data preprocessing in Machine Learning.

---

🔥 12 Days Done.
Consistency > Motivation.
AI Engineer in Progress.

— Rahul Swain
