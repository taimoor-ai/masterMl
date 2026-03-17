# One Hot Encoding: Handling Nominal Categorical Data

## 1. Introduction

In Machine Learning, mathematical algorithms (like Linear Regression, SVM, or Neural Networks) require numerical input. However, real-world datasets often contain **Categorical Data** (text/strings). To use this data, we must convert it into numbers.

**One Hot Encoding (OHE)** is the standard technique for handling **Nominal Categorical Data**.

---

## 2. Categorical Data Recap

Before choosing an encoding method, you must identify the type of categorical data:

| Type              | Definition                                     | Example                                             | Recommended Encoding       |
| :---------------- | :--------------------------------------------- | :-------------------------------------------------- | :------------------------- |
| **Nominal** | No intrinsic order or rank between categories. | Color (Red, Blue), Gender, States.                  | **One Hot Encoding** |
| **Ordinal** | A clear order or rank exists.                  | Education (School < UG < PG), Rating (Poor < Good). | **Ordinal Encoding** |

---

## 3. How One Hot Encoding Works

OHE creates a new binary column for every unique category in a feature.

### The Vector Representation

If a column "Color" has three categories: **Yellow, Blue, Red**, OHE transforms it into three columns. For each row, only one of these columns will have a value of `1` (the "hot" bit), and the others will be `0`.

**Original Data:**

| Color  | Target |
| :----- | :----- |
| Yellow | 1      |
| Blue   | 0      |
| Red    | 1      |

**OHE Transformed Data:**

| Color_Yellow | Color_Blue | Color_Red | Target |
| :----------: | :--------: | :-------: | :----: |
|      1      |     0     |     0     |   1   |
|      0      |     1     |     0     |   0   |
|      0      |     0     |     1     |   1   |

---

## 4. The Dummy Variable Trap & Multicollinearity

A common issue in OHE is the **Dummy Variable Trap**.

### The Concept

If you have $n$ categories, you can perfectly predict the $n^{th}$ category by knowing the values of the previous $n-1$ categories.

* *Example:* If `Color_Blue` is 0 and `Color_Red` is 0, the color **must** be Yellow.

### The Problem

This creates **Multicollinearity**, where input variables are highly correlated. This confuses linear models (Linear/Logistic Regression).

### The Solution

Always drop one of the encoded columns. If you have $n$ categories, use **$n-1$ columns**.

* **Yellow** is represented as `[0, 0]` in the Blue and Red columns.

---

## 5. Implementation: Pandas vs. Scikit-Learn

### A. Using Pandas (`pd.get_dummies`)

Best for quick Data Analysis and Visualization.

```python
import pandas as pd
# Basic OHE
df_encoded = pd.get_dummies(df, columns=['fuel', 'owner'])

# OHE with n-1 columns (Avoids Dummy Variable Trap)
df_encoded = pd.get_dummies(df, columns=['fuel', 'owner'], drop_first=True)
```

### B. Using Scikit-Learn (`OneHotEncoder`)

Best for **Machine Learning Pipelines**. Unlike Pandas, it "remembers" the categories from the training set and can handle new data consistently.

```python
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Initialize (drop='first' avoids the Dummy Variable Trap)
ohe = OneHotEncoder(drop='first', sparse=False, dtype=np.int32)

# Fit and transform
X_transformed = ohe.fit_transform(X[['fuel', 'owner']])
```

---

## 6. Handling High Cardinality (Too Many Categories)

If a column has many unique values (e.g., "Car Brand" with 32+ unique brands), OHE will create 32+ new columns, leading to the **Curse of Dimensionality**.

### The Strategy: Frequency-based Thresholding

1. Count the frequency of each category.
2. Set a threshold (e.g., categories appearing less than 100 times).
3. Group all infrequent categories into a single new label called **"Other"** or **"Uncommon"**.
4. Apply OHE to the remaining top categories.

**Example Logic:**

```python
counts = df['brand'].value_counts()
threshold = 100
repl = counts[counts <= threshold].index

# Replace rare brands and then apply OHE
df['brand'] = df['brand'].replace(repl, 'uncommon')
pd.get_dummies(df['brand'])
```

---

## 7. Quick Revision

* **OHE** is for **Nominal** data (no order).
* **Mechanism:** Creates $n$ binary columns for $n$ categories.
* **Dummy Variable Trap:** Results in multicollinearity; solved by using $n-1$ columns (`drop_first=True`).
* **Sparse Matrix:** OHE results in many zeros. Scikit-Learn stores this as a `sparse matrix` by default to save memory. Use `sparse=False` or `.toarray()` to view it as a standard array.
* ** cardinalty:** If categories are too many, club the rare ones into an "Other" category before encoding.
* **Pandas vs. Sklearn:** Use Pandas for EDA; use Scikit-Learn for Model Building and Pipelines.
