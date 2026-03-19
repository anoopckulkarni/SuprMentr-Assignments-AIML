import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

print("---- COLLEGE: Student Performance Prediction ----")

college_data = {
    "attendance": [80, 60, 90, 70, 85, 50, 95, 65],
    "study_hours": [2, 1, 4, 3, 3, 1, 5, 2],
    "assignment_score": [70, 50, 90, 75, 80, 45, 95, 60],
    "result": [1, 0, 1, 1, 1, 0, 1, 0]
}

college_df = pd.DataFrame(college_data)
X_col = college_df[["attendance", "study_hours", "assignment_score"]]
y_col = college_df["result"]

model1 = LogisticRegression()
model1.fit(X_col, y_col)

new_student = pd.DataFrame([[85, 3, 80]], columns=["attendance", "study_hours", "assignment_score"])
pred1 = model1.predict(new_student)
print("Student Prediction (1=Pass, 0=Fail):", pred1[0])

print("\n---- HEALTHCARE: Disease Risk Prediction ----")

health_data = {
    "age": [25, 45, 50, 35, 60, 40, 55, 30],
    "blood_pressure": [120, 140, 150, 130, 160, 135, 155, 125],
    "cholesterol": [180, 220, 240, 200, 260, 210, 250, 190],
    "disease": [0, 1, 1, 0, 1, 0, 1, 0]
}

health_df = pd.DataFrame(health_data)
X_health = health_df[["age", "blood_pressure", "cholesterol"]]
y_health = health_df["disease"]

model2 = DecisionTreeClassifier()
model2.fit(X_health, y_health)

new_patient = pd.DataFrame([[50, 145, 230]], columns=["age", "blood_pressure", "cholesterol"])
pred2 = model2.predict(new_patient)
print("Disease Risk (1=Risk, 0=No Risk):", pred2[0])

print("\n---- SHOPPING: Purchase Prediction ----")

shop_data = {
    "age": [20, 25, 30, 35, 40, 28, 33, 45],
    "income": [20000, 30000, 40000, 50000, 60000, 35000, 45000, 65000],
    "browsing_time": [5, 10, 15, 20, 25, 12, 18, 30],
    "purchase": [0, 0, 1, 1, 1, 0, 1, 1]
}

shop_df = pd.DataFrame(shop_data)
X_shop = shop_df[["age", "income", "browsing_time"]]
y_shop = shop_df["purchase"]

model3 = KNeighborsClassifier(n_neighbors=3)
model3.fit(X_shop, y_shop)

new_shopper = pd.DataFrame([[32, 42000, 16]], columns=["age", "income", "browsing_time"])
pred3 = model3.predict(new_shopper)
print("Purchase Prediction (1=Yes, 0=No):", pred3[0])