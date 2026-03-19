import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "marks": [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

X = df[["study_hours"]]   # Feature
y = df["marks"]           # Label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

prediction = model.predict([[5]])
print("\nPredicted Marks for 5 Study Hours:", prediction)

plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()