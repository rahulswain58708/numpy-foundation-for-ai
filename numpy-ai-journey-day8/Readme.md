# 📅 Day 8 – NumPy Learning Journey (AI Engineer)

## 🚀 Topic Covered: Iterating in NumPy

Today I learned how to iterate over NumPy arrays efficiently.

---

## 📚 Concepts Covered

### 1️⃣ Iterating 1D Array

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

for x in arr:
    print(x)
```

---

### 2️⃣ Iterating Using np.nditer()

```python
import numpy as np

arr = np.array([[10, 20],
                [30, 40]])

for x in np.nditer(arr):
    print(x)
```

---

### 3️⃣ Iterating with Index using np.ndenumerate()

```python
import numpy as np

arr = np.array([[10, 20],
                [30, 40]])

for idx, value in np.ndenumerate(arr):
    print(f"Index {idx} Value {value}")
```

✔ Output:
```
Index (0, 0) Value 10
Index (0, 1) Value 20
Index (1, 0) Value 30
Index (1, 1) Value 40
```

---

## 🧠 Key Learnings

- NumPy supports iteration over multi-dimensional arrays.
- `np.nditer()` allows single-loop iteration.
- `np.ndenumerate()` provides both index and value.
- In AI projects, vectorization is preferred over loops for better performance.

---

## 🔜 Next Topic: Copy vs View in NumPy

Tomorrow I will learn:

- What is Copy?
- What is View?
- Memory sharing concept
- `.copy()` vs `.view()`
- Performance implications

---

## 🎯 AI Engineer Journey

Day 8 Completed ✅  
Building strong NumPy foundations for AI Engineering.
Consistency is the real superpower.
