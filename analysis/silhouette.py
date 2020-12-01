from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

# dataset creation
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data[:, :3]

max_n_clusters = 10
scores = [0 for _ in range(max_n_clusters+1)]
for n_clusters in range(2,max_n_clusters+1):
    kmeans = KMeans(n_clusters = n_clusters)
    prediction = kmeans.fit_predict(X)
    scores[n_clusters] = silhouette_score(X, prediction)
    print(f"For {n_clusters} clusters got a score of {scores[n_clusters]}.")

best_score = 0
best_n = 0
for n, score in enumerate(scores):
    if score > best_score:
        best_score = score
        best_n = n

print(f"Best cluster amount was {best_n} with a score of {best_score}.")

kmeans = KMeans(n_clusters = best_n)
kmeans.fit(X)

# plot drawing
import matplotlib.pyplot as plt

fig = plt.figure()
axes = plt.axes(projection = "3d")

axes.scatter(X[:,0], X[:,1], X[:,2], c = kmeans.labels_)

plt.show()
