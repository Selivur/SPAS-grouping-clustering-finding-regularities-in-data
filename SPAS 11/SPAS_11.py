# -*- coding: cp1251 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
from collections import Counter

dataset = pd.read_csv("balance-scale.csv", sep=',')

balanceScale_param = dataset.iloc[:, 1:5].values
balanceScale_class= dataset.iloc[:, 0:1].values
clusterer = KMeans(n_clusters=3)
clusterer.fit(balanceScale_param)
labels = clusterer.labels_
metrics.silhouette_score(balanceScale_param, labels, metric='chebyshev')
predictions = clusterer.predict (balanceScale_param)
print(metrics)
dataset ["cluster"]=predictions
print ("Початкові дані")
print (dataset, "\n")
print ("Загальна внутрішньо-кластерна сума квадратів відстаней від екземплярів до найближчого центроїда")
print (clusterer.inertia_, "\n")
centroids = clusterer.cluster_centers_
print ("Координати усіх центроїдів")
print (centroids, "\n")
print("Кількість ітерацій")
print(clusterer.max_iter)
print("К-сть у кластерах")
print(Counter(labels), "\n")
fig, ax = plt.subplots()
scatterl = ax.scatter(balanceScale_param[ : , 2], balanceScale_param[ : , 3], c=predictions, s=15, cmap='brg')
handles, labels = scatterl.legend_elements()
legendl = ax.legend(handles, labels, loc="upper right")
ax.add_artist (legendl)
scatter2 = ax.scatter(centroids[ : , 2], centroids[ : , 3], marker="x",c='purple', s=200, linewidths=3, label='centroids')
plt.legend(loc="lower right")
plt.xlabel (f"{dataset.columns[2]}")
plt.ylabel (f"{dataset.columns[3]}")

fig, ax = plt.subplots()
scatterl = ax.scatter(balanceScale_param[ : , 1], balanceScale_param[ : , 3], c=predictions, s=15, cmap='brg')
handles, labels = scatterl.legend_elements()
legendl = ax.legend(handles, labels, loc="upper right")
ax.add_artist (legendl)
scatter2 = ax.scatter(centroids[ : , 1], centroids[ : , 3], marker="x",c='purple', s=200, linewidths=3, label='centroids')
plt.legend(loc="lower right")
plt.xlabel (f"{dataset.columns[1]}")
plt.ylabel (f"{dataset.columns[3]}")

fig, ax = plt.subplots()
scatterl = ax.scatter(balanceScale_param[ : , 1], balanceScale_param[ : , 2], c=predictions, s=15, cmap='brg')
handles, labels = scatterl.legend_elements()
legendl = ax.legend(handles, labels, loc="upper right")
ax.add_artist (legendl)
scatter2 = ax.scatter(centroids[ : , 1], centroids[ : , 2], marker="x",c='purple', s=200, linewidths=3, label='centroids')
plt.legend(loc="lower right")
plt.xlabel (f"{dataset.columns[1]}")
plt.ylabel (f"{dataset.columns[2]}")
plt.show()