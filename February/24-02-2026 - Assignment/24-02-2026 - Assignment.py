import pandas as pd

df = pd.read_csv("data.csv")

print("Top 5 Rows:")
print(df.head())

highest_column = df.mean(numeric_only=True).idxmax()
print("\nColumn with Highest Average Value:", highest_column)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

print("\nTotal Missing Values:", df.isnull().sum().sum())