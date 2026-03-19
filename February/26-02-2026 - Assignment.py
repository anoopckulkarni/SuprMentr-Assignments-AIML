import pandas as pd
data = {
    "Name": ["Alice", "Bob", "alice", "Charlie", None],
    "Age": [25, 30, None, 35, 28],
    "City": ["New York", "London", "new york", "Paris", "London"]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Name"].fillna("Unknown", inplace=True)
df = df.drop_duplicates()
df["Name"] = df["Name"].str.lower().str.strip()
df["City"] = df["City"].str.lower().str.strip()

print("\nCleaned Dataset:\n")
print(df)