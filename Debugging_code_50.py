# 26. Wrong Pandas Column Name
# import pandas as pd

# df = pd.DataFrame({"Name": ["A", "B"], "Age": [20, 25]})
# print(df["age"])
# Task: Fix the error.
# Focus: Case sensitivity in Pandas

# Error: KeyError
# Wrong column name usage

# Output:
import pandas as pd

df = pd.DataFrame({"Name": ["A", "B"], "Age": [20, 25]})
print(df["Age"])   
# =================================================
# 27. NaN Conversion Error
# import pandas as pd

# df = pd.DataFrame({"age": [20, None, 30]})
# df["age"] = df["age"].astype(int)
# print(df)
# Task: Handle missing values correctly before conversion.
# Focus: Data cleaning 

# Error: 
# •	ValueError
# •	Wrong conversion usage
# •	None or NaN is considered missing data in Pandas. 
# •	cannot convert a column with missing values directly to int

# Output:
import pandas as pd

df = pd.DataFrame({"age": [20, None, 30]})

# Fill missing values (e.g., with 0) before converting
df["age"] = df["age"].fillna(0).astype(int)

print(df)
# =================================================
# 28. Wrong GroupBy Usage
# import pandas as pd

# df = pd.DataFrame({
#     "category": ["A", "A", "B"],
#     "sales": [100, 200, 300]
# })

# print(df.groupby("category")["sales"])
# Task: Modify the code to display aggregated sales totals.
# Focus: Grouping and aggregation 

# Error / Wrong Usage
# df.groupby("category")["sales"] creates a GroupBy object, it doesn’t automatically calculate totals.
# need to apply an aggregation function like sum(), mean(), etc., to see results.

# Output:
import pandas as pd

df = pd.DataFrame({
    "category": ["A", "A", "B"],
    "sales": [100, 200, 300]
})

# Group by category and sum sales
sales_totals = df.groupby("category")["sales"].sum()

print(sales_totals)
# =================================================
# 29. Incorrect DataFrame Filter
# import pandas as pd

# df = pd.DataFrame({"marks": [40, 60, 80]})
# print(df[df["marks" > 50]])
# Task: Correct the filtering logic.
# Focus: Boolean indexing

# Error: TypeError / Wrong Filtering Usage
# •	"marks" > 50 compares a string to a number → invalid. 
# •	To filter rows,need to compare the column itself, not the string name. 

# Output:
import pandas as pd

df = pd.DataFrame({"marks": [40, 60, 80]})

# Correct filter: compare the column
print(df[df["marks"] > 50])
# =================================================
# 30. Duplicate Removal Not Saved
# import pandas as pd

# df = pd.DataFrame({"id": [1, 1, 2], "name": ["A", "A", "B"]})
# df.drop_duplicates()
# print(df)
# Task: Fix the code so duplicates are actually removed.
# Focus: DataFrame updates

# Error
# drop_duplicates() does not modify the original DataFrame by default.
# either need to assign it back or use inplace=True.

# Output:
import pandas as pd

df = pd.DataFrame({"id": [1, 1, 2], "name": ["A", "A", "B"]})

# Assign the result back to df
df = df.drop_duplicates()

print(df)

import pandas as pd

df = pd.DataFrame({"id": [1, 1, 2], "name": ["A", "A", "B"]})

# Remove duplicates in place
df.drop_duplicates(inplace=True)

print(df)
# =================================================
# 31. Wrong Merge Key
# import pandas as pd

# df1 = pd.DataFrame({"id": [1, 2], "name": ["A", "B"]})
# df2 = pd.DataFrame({"emp_id": [1, 2], "salary": [5000, 6000]})

# merged = pd.merge(df1, df2, on="id")
# print(merged)
# Task: Debug the merge operation.
# Focus: Data wrangling

# Error:
# •	The column names in df1 and df2 must match if you use on="column_name". 
# •	Here, df1 has "id", but df2 has "emp_id". 
# •	This mismatch causes KeyError.

# Output:
import pandas as pd

