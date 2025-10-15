"""Week 10: Simple K-means implementation from scratch (no sklearn)."""
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import random

def kmeans(X, k, maxiter=100):
    n, d = X.shape
    centroids = X[np.random.choice(n, k, replace=False)]
    for iteration in range(maxiter):
        # assign
        dist = np.linalg.norm(X[:,None,:] - centroids[None,:,:], axis=2)
        labels = dist.argmin(axis=1)
        new_centroids = np.array([X[labels==i].mean(axis=0) if np.any(labels==i) else centroids[i] for i in range(k)])
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    inertia = sum(((X - centroids[labels])**2).sum(axis=1))
    return centroids, labels, inertia

def main():
    iris = datasets.load_iris()
    X = iris.data
    centroids, labels, inertia = kmeans(X, 3)
    print('Inertia:', inertia)
    print('Centroids:\n', centroids)
    # save plot
    import matplotlib.pyplot as plt
    plt.scatter(X[:,0], X[:,1], c=labels)
    plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=100)
    plt.savefig('week10_kmeans_custom.png')
    print('Plot saved to week10_kmeans_custom.png')

if __name__=='__main__':
    main()
