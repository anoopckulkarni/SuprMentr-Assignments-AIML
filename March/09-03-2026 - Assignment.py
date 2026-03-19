import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. CREATE THE DATASET
data = {
    'Square_Feet': [600, 850, 1100, 1350, 1500, 1800, 2200, 2500],
    'Price_Thousands': [155, 195, 240, 290, 310, 370, 450, 510]
}
df = pd.DataFrame(data)

# 2. SEPARATE FEATURES (X) AND TARGET (y)
X = df[['Square_Feet']]
y = df['Price_Thousands']

# 3. TRAIN THE MODEL
model = LinearRegression()
model.fit(X, y)

# 4. PREDICT WITH A NAMED DATAFRAME (Removes UserWarning)
new_input = pd.DataFrame({'Square_Feet': [1700]})
prediction = model.predict(new_input)

# 5. OUTPUT THE RESULTS
print(f"For 1700 sq ft, the predicted price is ${prediction[0]:.2f}k")