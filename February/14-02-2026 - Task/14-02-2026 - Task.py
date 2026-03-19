import pandas as pd
import numpy as np

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'maths': [85, 90, 78, np.nan, 92, 45, 88, 76],
    'science': [92, 85, 80, 88, 95, 50, 70, 79],
    'english': [78, 95, 82, 91, 89, 40, 85, 80],
    'dept': ['CS', 'CS', 'EC', 'EC', 'CS', 'ME', 'ME', 'CS']
}
df_initial = pd.DataFrame(data)
df_initial.to_csv('students.csv', index=False)

df = pd.read_csv('students.csv')

df[['maths', 'science', 'english']] = df[['maths', 'science', 'english']].fillna(0)

df['total'] = df['maths'] + df['science'] + df['english']
df['average'] = df['total'] / 3

top_3 = df.sort_values(by='total', ascending=False).head(3)

dept_avg = df.groupby('dept')[['maths', 'science', 'english']].mean()

high_scorers = df[(df['maths'] > 75) & (df['science'] > 75) & (df['english'] > 75)]

df.to_csv('processed_students.csv', index=False)

print("Top 3 Students:")
print(top_3[['name', 'total']])
print("\nDepartment Wise Average Marks:")
print(dept_avg)
print("\nStudents scoring above 75 in all subjects:")
print(high_scorers[['name', 'maths', 'science', 'english']])