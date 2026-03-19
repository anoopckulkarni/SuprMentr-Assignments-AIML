import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'Age': [19, 21, 20, 23, 31, 22, 35, 23, 64, 30, 67, 35, 58, 24, 37, 22, 52, 35, 59, 35],
    'Annual_Income': [15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 23, 23, 24, 24, 25, 25],
    'Spending_Score': [39, 81, 6, 77, 40, 76, 6, 94, 3, 72, 14, 99, 15, 77, 4, 79, 13, 98, 14, 73]
}
df = pd.DataFrame(data)

X = df[['Annual_Income', 'Spending_Score']]

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

centroids = kmeans.cluster_centers_
print("--- Cluster Centroids (Income, Spending Score) ---")
print(centroids)

plt.figure(figsize=(10, 6))

colors = ['red', 'blue', 'green', 'cyan', 'magenta']
for i in range(5):
    plt.scatter(X.iloc[df['Cluster'] == i, 0], 
                X.iloc[df['Cluster'] == i, 1], 
                s=100, c=colors[i], label=f'Cluster {i+1}')

plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='yellow', label='Centroids', marker='*')

plt.title('Mall Customer Clusters')
plt.xlabel('Annual Income ($k)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()