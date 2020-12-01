import json
import sys
from functools import reduce
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

INPUT_FILE = sys.argv[1]
N_CLUSTERS = int(sys.argv[2])

# Read data from input file
with open(INPUT_FILE) as f:
    X = np.array(reduce(lambda x, y: x+y, json.load(f).values(), []))

kmeans = KMeans(n_clusters = N_CLUSTERS)
kmeans.fit(X)

cluster_colors = kmeans.cluster_centers_/255

# Plot drawing
import matplotlib.pyplot as plt

fig = plt.figure()

ax = plt.axes(projection = "3d")
ax.scatter(X[:,0], X[:,1], X[:,2], c = cluster_colors[kmeans.labels_])

plt.show()
