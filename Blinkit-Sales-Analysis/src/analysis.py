import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("data/raw/blinkit_data.csv")

print("="*50)
print("BLINKIT SALES DATASET")
print("="*50)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

# ==========================
# Total Sales
# ==========================

total_sales = df["Sales"].sum()

print("\nTotal Sales:", total_sales)

# ==========================
# Total Orders
# ==========================

print("Total Orders:", len(df))

# ==========================
# Average Rating
# ==========================

print("Average Rating:", round(df["Rating"].mean(),2))

# ==========================
# Category Wise Sales
# ==========================

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\nCategory Wise Sales")
print(category_sales)

# ==========================
# City Wise Sales
# ==========================

city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)

print("\nCity Wise Sales")
print(city_sales)

# ==========================
# Monthly Sales
# ==========================

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales")
print(monthly_sales)

# ==========================
# Charts
# ==========================

category_sales.plot(kind="bar", figsize=(8,5))
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


city_sales.plot(kind="bar", figsize=(8,5))
plt.title("City Wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


monthly_sales.plot(kind="line", marker="o", figsize=(8,5))
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
