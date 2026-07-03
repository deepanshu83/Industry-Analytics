import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# LOAD DATASET
# ==========================
df = pd.read_csv("data/cleaned_superstore.csv")

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)
print(df.info())

# ==========================
# BASIC KPIs
# ==========================
print("\n" + "=" * 60)
print("TOTAL SALES")
print(df["Sales"].sum())

print("\n" + "=" * 60)
print("TOTAL PROFIT")
print(df["Profit"].sum())

print("\n" + "=" * 60)
print("TOTAL ORDERS")
print(df["Order ID"].nunique())

print("\n" + "=" * 60)
print("TOTAL CUSTOMERS")
print(df["Customer ID"].nunique())

# ==========================
# CATEGORY WISE SALES
# ==========================
print("\n" + "=" * 60)
print("CATEGORY WISE SALES")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ==========================
# REGION WISE PROFIT
# ==========================
print("\n" + "=" * 60)
print("REGION WISE PROFIT")

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(region_profit)

plt.figure(figsize=(8,5))
region_profit.plot(kind="bar", color="green")
plt.title("Region Wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# ==========================
# SEGMENT WISE SALES
# ==========================
print("\n" + "=" * 60)
print("SEGMENT WISE SALES")

segment_sales = (
    df.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(segment_sales)

plt.figure(figsize=(6,6))
segment_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Segment Wise Sales")
plt.tight_layout()
plt.show()

# ==========================
# TOP 10 PRODUCTS
# ==========================
print("\n" + "=" * 60)
print("TOP 10 PRODUCTS")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

plt.figure(figsize=(10,6))
top_products.plot(kind="barh")
plt.title("Top 10 Products")
plt.xlabel("Sales")
plt.tight_layout()
plt.show()

# ==========================
# TOP 10 STATES
# ==========================
print("\n" + "=" * 60)
print("TOP 10 STATES")

top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_states)

plt.figure(figsize=(10,6))
top_states.plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ==========================
# MONTHLY SALES TREND
# ==========================
df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print("\n" + "=" * 60)
print("MONTHLY SALES TREND")
print(monthly_sales)

plt.figure(figsize=(12,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# ==========================
# TOP 10 CUSTOMERS
# ==========================
print("\n" + "=" * 60)
print("TOP 10 CUSTOMERS")

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)

plt.figure(figsize=(10,6))
top_customers.plot(kind="bar")
plt.title("Top 10 Customers")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)