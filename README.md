# 📊 NumPy Foundation for AI

## 🚀 Overview

This repository contains my foundational learning of NumPy as part of my AI Engineer journey.

Today I covered:
- What is NumPy
- What is NumPy Array
- Importance of NumPy
- Python List vs NumPy Array
- Creating 1D, 2D, 3D arrays
- Zeros, Ones, Empty arrays
- Arange
- Linspace
- Diagonal Array

---

## 📌 1. What is NumPy?

NumPy (Numerical Python) is a powerful Python library used for:
- Scientific computing
- Mathematical operations
- Working with multi-dimensional arrays
- Linear algebra
- Random number generation

NumPy is faster and more memory efficient than Python lists.

---

## 📌 2. What is NumPy Array?

A NumPy array:
- Stores elements of the same data type
- Supports vectorized operations
- Is optimized for performance

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
```

---

## 📌 3. Importance of NumPy

- Faster computation
- Less memory usage
- Used in AI, ML, Data Science
- Supports multi-dimensional arrays
- Provides built-in mathematical and logical operations

---

## 📌 4. Python List vs NumPy Array

| Feature | Python List | NumPy Array |
|----------|-------------|-------------|
| Speed | Slower | Faster |
| Data Type | Mixed allowed | Same type only |
| Memory Usage | Higher | Lower |
| Math Operations | Limited | Powerful |

---

## 📌 5. Creating Arrays

### 1D Array
```python
arr = np.array([1,2,3,4])
```

### 2D Array
```python
arr_2d = np.array([[2,4,8,10],
                   [10,12,14,16]])
```

### 3D Array
```python
arr_3d = np.array([[[1,7,8,4,9],
                    [12,21,14,18,19]],
                   [[16,65,75,84,63],
                    [89,94,98,74,91]]])
```

---

## 📌 6. Special Array Functions

### Zeros
```python
np.zeros((4,8))
```

### Ones
```python
np.ones((8,16))
```

### Empty
```python
np.empty((2,3))
```

### Arange
```python
np.arange(1, 10, 2)
```

### Linspace
```python
np.linspace(0, 10, 5)
```

### Diagonal Array
```python
np.diag([1,2,3])
```

---

## 🎯 Next Learning Target

- Random number function
- Datatypes in numpy array
- arithmatic operator
- arithmatic function
- shape & reshape

---

### 👨‍💻 Author
Rahul Swain  
AI Engineer in Progress 🚀