df1 = pd.DataFrame({"id": [1, 2], "name": ["A", "B"]})
df2 = pd.DataFrame({"emp_id": [1, 2], "salary": [5000, 6000]})

# Merge using different column names
merged = pd.merge(df1, df2, left_on="id", right_on="emp_id")

print(merged)
# =================================================
# 32. Plotting Wrong Columns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.DataFrame({"month": [1, 2, 3], "sales": [100, 150, 200]})
# plt.plot(df["months"], df["sales"])
# plt.show()
# Task: Fix the chart.
# Focus: Visualization debugging

# Error:
# Column names are case-sensitive.
# DataFrame has "month" (no "s"), but the code tries "months".
# This causes a KeyError.

# Output:
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({"month": [1, 2, 3], "sales": [100, 150, 200]})

# Use correct column name
plt.plot(df["month"], df["sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()
# =================================================
# 33. Seaborn Dataset Variable Error
# import seaborn as sns

# df = sns.load_dataset("iris")
# sns.scatterplot(x="sepal_length", y="petal_length", data=data)
# Task: Correct the code.
# Focus: Variable reference

# Error:
# The DataFrame is stored in the variable df, but the code tries to use data.
# This causes a NameError.

# Output:
import seaborn as sns
import matplotlib.pyplot as plt
# Load dataset
df = sns.load_dataset("iris")
# Use the correct variable for data
sns.scatterplot(x="sepal_length", y="petal_length", data=df)
plt.show()
# =================================================
# 34. NumPy Shape Mismatch
# import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([[1, 2], [3, 4]])
# print(a + b)
# Task: Explain the error and fix the code properly.
# Focus: Array dimensions

# Error:
# Array a has shape (3,)
# Array b has shape (2,2)
# incompatible shapes

# Output:
import numpy as np
a = np.array([1, 2])             # shape (2,)
b = np.array([[1, 2], [3, 4]])   # shape (2,2)
print(a + b)
# =================================================
# 35. Wrong Reshape Size
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr.reshape(2, 3))
# Task: Correct the reshape operation.
# Focus: NumPy array shape

# Error:
# Total elements = 5 
# Requested shape = (2 × 3) = 6 elements

# Output:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.reshape(2, 3))

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.reshape(5, 1))
# =================================================
# 36. SQL WHERE with Aggregate
# SELECT department, COUNT(*) 
# FROM employees
# WHERE COUNT(*) > 5
# GROUP BY department;
# Task: Rewrite the query correctly.
# Focus: WHERE vs HAVING 

# Error:
# •	WHERE filters rows before grouping wrong
# •	COUNT(*) is an aggregate function (after grouping) 
# •	So it cannot be used in WHERE → causes an error
# •	WHERE → filters before GROUP BY 
# •	HAVING → filters after GROUP BY (aggregates)

# Output:
# SELECT department, COUNT(*) 
# FROM employees
# GROUP BY department
# HAVING COUNT(*) > 5;  
# =================================================
# # 37. SQL Wrong Join Column
# SELECT c.customer_name, o.order_total
# FROM customers c
# JOIN orders o
# ON c.id = o.order_id;
# Task: Identify and fix the join condition.
# Focus: SQL joins 
 
# Error:
# c.id = customer ID 
# o.order_id = order ID 
# These are different things, so the join is incorrect 
# should join using the common key → customer_id

# Output:
# SELECT c.customer_name, o.order_total
# FROM customers c
# JOIN orders o
# ON c.id = o.customer_id;  
# =================================================
# 38. SQL Update Without Filter
# UPDATE employees
# SET salary = 75000;
# Task: Rewrite the query to update only one employee.
# Focus: Safe SQL updates 

# Error:
# Without WHERE, the query updates every employee
# This is dangerous and can overwrite all data

# Output:
# UPDATE employees
# SET salary = 75000
# WHERE employee_id = 101;   
# =================================================
# 39. SQL Invalid Subquery Result
# SELECT name
# FROM employees
# WHERE department_id = (
#     SELECT department_id FROM departments
# );
# Task: Fix the subquery issue.
# Focus: Subqueries

