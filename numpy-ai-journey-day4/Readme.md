# 🚀 NumPy AI Journey – Day 4  
## 📅 Topic: Reshape & Flattening Arrays

Today I learned how to reshape arrays and convert multidimensional arrays into one-dimensional arrays using NumPy.

---

## 📚 What I Learned

### ✅ 1. Convert 1D Array to 2D Array

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)

print(reshaped)
```

Output:
```
[[1 2 3]
 [4 5 6]]
```

---

### ✅ 2. Convert 1D Array to 3D Array

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reshaped = arr.reshape(2, 2, 2)

print(reshaped)
```

Output:
```
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

---

### ✅ 3. Convert Multidimensional Array to 1D (Flattening)

```python
import numpy as np

mult_arr = np.array([[9, 8, 7], [6, 5, 4]])
arr = mult_arr.reshape(-1)

print(arr)
```

Output:
```
[9 8 7 6 5 4]
```

---

## 🧠 Key Concepts

- Total number of elements must remain the same while reshaping.
- `reshape()` changes structure, not data.
- `-1` allows NumPy to automatically calculate the dimension.
- Flattening is useful before feeding data into Machine Learning models.

---

## 📂 Files Created

- reshape_1d_to_2d.py  
- reshape_1d_to_3d.py  
- flattening_arrays.py  

---

## 🎯 Why This Matters for AI

Reshaping is essential in:
- Data preprocessing  
- Image data transformation  
- Neural network input formatting  
- Machine Learning pipelines  

Strong fundamentals in NumPy build a strong base for AI Engineering.
