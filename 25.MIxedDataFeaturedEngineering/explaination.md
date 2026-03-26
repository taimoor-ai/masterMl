# Feature Engineering: Handling Mixed Variables

In real-world datasets, variables are rarely perfectly formatted. One of the most challenging types of data to clean is **Mixed Variables**. This note explores how to identify, categorize, and transform these variables for Machine Learning models.

---

## 1. What are Mixed Variables?

A **Mixed Variable** is a feature that contains both numbers and labels (categorical data). Since Machine Learning models require numerical input, leaving these variables as strings or objects leads to a loss of valuable information.

### The Two Types of Mixed Variables

| Type                             | Description                                                           | Example                              |
| :------------------------------- | :-------------------------------------------------------------------- | :----------------------------------- |
| **Type 1: Intra-cell Mix** | Numbers and characters are combined within a single value/string.     | `Cabin: B5`, `Ticket: A/5 21171` |
| **Type 2: Inter-row Mix**  | Some rows contain purely numbers, while others contain purely labels. | `Rating: 1, 2, 3, "Missing", "A+"` |

---

## 2. Visualizing the Problem

### Case A: Cabin Number (Intra-cell)

Information is "hidden" in the string. `B` might represent the Deck (categorical), and `5` represents the specific Room Number (numerical).

```text
[ Cabin ]             [ Deck ]   [ Room ]
|  B5   |    --->     |  B   |   |  5   |
|  C23  |    --->     |  C   |   |  23  |
```

### Case B: Passengers Traveling (Inter-row)

A column meant for numbers might have categorical labels injected during data entry.

```text
[ Number ]            [ Num_Part ]   [ Cat_Part ]
|   5    |   --->     |    5     |   |   NaN    |
|   A    |   --->     |   NaN    |   |    A     |
```

---

## 3. Transformation Strategies

### Strategy 1: Handling "Inter-row" Mixed Data

This strategy is used when a column contains distinct numeric values and distinct labels in different rows.

**The Process:**

1. Create a **Numerical Column**: Convert labels to `NaN` (null) and keep numbers.
2. Create a **Categorical Column**: Convert numbers to `NaN` and keep labels.

**Python Implementation:**

```python
import pandas as pd
import numpy as np

# 1. Extract Numerical Part
# errors='coerce' turns non-numeric strings into NaN
df['number_numerical'] = pd.to_numeric(df['number'], errors='coerce')

# 2. Extract Categorical Part
# If the numerical part is null, it means the original was a string
df['number_categorical'] = np.where(df['number_numerical'].isnull(), df['number'], np.nan)
```

---

### Strategy 2: Handling "Intra-cell" Mixed Data (Regex)

This strategy uses Regular Expressions (Regex) to pull out substrings.

**The Process:**

1. **Extract Numbers:** Find the digits within the string.
2. **Extract Labels:** Find the alphabetic characters (often the prefix).

**Python Implementation:**

```python
# Extracting digits (\d+) from the 'cabin' column
df['cabin_num'] = df['cabin'].str.extract('(\d+)') 

# Extracting the first character (Deck letter)
df['cabin_cat'] = df['cabin'].str[0] 
```

---

## 4. Real-World Applications

* **Financial Services:** Transaction IDs often look like `TXN102938`, where `TXN` is the type and the digits are the sequence.
* **Logistics/E-commerce:** SKU codes like `ELEC-992-BLK`. Breaking this into `Category`, `Product ID`, and `Color` provides better features for demand forecasting.
* **Healthcare:** Medical codes that combine a department prefix with a patient number.
* **Aviation/Travel:** Seat numbers (e.g., `12A`, `14C`). `12` is the row (numerical distance from the cockpit), and `A` is the seat position (window/aisle).

---

## 5. Why do we do this? (Advanced Perspective)

1. **Reducing Cardinality:** A column like `Cabin` might have 150 unique values (High Cardinality), making it hard to One-Hot Encode. By extracting the `Deck` letter (e.g., A, B, C), we reduce 150 unique values to 7-8 categories, which is much easier for a model to learn from.
2. **Capturing Trends:** In seat numbers (e.g., `12A`), the number `12` represents how far back the passenger is. This numerical relationship is lost if the whole value is treated as a categorical label.
3. **Handling Missing Values:** Splitting allows us to handle missing data differently for the categorical part versus the numerical part (e.g., imputing the median for numbers but using "Missing" for categories).

---

## 6. Quick Revision Summary

* **Mixed Variable:** A feature with both numbers and strings.
* **Detection:** Use `df['column'].unique()` to spot patterns of mixed data.
* **Tools:**
  * `pd.to_numeric(errors='coerce')` for splitting rows of different types.
  * `.str.extract()` with Regex for pulling numbers out of strings.
* **Goal:** Turn one "dirty" column into two "clean" columns (one numeric, one categorical) to maximize the information available to the Machine Learning algorithm.
