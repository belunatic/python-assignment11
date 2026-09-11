import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#connect to the database
conn = sqlite3.connect('../db/lesson.db')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

#sql to dataframe
sql_statement='SELECT last_name, SUM(price * quantity) AS revenue FROM employees e JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id;'
df = pd.read_sql(sql_statement, conn)

#Bar plot
df.plot(x='last_name', y='revenue', kind='bar', color='green', title='Revenue by Employee')
plt.xlabel('Employee Last Name')
plt.ylabel('Revenue')
plt.show()