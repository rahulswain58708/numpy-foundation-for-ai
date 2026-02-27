# 🚀 Day 11 – NumPy Learning | AI Engineering Journey

## 📅 Date:
27 Feb 2026

## 📚 Topics Covered:
- NumPy Searching
- NumPy Sorting
- NumPy Filtering

---

## 🔍 NumPy Searching

### Using np.where()

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = np.where(arr == 30)

print(result)
```

### Using np.searchsorted()

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

position = np.searchsorted(arr, 35)

print(position)
```

---

## 📊 NumPy Sorting

### Using np.sort()

```python
import numpy as np

arr = np.array([5, 2, 8, 1, 9])

sorted_arr = np.sort(arr)

print(sorted_arr)
```

### Using np.argsort()

```python
import numpy as np

arr = np.array([5, 2, 8, 1, 9])

index_order = np.argsort(arr)

print(index_order)

# Reordering manually
sorted_manual = arr[index_order]

print(sorted_manual)
```

---

## 🎯 NumPy Filtering

### Filter values greater than 15

```python
import numpy as np

arr = np.array([5, 12, 25, 7, 30, 18])

filtered = arr[arr > 15]

print(filtered)
```

### Filter values between 10 and 30

```python
import numpy as np

arr = np.random.randint(1, 40, 15)

filtered = arr[(arr >= 10) & (arr <= 30)]

print("Original Array:", arr)
print("Filtered Array:", filtered)
```

---

## 🧠 Practice Completed:
- Searched elements using conditions
- Found insertion positions
- Sorted arrays
- Used argsort for index-based sorting
- Filtered data using boolean indexing

---

## 💡 Learning Reflection

Day 11 completed successfully.
Understanding search, sort, and filtering is important for data preprocessing in AI and Machine Learning.

Consistency builds mastery.

---

🔥 Rahul Swain  
AI Engineer in Progress
