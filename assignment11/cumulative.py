import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('../db/lesson.db')
conn.execute("PRAGMA foreign_keys = 1")

#sql to dataframe
sql_statement = '''
SELECT o.order_id, SUM(price * quantity) AS total_price
FROM orders o
JOIN line_items l 
ON o.order_id = l.order_id
JOIN products p 
ON l.product_id = p.product_id
GROUP BY o.order_id
'''

df = pd.read_sql(sql_statement, conn)

#add the cummulative sum column
df['cumulative_sum'] = df['total_price'].cumsum()

print(df.head(15))

df.plot(x="order_id", y="cumulative_sum", kind="line", title="Revenue Vs Order_id")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Sum")
plt.show()
