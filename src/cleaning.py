import pandas as pd

# Dataset Load
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

print("="*50)
print("First 5 Rows")
print(df.head())

print("="*50)
print("Dataset Information")
print(df.info())

print("="*50)
print("Missing Values")
print(df.isnull().sum())

print("="*50)
print("Duplicate Rows")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("data/cleaned_superstore.csv", index=False)

print("="*50)
print("Cleaning Completed Successfully!")