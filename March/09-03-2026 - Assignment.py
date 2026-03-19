import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Square_Feet': [600, 850, 1100, 1350, 1500, 1800, 2200, 2500],
    'Price_Thousands': [155, 195, 240, 290, 310, 370, 450, 510]
}
df = pd.DataFrame(data)
X = df[['Square_Feet']]
y = df['Price_Thousands']

model = LinearRegression()
model.fit(X, y)

new_input = pd.DataFrame({'Square_Feet': [1700]})
prediction = model.predict(new_input)

print(f"For 1700 sq ft, the predicted price is ${prediction[0]:.2f}k")