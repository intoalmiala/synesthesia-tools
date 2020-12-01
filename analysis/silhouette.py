import json
import sys
from functools import reduce
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

INPUT_FILE = sys.argv[1]
#OUTPUT_FILE = sys.argv[2]

with open(INPUT_FILE) as f:
    X = np.array(reduce(lambda x, y: x+y, json.load(f).values(), []))

colors = np.array([tuple(map(lambda x: x/255, X[i])) for i in range(len(X))])

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

cluster_colors = kmeans.cluster_centers_/255

# Plot drawing
import matplotlib.pyplot as plt

fig = plt.figure()

# For plotting only cluster colors
ax = plt.axes(projection = "3d")
ax.scatter(X[:,0], X[:,1], X[:,2], c = cluster_colors[kmeans.labels_])

# For plotting cluster colors and true colors side by side
#ax1 = fig.add_subplot(1, 2, 1, projection = "3d")
#ax1.scatter(X[:,0], X[:,1], X[:,2], c = cluster_colors[kmeans.labels_])
#
#ax2 = fig.add_subplot(1, 2, 2, projection = "3d")
#ax2.scatter(X[:,0], X[:,1], X[:,2], c = colors)

plt.show()