# Error:
# The subquery returns multiple department_id values
# But = expects only one value
# This causes an error like:
# Error: Subquery returns more than 1 row

# Output:
# SELECT name
# FROM employees
# WHERE department_id IN (
#     SELECT department_id FROM departments
# );
# Returns employees whose department_id exists in the departments table
# SELECT name
# FROM employees
# WHERE department_id = (
#     SELECT department_id 
#     FROM departments
#     WHERE department_name = 'HR'
# );
# Use = → when subquery returns single value
# Use IN → when subquery returns multiple values
# =================================================
# 40. Wrong Window Function Use
# SELECT name, salary,
# RANK() OVER (salary DESC) AS rnk
# FROM employees;
# Task: Correct the syntax.
# Focus: Window functions 

# Error:
# Inside OVER(), must specify ORDER BY
# Just writing salary DESC is invalid syntax
# Window functions need a proper clause

# Output:
# SELECT name, salary,
# RANK() OVER (ORDER BY salary DESC) AS rnk
# FROM employees;
# =================================================
# 41. Scikit-learn Fit Argument Error
# from sklearn.linear_model import LinearRegression

# model = LinearRegression()
# X = [1, 2, 3, 4]
# y = [2, 4, 6, 8]

# model.fit(X, y)
# Task: Fix the input format for training.
# Focus: Model input shape

# Error:
# Scikit-learn expects X as 2D array (samples × features)
# But X is given as 1D list

# Output:
from sklearn.linear_model import LinearRegression
import numpy as np

model = LinearRegression()

X = np.array([1, 2, 3, 4]).reshape(-1, 1)  #make it 2D
y = [2, 4, 6, 8]

model.fit(X, y)

# Before:
# [1, 2, 3, 4]
# After:
# 1
# 2
# 3
# 4
# =================================================
# 42. Predict Before Fit
# from sklearn.linear_model import LogisticRegression

# model = LogisticRegression()
# print(model.predict([[5, 2]]))
# Task: Debug the workflow.
# Focus: ML model lifecycle

# Error:
# •	calling predict() before fit() 
# •	The model has not learned anything yet

# Output:
from sklearn.linear_model import LogisticRegression

# Sample training data
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]

model = LogisticRegression()

# Step 1: Train the model
model.fit(X, y)

# Step 2: Predict
print(model.predict([[5, 2]]))
# =================================================
# 43. Wrong Train-Test Split Assignment
# from sklearn.model_selection import train_test_split

# X = [[1], [2], [3], [4]]
# y = [2, 4, 6, 8]

# X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2)
# Task: Correct the variable assignment order.
# Focus: Data splitting

# Error:
# train_test_split() returns values in this order:
# X_train, X_test, y_train, y_test
# But assigned them incorrectly → data gets mismatched

# Output:
from sklearn.model_selection import train_test_split
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]
# Correct order
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train, X_test, y_train, y_test)
# =================================================
# 44. Accuracy Calculation Mismatch
# from sklearn.metrics import accuracy_score

# y_true = [1, 0, 1]
# y_pred = [1, 0]

# print(accuracy_score(y_true, y_pred))
# Task: Fix the evaluation issue.
# Focus: Prediction length consistency

# Error:
# •	y_true has 3 values 
# •	y_pred has 2 values 
# •	Both must have same number of elements

# Output:
from sklearn.metrics import accuracy_score

y_true = [1, 0, 1]
y_pred = [1, 0, 1]   #  same length as y_true

print(accuracy_score(y_true, y_pred))
# =================================================
# 45. Wrong Classification Problem Statement
# from sklearn.linear_model import LinearRegression

# X = [[1], [2], [3], [4]]
# y = ["Yes", "No", "Yes", "No"]

# model = LinearRegression()
# model.fit(X, y)
# Task: Replace the wrong model with a suitable one.
# Focus: Model selection

# Error:
# LinearRegression is used for continuous numeric output 
# target y has categorical values ("Yes", "No")
# This is a classification problem, not regression

# Output:
from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4]]
y = ["Yes", "No", "Yes", "No"]

