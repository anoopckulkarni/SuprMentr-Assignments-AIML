import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'engine_size': [1000, 1200, 1500, 2000, 2500, 1100, 1800, 2200],
    'mileage': [15, 18, 22, 12, 10, 25, 14, 11],
    'age': [10, 8, 5, 3, 1, 12, 4, 2],
    'price': [300000, 450000, 700000, 900000, 1200000, 250000, 800000, 1100000]
}
df = pd.DataFrame(data)

X = df[['engine_size', 'mileage', 'age']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

new_car = pd.DataFrame([[1500, 20, 3]], columns=['engine_size', 'mileage', 'age'])
predicted_price = model.predict(new_car)

print(f"Predicted Price: {predicted_price[0]:.2f}")
print("\nCoefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.2f}")

importances = pd.Series(abs(model.coef_), index=X.columns)
most_impactful = importances.idxmax()
print(f"\nMost Impactful Feature: {most_impactful}")