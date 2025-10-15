"""Week 9: Clustering using k-means on Iris dataset, study SSE and centroids."""
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def main():
    iris = datasets.load_iris()
    X = iris.data
    for k in [2,3,4,5]:
        kmeans = KMeans(n_clusters=k, random_state=42).fit(X)
        print(f"k={k} inertia (SSE)={kmeans.inertia_:.2f}")
        print("Centroids:\n", kmeans.cluster_centers_)
    # plot first two features clustering for k=3
    kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
    labels = kmeans.labels_
    plt.scatter(X[:,0], X[:,1], c=labels)
    plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker='x', s=100)
    plt.xlabel('Sepal length'); plt.ylabel('Sepal width')
    plt.title('k-means (k=3) on Iris (first two features)')
    plt.savefig('week9_kmeans_iris.png')
    print('Plot saved to week9_kmeans_iris.png')

if __name__=='__main__':
    main()
