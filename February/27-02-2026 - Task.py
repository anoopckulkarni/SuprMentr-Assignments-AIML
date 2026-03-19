import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

k_values = range(1, 16)
euclidean_acc = []
manhattan_acc = []

for k in k_values:
    knn_e = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    knn_e.fit(X_train, y_train)
    euclidean_acc.append(accuracy_score(y_test, knn_e.predict(X_test)))
    
    knn_m = KNeighborsClassifier(n_neighbors=k, metric='manhattan')
    knn_m.fit(X_train, y_train)
    manhattan_acc.append(accuracy_score(y_test, knn_m.predict(X_test)))

plt.plot(k_values, euclidean_acc, marker='o', label='Euclidean')
plt.plot(k_values, manhattan_acc, marker='s', label='Manhattan')
plt.title('KNN Accuracy: Euclidean vs Manhattan')
plt.xlabel('Value of K')
plt.ylabel('Testing Accuracy')
plt.xticks(k_values)
plt.legend()
plt.grid(True)
plt.show()