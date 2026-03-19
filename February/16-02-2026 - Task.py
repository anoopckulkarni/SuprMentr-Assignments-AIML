import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Alice', 'Grace'],
    'age': [25, 30, np.nan, 35, 28, np.nan, 25, 40],
    'salary': [50000, np.nan, 60000, 75000, np.nan, 45000, 50000, 80000],
    'city': ['hyderabad', 'HYDERABAD', 'Hyderabad', 'Bangalore', 'bangalore', 'CHENNAI', 'hyderabad', 'Chennai'],
    'experience': [2, 5, 3, 10, 4, 1, 2, 12]
}
df = pd.DataFrame(data)
df = df.drop_duplicates()
df['age'] = df['age'].fillna(df['age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].mean())
df['city'] = df['city'].str.title()

scaler = MinMaxScaler()
df[['age', 'salary']] = scaler.fit_transform(df[['age', 'salary']])
print("--- Final Cleaned Data ---")
print(df)