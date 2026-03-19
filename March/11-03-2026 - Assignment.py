import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'Annual_Income_k': [15, 16, 17, 18, 70, 72, 75, 78, 80, 85, 90, 20, 25, 30],
    'Spending_Score': [39, 81, 6, 77, 40, 45, 50, 55, 90, 95, 88, 10, 15, 20]
}
df = pd.DataFrame(data)

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['Annual_Income_k', 'Spending_Score']])

print("--- Customer Segmentation Results ---")
for i in range(3):
    group = df[df['Cluster'] == i]
    avg_income = group['Annual_Income_k'].mean()
    avg_spend = group['Spending_Score'].mean()
    print(f"Group {i}: Avg Income ${avg_income:.1f}k, Avg Spend Score {avg_spend:.1f}")

new_customer = [[60, 50]]
cluster_pred = kmeans.predict(new_customer)
print(f"\nA customer with $60k income belongs to Group {cluster_pred[0]}.")