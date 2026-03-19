import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Math": [85, 78, 92, 70, 88],
    "Science": [90, 74, 89, 65, 91],
    "English": [88, 80, 95, 72, 84]
}

df = pd.DataFrame(data)
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = np.round(df["Total"] / 3, 2)

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"
df["Grade"] = df["Average"].apply(assign_grade)
topper = df.loc[df["Total"].idxmax()]
class_average = np.round(df["Average"].mean(), 2)

print("Student Data:\n")
print(df)
print("\nTopper:")
print(topper["Name"], "with Total =", topper["Total"])
print("\nClass Average:", class_average)