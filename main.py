import sqlite3
import pandas as pd

# STEP 1A
# Import SQL Library and Pandas Library

# STEP 1B
# Connect to the SQLite database
conn = sqlite3.connect('data.sqlite')

# STEP 2
# Assign employee number and last name
df_first_five = pd.read_sql("SELECT employeeNumber, lastName FROM employees", conn)

# STEP 3
# Employee number and last name in reverse order (last name first)
df_five_reverse = pd.read_sql("SELECT lastName, employeeNumber FROM employees", conn)

# STEP 4
# Employee number as 'ID' and last name
df_alias = pd.read_sql("SELECT lastName, employeeNumber AS 'ID' FROM employees", conn)

# STEP 5
# CASe statement to create new column 'role' with value 'Executive' for President, VP Sales, VP Marketing, and 'Not Executive' for others
df_executive = pd.read_sql("""
    SELECT *,
    CASE 
        WHEN jobTitle = "President" OR jobTitle = "VP Sales" OR jobTitle = "VP Marketing" THEN "Executive"
        ELSE "Not Executive"
    END AS role
    FROM employees
""", conn)

# STEP 6
# Length of last name as name_length
df_name_length = pd.read_sql("SELECT LENGTH(lastName) AS name_length FROM employees", conn)

# STEP 7
# First two Letters of job title as short_title
df_short_title = pd.read_sql("SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees", conn)



# STEP 8
# calculate total price of all orders by multiplying priceEach and quantityOrdered, 
# rounding to the nearest whole number, and summing the total price for all orders
#
result = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total 
    FROM orderDetails
""", conn)
sum_total_price = [result.iloc[0, 0]]

# STEP 9
# Return original order date and day, month, year as separate columns
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
    STRFTIME('%d', orderDate) AS day,
    STRFTIME('%m', orderDate) AS month,
    STRFTIME('%Y', orderDate) AS year
    FROM orders
""", conn)

# Close the connection
conn.close()