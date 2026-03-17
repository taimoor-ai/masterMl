# Encoding Categorical Variables

In Machine Learning, **Feature Engineering** is often the difference between a mediocre model and a high-performing one. A critical part of this process is **Feature Transformation**, specifically handling categorical data. Since most mathematical models (like Linear Regression or Support Vector Machines) require numerical inputs, we must convert text-based categories into numbers.

---

## 1. Understanding Data Types

Before encoding, we must classify the data correctly. Data is broadly divided into two types:

1. **Numerical Data:** Continuous or discrete numbers (e.g., Age, Weight, Salary).
2. **Categorical Data:** Groups or labels (e.g., Color, Gender, Education).

### Categorical Data Sub-types

Categorical data is further divided based on whether the categories have an inherent order:

| Type              | Description                                               | Example                                                       | Encoding Technique         |
| :---------------- | :-------------------------------------------------------- | :------------------------------------------------------------ | :------------------------- |
| **Nominal** | No intrinsic ordering or relationship between categories. | Gender (Male, Female), States, Color.                         | **One-Hot Encoding** |
| **Ordinal** | Categories have a natural rank or sequence.               | Education (School < UG < PG), Review (Poor < Average < Good). | **Ordinal Encoding** |

---

## 2. Ordinal Encoding vs. Label Encoding

A common mistake among beginners is using these interchangeably. However, Scikit-Learn defines specific use cases for each:

### A. Ordinal Encoding (`OrdinalEncoder`)

* **Target:** Used for **Input Features ($X$)**.
* **Behavior:** It allows the user to define the rank/order of categories manually.
* **Logic:** Converts categories into integers (0, 1, 2...) based on the provided hierarchy.

### B. Label Encoding (`LabelEncoder`)

* **Target:** Used **ONLY** for the **Target Variable ($y$)**.
* **Behavior:** It automatically assigns integers to categories. It is primarily used for classification labels (e.g., converting "Yes/No" to 1/0).
* **Warning:** **Never** use `LabelEncoder` on input features ($X$); it is not designed to handle multiple columns and can lead to unintended mathematical bias if used on nominal data.

---

## 3. Implementation Workflow (Scikit-Learn)

### Step 1: Train-Test Split

Always perform the split before encoding to prevent **Data Leakage**. Your encoder should learn the mapping from the training set and simply apply it to the test set.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 0:2], df.iloc[:, -1], test_size=0.2)
```

### Step 2: Ordinal Encoding for Features ($X$)

You must pass a list of lists to the `categories` parameter to define the order.

```python
from sklearn.preprocessing import OrdinalEncoder

# Define the order: index 0 is the lowest rank
oe = OrdinalEncoder(categories=[['Poor', 'Average', 'Good'], ['School', 'UG', 'PG']])

# Fit on training data (learns categories)
oe.fit(X_train)

# Transform both sets
X_train_transformed = oe.transform(X_train)
X_test_transformed = oe.transform(X_test)
```

### Step 3: Label Encoding for Target ($y$)

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(y_train)

y_train_transformed = le.transform(y_train)
y_test_transformed = le.transform(y_test)
```

---

## 4. Visualizing the Transformation

Imagine an "Education" column:

**Original Data ($X$):**

1. PG
2. UG
3. School

**Ordinal Mapping Provided:** `['School', 'UG', 'PG']`

**Transformation Result:**

* PG $\rightarrow$ 2
* UG $\rightarrow$ 1
* School $\rightarrow$ 0

---

## 5. Real-World Applications

1. **E-commerce Sentiment Analysis:** Converting customer reviews ("Very Dissatisfied", "Neutral", "Very Satisfied") into numerical ranks to predict churn.
2. **Credit Scoring:** Ranking income levels ("Low", "Medium", "High") or employment types to calculate credit risk.
3. **HR Analytics:** Encoding employee performance ratings or education levels to predict promotions.

---

## 6. Quick Revision

* **Categorical Data** = Nominal (No Order) + Ordinal (Ordered).
* **Model Input ($X$):** If the feature is Ordinal, use `OrdinalEncoder`. If it is Nominal, use One-Hot Encoding (to be covered next).
* **Model Output ($y$):** Use `LabelEncoder`.
* **Manual Ordering:** In `OrdinalEncoder`, you must explicitly pass the order of categories, otherwise, it will assign numbers randomly/alphabetically, which might destroy the ordinal relationship.
* **Data Leakage:** Always `fit` on your training data and `transform` on your test data.

---

## 7. Pro-Tip: The Column Transformer

Encoding multiple columns separately (one for OHE, another for Ordinal) can be tedious. In advanced workflows, we use the **Column Transformer** to apply different encoding techniques to different columns in a single, clean step. *(Topic for future notes)*.
