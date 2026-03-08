
# Tensors in Machine Learning

## 1. Introduction

In modern Machine Learning and Deep Learning,  **tensors are the fundamental data structures used to store numerical data** .

A tensor can be understood as a  **container for numbers arranged across multiple dimensions (axes)** .

You can think of tensors as a  **generalization of scalars, vectors, and matrices** .

Most machine learning libraries rely heavily on tensors, including:

* TensorFlow
* PyTorch
* NumPy

These libraries perform  **fast numerical computations using GPUs and TPUs** .

---

# 2. Tensor Rank (Number of Dimensions)

The **rank of a tensor** represents the **number of axes (dimensions)** it has.

```
Rank = Number of Axes = Number of Dimensions
```

| Structure | Example        | Rank | Description              |
| --------- | -------------- | ---- | ------------------------ |
| Scalar    | 5              | 0    | Single number            |
| Vector    | [1,2,3]        | 1    | List of numbers          |
| Matrix    | [[1,2],[3,4]]  | 2    | Table of numbers         |
| 3D Tensor | cube-like data | 3    | Collection of matrices   |
| 4D Tensor | image batches  | 4    | Collection of 3D tensors |
| 5D Tensor | video data     | 5    | Collection of 4D tensors |

---

# 3. Scalars (Rank 0 Tensor)

A **scalar** is a single numerical value.

Example:

```python
x = 7
```

Characteristics:

* No axes
* Single value
* Rank = 0

In NumPy:

```python
import numpy as np
x = np.array(7)
print(x.ndim)  # Output: 0
```

---

# 4. Vectors (Rank 1 Tensor)

A **vector** is a list of numbers arranged along a single axis.

Example:

```python
v = [10, 20, 30]
```

Characteristics:

* One axis
* Rank = 1
* Represents a point in space

Example in NumPy:

```python
v = np.array([10,20,30])
print(v.ndim)  # Output: 1
```

---

# 5. Matrices (Rank 2 Tensor)

A **matrix** is a 2D grid of numbers with rows and columns.

Example:

```python
m = [
    [1,2,3],
    [4,5,6]
]
```

Characteristics:

* Two axes
* Rank = 2
* Often used to represent datasets

Example:

```python
m = np.array([[1,2,3],[4,5,6]])
print(m.ndim)  # Output: 2
```

---

# 6. Higher Dimensional Tensors

Tensors can extend beyond matrices.

Hierarchy:

```
Scalar → Vector → Matrix → 3D Tensor → 4D Tensor → 5D Tensor
```

Each level is formed by  **collecting multiple objects of the previous level** .

Example:

* Vector = collection of scalars
* Matrix = collection of vectors
* 3D tensor = collection of matrices

---

# 7. Tensor Rank vs Vector Dimension

This is a common confusion.

### Tensor Rank

Tensor rank refers to  **number of axes** .

Example:

```
[1,2,3,4]
```

This is a  **1D tensor (Rank = 1)** .

### Vector Dimension

Vector dimension refers to  **number of elements inside the vector** .

Example:

```
[1,2,3,4]
```

This is a  **4-dimensional vector** .

### Key Difference

| Concept          | Meaning            |
| ---------------- | ------------------ |
| Tensor Rank      | Number of axes     |
| Vector Dimension | Number of elements |

Example:

```
[1,2,3,4,5]
```

* 5D vector
* Rank-1 tensor

---

# 8. Tensor Shape

The **shape of a tensor** describes the size along each axis.

Example:

```
(32, 256, 256, 3)
```

Meaning:

| Axis | Meaning        |
| ---- | -------------- |
| 32   | Batch size     |
| 256  | Image height   |
| 256  | Image width    |
| 3    | Color channels |

---

# 9. Tensor Size

Tensor size is the  **total number of elements inside the tensor** .

Example:

```
(32 × 256 × 256 × 3)
```

Total values stored inside the tensor.

---

# 10. Real Machine Learning Examples

## Example 1 — Tabular Data

Student dataset:

```
[CGPA, IQ, Age]
```

Example:

```
[3.5, 120, 21]
```

This is a  **3-dimensional vector** .

---

## Example 2 — Image Representation

Images are represented as  **3D tensors** .

```
Height × Width × Channels
```

Example:

```
256 × 256 × 3
```

Channels represent:

* Red
* Green
* Blue

---

## Example 3 — Batch of Images

Deep learning models process images in batches.

Shape:

```
Batch × Height × Width × Channels
```

Example:

```
32 × 256 × 256 × 3
```

This is a  **4D tensor** .

---

## Example 4 — Video Data

Videos add a  **time dimension (frames)** .

Shape:

```
Batch × Frames × Height × Width × Channels
```

Example:

```
16 × 30 × 224 × 224 × 3
```

This is a  **5D tensor** .

---

# 11. Why Tensors are Important in Machine Learning

Tensors allow efficient computation for:

* Matrix multiplication
* Neural network operations
* GPU acceleration
* Parallel processing

All modern deep learning frameworks operate primarily on tensors.

---

# 12. Quick Summary

| Data Structure | Tensor Rank |
| -------------- | ----------- |
| Scalar         | 0           |
| Vector         | 1           |
| Matrix         | 2           |
| 3D Tensor      | 3           |
| 4D Tensor      | 4           |
| 5D Tensor      | 5           |

Memory Tip:

```
Scalar → number
Vector → list
Matrix → table
Tensor → multi-dimensional array
```

---

# 13. Recommended Practice

Try creating tensors using:

* NumPy
* PyTorch
* TensorFlow

Example:

```python
import numpy as np

tensor = np.random.rand(3,4,5)
print(tensor.shape)
```
