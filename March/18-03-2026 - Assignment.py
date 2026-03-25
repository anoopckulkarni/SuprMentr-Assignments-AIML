import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'Annual_Income': [15, 16, 17, 18, 70, 72, 75, 78, 80, 85, 90, 20, 25, 30, 85, 95],
    'Spending_Score': [39, 81, 6, 77, 40, 45, 50, 55, 90, 95, 88, 10, 15, 20, 10, 8]
}
df = pd.DataFrame(data)

X = df[['Annual_Income', 'Spending_Score']]


kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

plt.scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'], cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='black', marker='X')
plt.title('Mall Customer Segments')
plt.xlabel('Annual Income ($k)')
plt.ylabel('Spending Score (1-100)')
plt.show()