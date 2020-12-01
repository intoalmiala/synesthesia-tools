from sklearn.cluster import KMeans
import numpy as np

# dataset creation
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data[:, :3]

kmeans = KMeans(n_clusters = 3)
kmeans.fit(X)

# plot drawing
import matplotlib.pyplot as plt

fig = plt.figure()
axes = plt.axes(projection = "3d")

axes.scatter(X[:,0], X[:,1], X[:,2], c = kmeans.labels_)

plt.show()
