import pandas as pd
import matplotlib.pyplot as plt

# Load a dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 150, 200, 250, 300, 350],
    "Expenses": [80, 120, 180, 200, 220, 300],
    "Profit": [20, 30, 20, 50, 80, 50]
}
df = pd.DataFrame(data)

# Line Plot
# df.plot(x="Month", y=["Sales", "Expenses"], kind="line", title="Sales vs. Expenses")
plt.plot(df["Month"], df["Sales"], label="Sales", marker='o')
plt.plot(df["Month"], df["Expenses"], label="Expenses", marker='o')
plt.plot(df["Month"], df["Profit"], label="Profit", marker='o')
plt.title("Sales vs. Expenses")
plt.xlabel("Month") 
plt.ylabel("Amount")
plt.legend()
plt.show()

# Bar Plot
df.plot(x="Month", y="Sales", kind="bar", color="skyblue", title="Monthly Sales")
plt.show()