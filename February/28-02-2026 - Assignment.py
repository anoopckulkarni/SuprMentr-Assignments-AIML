import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["A", "B", "C", "D"],
    "Sales": [120, 90, 150, 70],
    "Region": ["North", "South", "East", "West"],
    "Customer_Ages": [22, 25, 30, 28, 35, 40, 26, 29, 31, 27]
}

sales_df = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Sales": [120, 90, 150, 70]
})

ages = data["Customer_Ages"]

plt.figure()
plt.bar(sales_df["Product"], sales_df["Sales"])
plt.title("Product Sales Comparison")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

plt.figure()
plt.pie(sales_df["Sales"], labels=sales_df["Product"], autopct='%1.1f%%')
plt.title("Sales Distribution by Product")
plt.show()

plt.figure()
plt.hist(ages, bins=5)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()