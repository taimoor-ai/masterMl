# Feature Engineering: Working with Date and Time

In Machine Learning, raw date and time strings are almost useless. To extract value from temporal data, we must perform **Feature Engineering**—the process of decomposing a timestamp into multiple meaningful attributes that a model can understand.

---

## 1. The Core Challenge

When you import a dataset using Pandas, date and time columns are usually treated as **Objects (Strings)**.

* **Problem:** Models cannot perform math on "2023-12-25".
* **Solution:** Convert the column to a `datetime64` object.

### Conversion Logic

```python
import pandas as pd

# Convert string to datetime object
df['date'] = pd.to_datetime(df['date'])
```

Once converted, you gain access to the `.dt` accessor, which allows you to extract specific temporal properties.

---

## 2. Basic Feature Extraction (Date)

A single date contains multiple "hidden" features. By extracting them, we allow the model to find patterns related to seasonality or specific times of the month.

| Feature              | Code                           | Output Example    |
| :------------------- | :----------------------------- | :---------------- |
| **Year**       | `df['date'].dt.year`         | 2019, 2023        |
| **Month**      | `df['date'].dt.month`        | 1 to 12           |
| **Month Name** | `df['date'].dt.month_name()` | January, December |
| **Day**        | `df['date'].dt.day`          | 1 to 31           |

---

## 3. Advanced Temporal Features

Often, the most predictive power comes from derived logic, such as identifying weekends or specific business cycles.

### A. Day of the Week

Extracting the day number (0 for Monday, 6 for Sunday) or the day name.

```python
df['day_of_week'] = df['date'].dt.dayofweek
df['day_name'] = df['date'].dt.day_name()
```

### B. Weekend Indicator

Models often behave differently on weekends (e.g., higher e-commerce sales). We can create a boolean/binary feature:

```python
import numpy as np
df['is_weekend'] = np.where(df['day_name'].isin(['Sunday', 'Saturday']), 1, 0)
```

### C. Quarters and Semesters

Useful for financial or retail data where performance is tracked in cycles.

* **Quarter:** `df['date'].dt.quarter` (1 to 4)
* **Semester:**
  ```python
  df['semester'] = np.where(df['quarter'].isin([1, 2]), 1, 2)
  ```

---

## 4. Time-Based Feature Extraction

If your timestamp includes hours, minutes, and seconds, you can extract features relevant to "time-of-day" patterns.

```text
Timestamp: 2023-04-21 15:30:45
   |
   |-- Hour: 15 (Useful for identifying morning/afternoon/night)
   |-- Minute: 30
   |-- Second: 45
   |-- Time: 15:30:45 (Isolated time part)
```

**Implementation:**

```python
df['hour'] = df['date'].dt.hour
df['min'] = df['date'].dt.minute
df['sec'] = df['date'].dt.second
```

---

## 5. Time Delta (Elapsed Time)

Calculating the difference between two dates is one of the most powerful features (e.g., "Days since last purchase" or "Age of the account").

### Calculating Time Difference

```python
import datetime

today = datetime.datetime.now()
df['elapsed_time'] = today - df['date']

# Extracting specific units from the difference
df['days_passed'] = df['elapsed_time'].dt.days
df['months_passed'] = df['elapsed_time'] / np.timedelta64(1, 'M') # Approximate months
```

---

## 6. Real-World Applications

1. **E-commerce:**
   * **Feature:** `is_weekend`.
   * **Application:** Identifying that users spend more on Saturdays.
2. **Expense Trackers:**
   * **Feature:** `month`.
   * **Application:** Analyzing monthly spending habits and predicting next month's budget.
3. **Logistics/Delivery:**
   * **Feature:** `hour`.
   * **Application:** Predicting traffic delays based on peak hours.
4. **Finance:**
   * **Feature:** `quarter`.
   * **Application:** Forecasting stock performance based on quarterly earnings reports.

---

## 7. Quick Revision Section

* **Step 1:** Always use `pd.to_datetime()` first.
* **Step 2:** Use `.dt` to access year, month, day, hour, etc.
* **Step 3:** Convert months/days to names using `.dt.month_name()` or `.dt.day_name()` for visualization, but keep numeric versions for the model.
* **Step 4:** Use `np.where` to create flags like `is_weekend` or `semester`.
* **Step 5:** Subtract dates to find the **Duration** or **Delta**, which is often more predictive than the raw date itself.