model = LogisticRegression()   #suitable for classification
model.fit(X, y)
# =================================================
# 46. PySpark Column Reference Error
# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName("test").getOrCreate()
# df = spark.createDataFrame([(1, 100), (2, 200)], ["id", "sales"])

# df.select("amount").show()
# Task: Fix the column issue.
# Focus: Spark DataFrame debugging

# Error:
# DataFrame has columns: "id" and "sales"
# trying to select "amount" 

# Output:
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("test").getOrCreate()
df = spark.createDataFrame([(1, 100), (2, 200)], ["id", "sales"])
df.select("sales").show()   #  correct column
# =================================================
# 47. PySpark Join Mistake
# joined_df = transactions_df.join(customers_df, on="customer", how="inner")
# joined_df.show()
# Task: Correct the join key.
# Focus: Big data transformation 

# Error:
# Column "customer" may not exist in both DataFrames 
# Join requires a common column name in both tables
# Usually, the correct key is something like "customer_id"

# Output:
# joined_df = transactions_df.join(customers_df, on="customer_id", how="inner")
# joined_df.show()

# joined_df = transactions_df.join(
#     customers_df,
#     transactions_df.customer_id == customers_df.id,
#     "inner"
# )
# =================================================
# 48. Debugging Numeric Conversion
# import pandas as pd

# df = pd.DataFrame({"Sales": ["100", "250", "N/A", "400"]})
# df["Sales"] = df["Sales"].astype(float)
# print(df)
# Task: Explain the error and correct the code professionally.
# Focus: Real-world debugging with dirty data 

# Error:
# Column "Sales" contains non-numeric value → "N/A"
# astype(float) cannot convert "N/A" to a number

# Output:
import pandas as pd

df = pd.DataFrame({"Sales": ["100", "250", "N/A", "400"]})

# Convert safely, invalid values → NaN
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

print(df)
# =================================================
# 49. Wrong Correlation Call
# import pandas as pd

# df = pd.DataFrame({
#     "hours": [2, 4, 6],
#     "marks": [50, 70, 90]
# })

# print(df.correlation())
# Task: Fix the code to calculate correlation properly.
# Focus: EDA methods

# Error:
# AttributeError (Wrong method name)
# Pandas does not have a method called correlation() 
# The correct method is .corr()

# Output:
import pandas as pd

df = pd.DataFrame({
    "hours": [2, 4, 6],
    "marks": [50, 70, 90]
})

print(df.corr())   # correct method
# =================================================
# 50. End-to-End Debugging Task
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("sales.csv")
# df["OrderDate"] = pd.to_datetime(df["order_date"])
# df["TotalSales"] = df["Quantity"] * df["price"]

# monthly_sales = df.groupby("OrderDate")["TotalSales"].sum()
# plt.bar(monthly_sales.index, monthly_sales.values)
# plt.show()
# Task: Review the full script, identify all possible issues, and produce a corrected version.
# Focus: End-to-end debugging, column consistency, date handling, aggregation, visualization

# Errors:
# 1.Column Name Mismatch
# "OrderDate" vs "order_date" 
# "Quantity" vs "price" (case inconsistency risk)
# 2.Date Handling Issue
# Grouping by full date → gives daily, not monthly 
# 3.Aggregation Issue
# Need monthly aggregation, not raw dates
# 4.Visualization Issue
# Too many dates → cluttered bar chart 

# Output:
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales.csv")

# Standardize column names (optional but good practice)
df.columns = df.columns.str.lower()

# Convert to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Create total sales
df["total_sales"] = df["quantity"] * df["price"]

# Extract month (YYYY-MM format)
df["month"] = df["order_date"].dt.to_period("M")

# Group by month
monthly_sales = df.groupby("month")["total_sales"].sum()

# Convert index to string for plotting
monthly_sales.index = monthly_sales.index.astype(str)

# Plot
plt.figure()
plt.bar(monthly_sales.index, monthly_sales.values)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales")
plt.xticks(rotation=45)
plt.show()
# =================================================



















