# 🚀 Day 6 – NumPy AI Engineer Journey

## 📅 Progress Update
Today I learned **NumPy Broadcasting** and solved 10 practice questions.

Broadcasting allows NumPy to perform element-wise operations on arrays of different shapes without using loops.

---

## 📚 What I Learned

### ✅ What is Broadcasting?
Broadcasting is a mechanism that allows NumPy to automatically expand smaller arrays so they can match the shape of larger arrays during operations.

### ✅ Broadcasting Rules
1. If arrays have different dimensions, NumPy pads the smaller shape with 1s on the left.
2. Two dimensions are compatible if:
   - They are equal  
   - OR one of them is 1  
3. If neither condition is satisfied → It raises an error.

---

## 🧠 Why Broadcasting is Important for AI

- Removes the need for loops
- Makes code faster
- Improves performance for large datasets
- Essential for ML and Deep Learning computations
- Used in normalization, scaling, and matrix operations

---

## 💻 Practice Completed (10 Questions)

- 1D + 2D array addition
- Scalar broadcasting
- Row-wise broadcasting
- Column-wise broadcasting
- Mean centering
- Row normalization
- Shape compatibility checks
- (3,1) + (3,) shape expansion
- Conditional broadcasting
- Advanced dimension matching

---

## 🔥 Example Code

```python
import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([[4, 5, 6],
               [1, 3, 7]])

result = a1 + a2
print(result)

# Output:
# [[ 5  7  9]
#  [ 2  5 10]]
```

---

## 🏗 Skills Improved

- Understanding array shapes
- Thinking in dimensions
- Row-wise vs Column-wise operations
- Writing optimized NumPy code
- Vectorized mindset

---

## 🎯 Next Goal

- Learn NumPy Vectorization
- Practice 10 mixed problems
- Strengthen mathematical thinking

---

Day 6 Complete ✅  
Consistency > Motivation
