# Data Gathering: Working with CSV Files

## Overview

**Data gathering is the backbone of any Machine Learning project. While building complex algorithms is important, an algorithm's performance is heavily dependent on the quality and quantity of data it receives. This session focuses on gathering data from **CSV (Comma Separated Values)** and **TSV (Tab Separated Values)** files, which are the most common formats in data science.**

## Key Concepts

* **Pandas **read_csv**:** The primary function used in Python to load delimited data.
* **Local vs. Remote Loading:** Loading files from a hard drive versus fetching data directly from a URL.
* **Parameter Tuning:** Customizing the import process to handle files without headers, encoding issues, or mismatched row lengths.
* **Memory Management:** Techniques like chunking to handle massive datasets that exceed RAM capacity.

## Detailed Explanation

**The video provides a comprehensive guide to the **pandas.read_csv()** function, exploring various parameters that solve real-world data loading problems.**

### 1. Basic Loading

* **Local File:** If the file is in the same directory, use **pd.read_csv('filename.csv')**.
* **From URL:** To fetch a CSV from a server (like GitHub), use the **requests** library to get the content and **io.StringIO** to convert the text into a format Pandas can read.

### 2. Handling Different Delimiters

* **Use the **sep** parameter. For TSV files, use **pd.read_csv('file.tsv', sep='\t')**.**

### 3. Header and Column Management

* **names**:** If a file lacks a header row, pass a list of names to define column titles.**
* **index_col**:** Sets a specific column (like **id**) as the index of the DataFrame to avoid redundant indexing.**
* **header**:** If the column names are accidentally treated as a data row, use **header=1** to skip to the correct line.**
* **usecols**:** Optimizes memory by importing only the specific columns needed for analysis.**

### 4. Handling Errors and Missing Data

* **encoding**:** Solves **UnicodeDecodeError** by specifying the character set (e.g., **latin-1**).**
* **error_bad_lines** (or **on_bad_lines**):** Skips rows that have too many values (extra commas), preventing the entire import from failing.**
* **na_values**:** Tells Pandas to treat specific strings (like "Male" or "-") as **NaN** (missing values).**

### 5. Data Types and Transformations

* **dtype**:** Explicitly defines column types (e.g., forcing a float column to stay as an integer) to save memory.**
* **parse_dates**:** Automatically converts string date columns into functional Python **datetime** objects.**
* **converters**:** Allows applying a custom function to a column **while** it is being loaded (e.g., shortening team names).**

## Important Definitions

* **CSV (Comma Separated Values):** A text file format that uses commas to separate values and newlines to separate records.
* **TSV (Tab Separated Values):** Similar to CSV but uses a tab character (**\t**) as the delimiter.
* **Encoding:** A system that assigns numbers to characters so they can be stored in a computer. Mismatched encoding is a common cause of file-reading errors.
* **Chunking:** The process of breaking a large dataset into smaller "chunks" to process them sequentially without crashing the system's memory.

## Examples / Use Cases

* **IPL Dataset:** Used **parse_dates** to enable time-based filtering and **converters** to change "Royal Challengers Bangalore" to "RCB".
* **Zomato Dataset:** Demonstrated the **encoding='latin-1'** parameter to fix loading errors caused by non-standard characters.
* **Book Recommender:** Used **error_bad_lines=False** to skip corrupt rows with excessive delimiters.

## Step-by-Step Explanation: Loading Huge Datasets

**If you have a file with millions of rows that crashes your RAM:**

* **Add the **chunksize** parameter: **dfs = pd.read_csv('huge_file.csv', chunksize=5000)**.**
* **This returns an iterable object rather than a DataFrame.**
* **Use a **for** loop to process each chunk:**

  ** code **Python**download**content_copy

  expand_less

  ```
  for chunk in dfs:
      # Perform operations like filtering or aggregation here
      print(chunk.shape)
  ```

## Key Takeaways

* **The **read_csv** function has over 15 parameters that can handle almost any structured text file issue.**
* **Memory efficiency** can be achieved by using **usecols**, **dtype**, and **chunksize**.
* **Data integrity** is maintained by using **parse_dates** and **na_values** during the initial load.

## Practical Notes

* **Always check the **encoding** if you get a **UnicodeDecodeError**.**
* **squeeze=True** converts a single-column DataFrame into a Series (Note: this is deprecated in newer versions; use **pd.read_csv(...).squeeze('columns')** instead).

## Interview / Exam Points

* **Q: How do you handle a CSV file that uses ';' instead of ','?**

  * **A: Use the **sep=';'** parameter in **pd.read_csv()**.**
* **Q: What is the benefit of using **dtype** during data loading?**

  * **A: It prevents Pandas from guessing types, which saves memory and prevents unexpected data conversion errors.**
* **Q: How do you read a file that is 10GB in size on a 4GB RAM machine?**

  * **A: Use the **chunksize** parameter to process the file in smaller batches.**

## Summary

**Gathering data from CSVs is more than just running a single line of code. By mastering the parameters of **read_csv**, you can automate cleaning tasks, manage system memory effectively, and handle various file errors before the data even enters your ML pipeline.**
