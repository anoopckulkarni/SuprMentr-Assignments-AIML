import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = {
    'hours_studied': [2, 3, 5, 1, 8, 7, 3, 9, 6, 2],
    'sleep_hours': [7, 8, 6, 5, 9, 7, 8, 6, 7, 5],
    'previous_score': [60, 65, 75, 50, 90, 85, 62, 95, 80, 55],
    'final_score': [65, 70, 80, 55, 95, 90, 68, 98, 85, 60]
}
df = pd.DataFrame(data)

X = df[['hours_studied', 'sleep_hours', 'previous_score']]
y = df['final_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("--- Model Performance Metrics ---")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

if r2 > 0.8:
    print("\nConclusion: The model is Good. High R² indicates it explains most of the variance.")
elif r2 > 0.5:
    print("\nConclusion: The model is Average. It shows a trend but needs more data or features.")
else:
    print("\nConclusion: The model is Bad. It fails to capture the relationship effectively.")