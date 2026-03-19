import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = {
    'Income': [50000, 80000, 30000, 100000, 20000, 90000, 40000, 65000, 32000, 95000],
    'Credit_Score': [600, 750, 500, 800, 450, 780, 620, 700, 510, 820],
    'Age': [25, 40, 22, 50, 19, 45, 30, 35, 24, 48],
    'Loan_Amount': [10000, 20000, 5000, 50000, 2000, 40000, 15000, 25000, 8000, 55000],
    'Employment_Years': [2, 10, 1, 20, 0, 15, 4, 7, 1, 18],
    'Loan_Approved': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1] 
}
df = pd.DataFrame(data)

X = df.drop('Loan_Approved', axis=1)
y = df['Loan_Approved']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

dt_acc = accuracy_score(y_test, dt_pred)
rf_acc = accuracy_score(y_test, rf_pred)

print(f"Decision Tree Accuracy: {dt_acc * 100}%")
print(f"Random Forest Accuracy: {rf_acc * 100}%")

print("\n--- Feature Importance (Impact on Loan Approval) ---")
importances = rf_model.feature_importances_
feature_names = X.columns
for feature, importance in zip(feature_names, importances):
    print(f"{feature}: {importance:.4f}")

with open('loan_model.pkl', 'wb') as file:
    pickle.dump(rf_model, file)

print("\nSuccess: Model saved as 'loan_model.pkl'")