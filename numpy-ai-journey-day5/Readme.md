# 📅 Day 5 – NumPy (Indexing & Slicing)
## 🚀 AI Engineer Journey

Today I focused on mastering NumPy Indexing and Slicing.

Indexing and slicing are core skills for:
- Data manipulation
- Image processing
- Neural network inputs
- Matrix operations

---

## 📌 Topics Covered

### 🔹 1D Array Indexing
- Positive indexing
- Negative indexing
- Accessing specific elements

### 🔹 2D Array Indexing
- Accessing rows
- Accessing columns
- Accessing specific elements using row & column indices

### 🔹 Slicing Techniques
- Basic slicing `[start:stop]`
- Step slicing `[::step]`
- Reverse slicing `[::-1]`
- 2D row and column slicing

### 🔹 Advanced Practice
- Sub-matrix extraction
- Pattern-based slicing
- Multi-dimensional slicing

---

## 🧠 Practice Completed

✅ 15 Practice Questions (Basic → Hard)

Examples:
- Print 4th element
- Print last element using negative indexing
- Slice from index 2 to 6
- Reverse array using slicing
- Print every 2nd element
- Extract specific rows & columns from 2D arrays

---

## 💻 Sample Code

```python
import numpy as np

# Create 1D array
arr = np.arange(1, 11)

print("Array:", arr)

# Indexing
print("4th element:", arr[3])
print("Last element:", arr[-1])

# Slicing
print("Elements from index 2 to 6:", arr[2:7])
print("Reverse array:", arr[::-1])
print("Every 2nd element:", arr[::2])


# 2D Example
matrix = np.arange(1, 17).reshape(4, 4)

print("Matrix:\n", matrix)

print("First row:", matrix[0])
print("Second column:", matrix[:, 1])
print("Sub-matrix:\n", matrix[1:3, 1:3])
```

---

## 🎯 Why This Matters for AI

- Neural networks use multi-dimensional arrays
- Image data is stored as matrices
- Dataset slicing is essential for training models
- Efficient indexing improves performance

---

## 📍 Progress

- ✅ NumPy Basics
- ✅ Indexing & Slicing
- ⏭ Next: Boolean Indexing & Broadcasting

---

Consistency > Motivation  
Day 5 Complete.
